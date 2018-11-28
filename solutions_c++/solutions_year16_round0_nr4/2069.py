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
    //ifstream ifs("D-small-attempt3.in");
    ifstream ifs("D-large.in");
    ofstream ofs("output.txt");
    
    int T;
    ifs >> T;
    
    for(int test=1; test<=T; test++) {
        ofs << "Case #" << test << ":";
        cout << "Case #" << test << ":";
        
        int K,C,S;
        ifs >> K >> C >> S;
        
        if(K > C*S) {
            ofs << " IMPOSSIBLE" << endl;
            cout << " IMPOSSIBLE" << endl;
            continue;
        }
        
        int foo = C;
        //while((foo-1)*C >= K)
        //    foo--;
        int j=0;
        long long i=0;
        while(true) {
            long long val = 0;
            for(int j=0; j<foo; ++j) {
                val *= K;
                val += i;
                i++;
                if(i>=K) break;
            }
            ofs << " " << (val+1);
            cout << " " << (val+1);
            j++;
            if(j>S) {cout << endl; cout << C << " " << i << " " << S << endl; cout.flush();throw;};
            if(i>=K) break;
        }
        ofs << endl;
        cout << endl;
    }
    
    return 0;
}

