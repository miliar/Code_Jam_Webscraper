/**
  * @author: Javier Monge (es.linkedin.com/pub/javier-monge/8b/50/808/)
  *
  */

#include <iostream>
#include <thread>
#include <algorithm>
#include <mutex>
#include <condition_variable>
#include <atomic>
#include <string>
#include <sstream>
#include <set>
#include <tuple>
#include <cmath>

#define NUM_THREADS 4

using namespace std;

vector<thread> workers;

vector<string> cases;

mutex mtx;  // For accesing cases.

condition_variable cond;    // For idling workers while no cases produced

int nCases; // Total number of cases

atomic<int> pCases; // Produced cases (readed)

atomic<int> cCases; // Consumed cases (solved)

/*
 * Function that solves the problem. Receives the case description in the caso argument
 * and stores the result in the same argument. Do not write 'Case #X: '.
 * */
void solve(string & caso){

    int res = 0;
    bool badmag = false;

    stringstream sin(caso);

    int fl[16];
    int sl[16];

    int fr, sr;

    sin >> fr;
    for(int i = 0; i < 16; i++){
        sin >> fl[i];
    }

    sin >> sr;
    for(int i = 0; i < 16; i++){
        sin >> sl[i];
    }

    fr--;
    sr--;

    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            if(fl[fr*4+i] == sl[sr*4+j]){
                if(res == 0){
                    res = fl[fr*4+i];
                }else{
                    badmag = true;
                }
            }
        }
    }

    if(badmag){
        caso = "Bad magician!";
    }else{
        if(res == 0){
            caso = "Volunteer cheated!";
        }else{
            caso = to_string(res);
        }
    }
}

// Gets a new case to solve
int getCase(string & caso){
    unique_lock<mutex> lock(mtx);
    int idxCase = nCases;
    cond.wait(lock, [](){return pCases > cCases || cCases >= nCases;});
    if(pCases > cCases){
        idxCase = cCases;
        caso = cases[cCases++];
    }
    cerr << "Got case: " << idxCase << "\n";
    return idxCase;
}

// Sets the result of a case
void setCase(int idxCase, string & caso){
    unique_lock<mutex> lock(mtx);
    cases[idxCase] = caso;
}

// Adds a new case to solve
void addCase(int idxCase, string & caso){
    unique_lock<mutex> lock(mtx);
    cases.insert(cases.begin() + idxCase, caso);
    pCases++;
    cond.notify_one();
}

/*
 * Funtion for workers
 * */
void work(){

    while(cCases < nCases){
        string caso;
        int idxCase = getCase(caso);
        if (idxCase < nCases){
            solve(caso);
            setCase(idxCase, caso);
        }
    }
    cond.notify_all();
}

/*
 * Function for reading cases
 * */
void iothread(){

    string line;
    string line2;

    for(int i = 0; i < nCases; i++){

        line = "";
        for(int j = 0; j < 10; j++){
            getline(cin, line2);

            line.append(" ");
            line.append(line2);
        }

        cerr << "CASE " << i << " IN: " << line << "\n";
        addCase(i, line);
    }

}

/*
 * Main thread. Shouldn't need modifications
 * */
int main()
{

    cerr << "START\n";

    string line;

    stringstream sline;

    getline(cin, line);

    sline << line;

    sline >> nCases;

    cerr << "#CASES: " << nCases << "\n";

    for(int i = 0; i < NUM_THREADS; i++){   // Create worker threads
        workers.push_back(thread(work));
    }

    iothread(); // Read the cases

    for(auto & th : workers){   // Wait for the workers to finnish
        th.join();
    }

    for(int i = 0; i < nCases; i++){    // Write the solution
        cout << "Case #" << i + 1 << ": " << cases[i] << "\n";
    }

    return 0;
}

