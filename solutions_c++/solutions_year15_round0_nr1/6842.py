#include <stdio.h>
#include <string>
#include <iostream>
#include <queue>
#include <vector>
#include <sstream>
#include <iterator>
using namespace std;
void solve();

void solve(int test_index){
    int answer;
    int smax; 
    vector<int> si;//= new vector<double>();
    scanf("%d", &smax);
    string si_input;
    
    cin >> si_input;
   
    for(int i=0; i<=smax; i++){    
        int val;
        if (si_input.at(i) == '0') val = 0;
        if (si_input.at(i) == '1') val = 1;
        if (si_input.at(i) == '2') val = 2;
        if (si_input.at(i) == '3') val = 3;
        if (si_input.at(i) == '4') val = 4;
        if (si_input.at(i) == '5') val = 5;
        if (si_input.at(i) == '6') val = 6;
        if (si_input.at(i) == '7') val = 7;
        if (si_input.at(i) == '8') val = 8;
        if (si_input.at(i) == '9') val = 9;
        si.push_back(val);
    }
  
    int sum = si[0];
    int friends = 0;
    for(int i=1;i<si.size();i++){
        if (si[i] != 0 && i > sum){
            friends += (i-sum);
            sum = i + si[i];
        }
        else sum += si[i];
    }
    answer = friends;
    
    printf("Case #%d: %d\n", test_index, answer);
    
}

int main(void) {

    string fname = "A-large";
    freopen((fname+".in").c_str(), "r", stdin);
    freopen((fname+".out").c_str(), "w", stdout);
    unsigned short int testcases;
    scanf("%d", &testcases);
    
    for(int i=1; i <= testcases; i++) { //loops for each case
        solve(i);
    }
    
    return 0;
}