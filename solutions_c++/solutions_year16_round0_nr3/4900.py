#include <fstream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <set>
#include <iterator>
#include <map>
#include <cmath>
#include <queue>
#include <ctime>

using namespace std;


ifstream in("input.txt");
ofstream out("output.txt");

int t,n,j,pr[11];

int is_prime(long long x){
    for (long long j=2;j<x;j++){
        if ((long long)j*j>x) break;
        if (x%j==0) return j;
    }
    return -1;
}

void rec(int m,string s){
    if (j==0) return;
    if (m==n){
        if (s[m-1]!='1') return;
        for (int i=2;i<=10;i++){
            long long x=0;
            for (int j=0;j<m;j++)
                x=x*i+(s[j]-'0');
            pr[i] = is_prime(x);
            if (pr[i]==-1) return;
        }
        out << s;
        for (int i=2;i<=10;i++) out << " " << pr[i];
        out << endl;
        j--;
        return;
    }
    rec(m+1,s+'0');
    rec(m+1,s+'1');
}

int main(int argc, const char * argv[]) {
    in >> t;
    int it=1;
    while (it<=t){
        out << "Case #" << it << ":" << endl;
        in >> n >> j;
        rec(1,"1");
        out << endl;
        it++;
    }
    
    return 0;
}