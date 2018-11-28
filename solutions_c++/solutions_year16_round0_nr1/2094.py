/* 
 * File:   main.cpp
 * Author: Timo
 *
 * Created on 9. huhtikuutata 2016, 21:21
 */

#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    //ifstream ifs("input.txt");
    //ifstream ifs("A-small-attempt1.in");
    ifstream ifs("A-large.in");
    ofstream ofs("output.txt");
    
    int T;
    ifs >> T;
    
    for(int test=1; test<=T; test++) {
        ofs << "Case #" << test << ":";
        cout << "Case #" << test << ":";
        
        int N;
        ifs >> N;
        
        if(N == 0) {
            ofs << " INSOMNIA" << endl;
            cout << " INSOMNIA" << endl;
            continue;
        }
        
        int M = N;
        
        bool seen[10];
        for(int i=0; i<10; ++i) seen[i] = 0;
        
        while(true) {
            int K = M;
                //cout << K << ": ";
            while(K>0) {
                seen[K%10] = true;
                //cout << (K%10) << " ";
                K /= 10;
            }
                //cout << endl;
            
            bool all_seen=true;
            for(int i=0; i<10; ++i) if(!seen[i]) all_seen=false;
            if(all_seen) break;
            
            M += N;
        }
        
        ofs << " " << M << endl;
        cout << " " << M << endl;
        
    }
    
    return 0;
}

