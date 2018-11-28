#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
//#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

const int bitsize = 32;
bool check(vector<int> s, int radix,int &witness){
    vector<int> v = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47};
    bool verified = false;
    for(int i=0;i<v.size();i++){
        int rem = 0;
        for(int j=0;j<s.size();j++){
            rem = (radix* rem+ s[j])%v[i];
        }
        if(rem==0){
            verified = true;
            witness = v[i];
            break;
        }
    }
    return verified;
    
}
ofstream cout("/Users/Nagi2/Documents/cccL.txt");

int main(int argc, const char * argv[]) {
    cout << "Case #1:" <<endl;
    vector <vector <int> > vout;
    vector <vector <int> > vw;
    while(vout.size()!=500){
        vector<int> v;
        for(int i=0;i<bitsize;i++){
            if(i==0) v.push_back(1);
            else if (i==bitsize-1) v.push_back(1);
            else v.push_back(rand()%2);
        }
        bool verified = true;
        vector <int> witnesses;
        for(int i=2;i<=10;i++){
            int witness;
            if(check(v,i,witness)==false) verified = false;
            witnesses.push_back(witness);
        }
        if(verified) {
            vout.push_back(v);
            vw.push_back(witnesses);
        }
    }
    for(int k=0;k<vout.size();k++){
        for(int a=0;a<vout[k].size();a++){
            cout << vout[k][a];
        }
        for(int a =0;a<vw[k].size();a++){
            cout << " " << vw[k][a];
        }
        
        cout << endl;
    }
    return 0;
}
