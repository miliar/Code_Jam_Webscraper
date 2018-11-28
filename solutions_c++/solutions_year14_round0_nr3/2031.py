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
    string grid;
    int m;
};

struct statecmp{
    bool operator() (const state & st1, const state & st2) const{
        return st1.grid < st2.grid;
    }
};

/*
 * Function that solves the problem. Receives the case description in the caso argument
 * and stores the result in the same argument. Do not write 'Case #X: '.
 * */
void solve(string & caso){

    stringstream sin(caso);

    int R, C, M;

    sin >> R >> C >> M;

    bool poss = false;
    bool swap = C > R;
    string grid(R*C, '.');

    if( C * R > M){

        if(M > 0){

            if(C == 1 || R == 1){
                poss = true;
                for(int i = 0; i < R*C-1; i++){
                    if(i < M){
                        grid[i] = '*';
                    }
                }
            }else if(C == 2 && R == 2){
                if(M == 3){
                    poss = true;
                    grid = "***c";
                }
            }else{

                set<state, statecmp> search;

                state init;
                init.m = M;
                init.grid = grid;

                search.insert(init);

                while( !poss && !search.empty()){

                    set<state, statecmp>::iterator it = search.begin();

                    state st = *it;
                    search.erase(it);

                    if(st.m == 0){
                        grid = st.grid;
                        poss = true;
                    }else{

                        bool cont = true;
                        for(int r = 0; r < R-1; r++){
                            cont = true;
                            for(int c = 0; c < C-1 && cont; c++){
                                if(r == 0 && st.grid[c] == '.'){
                                    if(c < C-2 && r < R - 2){
                                        state next;
                                        next.grid = st.grid;
                                        next.grid[c] = '*';
                                        next.m = st.m - 1;

                                        search.insert(next);
                                        cont = false;
                                    }else if(r < R-2 && st.m > 1){
                                        state next;
                                        next.grid = st.grid;
                                        next.grid[c] = '*';
                                        next.grid[c+1] = '*';
                                        next.m = st.m - 2;

                                        search.insert(next);
                                        cont = false;
                                    }else if(c < C-2 && st.m > 1){
                                        state next;
                                        next.grid = st.grid;
                                        next.grid[c] = '*';
                                        next.grid[C+c] = '*';
                                        next.m = st.m - 2;

                                        search.insert(next);
                                        cont = false;
                                    }else if(st.m > 2){
                                        state next;
                                        next.grid = st.grid;
                                        next.grid[c] = '*';
                                        next.grid[c+1] = '*';
                                        next.grid[C+c] = '*';
                                        next.m = st.m - 3;

                                        search.insert(next);
                                        cont = false;
                                    }
                                }else{
                                    if(st.grid[r*C+c] == '.' && st.grid[(r-1)*C+c] == '*'){
                                        if(r < R-2){

                                            if(c < C-2){
                                                state next;
                                                next.grid = st.grid;
                                                next.grid[r*C+c] = '*';
                                                next.m = st.m - 1;

                                                search.insert(next);
                                                cont = false;
                                            }else if(st.m > 1){
                                                state next;
                                                next.grid = st.grid;
                                                next.grid[r*C+c] = '*';
                                                next.grid[r*C+c+1] = '*';
                                                next.m = st.m - 2;

                                                search.insert(next);
                                                cont = false;
                                            }
                                        }else{
                                            if(c < C-2 && st.m > 1){
                                                state next;
                                                next.grid = st.grid;
                                                next.grid[r*C+c] = '*';
                                                next.grid[(r+1)*C+c] = '*';
                                                next.m = st.m - 2;

                                                search.insert(next);
                                                cont = false;

                                            }else if(st.m > 2){
                                                state next;
                                                next.grid = st.grid;
                                                next.grid[r*C+c] = '*';
                                                next.grid[r*C+c+1] = '*';
                                                next.grid[(r+1)*C+c] = '*';
                                                next.m = st.m - 3;

                                                search.insert(next);
                                                cont = false;
                                            }
                                        }
                                    }
                                }
                            }
                        }

                        for(int c = 0; c < C - 1; c++){
                            cont = true;
                            for(int r = 0; r < R-1 && cont; r++){
                                if(c == 0 && st.grid[r*C] == '.'){
                                    if(r < R-2 && c < C - 2){
                                        state next;
                                        next.grid = st.grid;
                                        next.grid[r*C] = '*';
                                        next.m = st.m - 1;

                                        search.insert(next);
                                        cont = false;
                                    }else if(c < C-2 && st.m > 1){
                                        state next;
                                        next.grid = st.grid;
                                        next.grid[r*C] = '*';
                                        next.grid[(r+1)*C] = '*';
                                        next.m = st.m - 2;

                                        search.insert(next);
                                        cont = false;
                                    }else if(r < R - 2 && st.m > 1){
                                        state next;
                                        next.grid = st.grid;
                                        next.grid[r*C] = '*';
                                        next.grid[r*C+1] = '*';
                                        next.m = st.m;

                                        search.insert(next);
                                        cont = false;
                                    }else if(st.m > 2){
                                        state next;
                                        next.grid = st.grid;
                                        next.grid[r*C] = '*';
                                        next.grid[(r+1)*C] = '*';
                                        next.grid[(r)*C+1] = '*';
                                        next.m = st.m - 3;

                                        search.insert(next);
                                        cont = false;
                                    }
                                }else{
                                    if(st.grid[r*C+c] == '.' && st.grid[r*C+c-1] == '*'){
                                        if(c < C-2){
                                            if(r < R-2){
                                                state next;
                                                next.grid = st.grid;
                                                next.grid[r*C+c] = '*';
                                                next.m = st.m - 1;

                                                search.insert(next);
                                                cont = false;
                                            }else if(st.m > 1){
                                                state next;
                                                next.grid = st.grid;
                                                next.grid[r*C+c] = '*';
                                                next.grid[(r+1)*C+c] = '*';
                                                next.m = st.m - 2;

                                                search.insert(next);
                                                cont = false;
                                            }
                                        }else{
                                            if(r < R-2 && st.m > 1){
                                                state next;
                                                next.grid = st.grid;
                                                next.grid[r*C+c] = '*';
                                                next.grid[r*C+c+1] = '*';
                                                next.m = st.m - 2;

                                                search.insert(next);
                                                cont = false;
                                            }else if(st.m > 2){
                                                state next;
                                                next.grid = st.grid;
                                                next.grid[r*C+c] = '*';
                                                next.grid[r*C+c+1] = '*';
                                                next.grid[(r+1)*C+c] = '*';
                                                next.m = st.m - 3;

                                                search.insert(next);
                                                cont = false;
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }

        }else{
            poss = true;
        }

        grid[(R-1)*(C)+C-1] = 'c';

    }

    if(poss){

        stringstream ss;

        for(int i = 0; i < R; i++){
            if( i < R){
                ss << "\n";
            }
            for(int j = 0; j < C; j++){
                ss << grid[i*C+j];
            }

        }
        caso = ss.str();

    }else{
        caso = "\nImpossible";
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
        if(i > 0){cout << "\n";}
        cout << "Case #" << i + 1 << ":" << cases[i];
    }

    return 0;
}

