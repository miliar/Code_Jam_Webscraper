#include <iostream>
#include <ctime>
#include <fstream>
#include <map>
#include <vector>
#include <set>
#include <stdlib.h>
#include <cmath>
#include <string>
#define ll long long 

#define FOR(i,a,b) for(ll i=(a);i<(b);i++)
#define IFOR(i,a,b) for(int i=(b-1);i>(a-1);i--)

using namespace std;

int T;
ll MAX = pow(10,6)+1;
int main() {
    clock_t start = clock();
    ofstream out;
    // out.open("out.out");
    out.open("sol");
    ifstream fileIn;
    fileIn.open("out.out");
    
    cin >> T;

    // Generate in
    // out << 100 << endl;
    // FOR(i,0,MAX){
    //     out << i << endl;
    // }
    
    // Generate out
    int N;
    cout << T << endl;
    FOR(i,0,T) {
        cin >> N;
        if(N == 0) {
           out << "Case #" << i+1 << ": "<< "INSOMNIA" << endl;
        //    out << 0 << endl;
           continue;
        }
        
        set<char> digits;
        bool passed = false;
        ll val;
        FOR(j,1,100) {
            val = j*N;
            for(char& c: to_string(val)){
                digits.insert(c);
            }
            if (digits.size() == 10) {
                out << "Case #" << i+1 << ": " << val << endl;
                // out << val << endl;
                passed = true;
                break;
            }
        }
        if (!passed) {
            cout << "bad stuff here: "<< N << endl;
            out << "Case #" << i+1 << ": " << "INSOMNIA" << endl; 
        //    out << 0 << endl; 
        }
    }
    
    // Parse in and find
    // ll lookup [MAX]; 
    // ll val;
    // FOR (i, 0, MAX) {
    //     fileIn >> val;
    //     lookup[i] = val;
    // }
    
    // cout << "ending array" << endl;
    
    // ll key;
    // FOR(i, 0, T){
    //     cin >> key;
    //     if(key == 0) {
    //         out << "Case #" << i+1 << ": INSOMNIA" << endl;            
    //     } else {
    //         out << "Case #" << i+1 << ": " << lookup[key] << endl;            
    //     }
    // }
    
    out.close();
    fileIn.close();

    cout << "Timing: " << ( clock() - start ) / (double) CLOCKS_PER_SEC << endl;
    return 0;
}
