#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <unordered_set>
#include <stdio.h>
#include <string.h>
#include <unordered_map>
#include <fstream>
using namespace std;

#define MOD 1000000007
#define ll long long

ifstream fin("in.txt");
ofstream fout("out.txt");

int main(){
    int t;
    fin>>t;
    for(int asdasd=0; asdasd<t; asdasd++){
        double C,F,X;
        fin>>C>>F>>X;
        double rate=2;
        double t=0;
        while(X/rate > C/rate+X/(rate+F)){
            t+=C/rate;
            rate+=F;
        }
        t+=X/rate;
        fout<<"CASE #"<<asdasd+1<<": "<<std::setprecision(9)<<std::fixed<<t<<endl;
    }
    return 0;
}
