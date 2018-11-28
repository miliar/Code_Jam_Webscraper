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
#include <list>
#include <functional>
#include <cmath>

#define NUM_THREADS 1

using namespace std;

vector<thread> workers;

vector<string> cases;

mutex mtx;  // For accesing cases.

condition_variable cond;    // For idling workers while no cases produced

int nCases; // Total number of cases

atomic<int> pCases; // Produced cases (readed)

atomic<int> cCases; // Consumed cases (solved)

struct state{
    vector<bool> flip;
};

struct statecmp{
    bool operator() (const state & st1, const state & st2) const{
        //return st1.grid < st2.grid;
        return false;
    }
};

/*
 * Function that solves the problem. Receives the case description in the caso argument
 * and stores the result in the same argument. Do not write 'Case #X: '.
 * */
void solve(string & caso){

    stringstream sin(caso);

    int maxS;

    int result = 0;

    sin >> maxS;

    string audstr;

    sin >> audstr;

    vector<int> audience;

    for ( unsigned int i = 0; i < audstr.size(); i++){
        audience.push_back(stoi(string(1, audstr[i])));
    }

    int stand = 0;

    for(unsigned int i = 0; i < ( audience.size() - 1); i++){
        stand += audience[i];
        if ( stand < ( i + 1 ) ){
            result += ( ( i + 1 ) - stand );
            stand += ( ( i + 1 ) - stand );
        }
    }

    caso = to_string(result);

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

    for(int i = 0; i < nCases; i++){

        string line;

        getline(cin, line);

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
        if(i > 0){cout << "\n";}
        cout << "Case #" << i + 1 << ": " << cases[i];
    }

    return 0;
}

