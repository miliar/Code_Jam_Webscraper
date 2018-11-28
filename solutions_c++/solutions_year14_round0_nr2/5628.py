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
#include <queue>
#include <tuple>
#include <array>
#include <functional>
#include <cmath>
#include <iomanip>
#include <sstream>

#define NUM_THREADS 4

using namespace std;

vector<thread> workers;

vector<string> cases;

mutex mtx;  // For accesing cases.

condition_variable cond;    // For idling workers while no cases produced

int nCases; // Total number of cases

atomic<int> pCases; // Produced cases (readed)

atomic<int> cCases; // Consumed cases (solved)

struct state{
    double rate;
    double ammount;
    double time;
};

/*
 * Function that solves the problem. Receives the case description in the caso argument
 * and stores the result in the same argument. Do not write 'Case #X: '.
 * */
void solve(string & caso){

    stringstream sin(caso);

    double res = 0.0;

    double C, F, X;

    bool found = false;

    sin >> C >> F >> X;

    queue<state> search;
    queue<state> next;

    state init;
    init.rate = 2.0;
    init.ammount = 0.0;
    init.time = 0.0;

    search.push(init);

    state cs;
    state es;

    while(!search.empty()){

        while( !search.empty() ){
            cs = search.front();
            search.pop();

            if ( (C- cs.ammount) > 0.000001 ){
                double ttf = ( C - cs.ammount ) / cs.rate;

                if( !found || (found && (res > (cs.time + ttf))) ){

                    es.ammount = 0;
                    es.rate = cs.rate + F;
                    es.time = cs.time + ttf;

                    next.push(es);

                    es.ammount = cs.ammount + cs.rate * ttf;
                    es.rate = cs.rate;
                    es.time = cs.time + ttf;

                    next.push(es);
                }

            }else{
                double ttx = ( X - cs.ammount ) / cs.rate;

                if(!found){
                    found = true;
                    res = cs.time + ttx;
                }else{
                    if(res > (cs.time + ttx)){
                        res = cs.time + ttx;
                    }
                }

            }

        }

        search = next;
        next = queue<state>();

    }

    ostringstream osres;
    osres << fixed << setprecision(10) << res;

    //caso = to_string(res);

    caso = osres.str();

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

    for(int i = 0; i < nCases; i++){

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
        cout << "Case #" << i + 1 << ": " << cases[i] << "\n";
    }

    return 0;
}

