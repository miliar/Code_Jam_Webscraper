#include <bits/stdc++.h>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <string>
#include <vector>
#include <deque>
//#include "prettyprint.h"
#include <deque>
#include <fstream>
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
#define M_PI 3.14159265358979323846
#define MP make_pair
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()
#define LD long double
#define INF 1000000000
#define int long long
void ciphers(int n, set<int> & nums){
    while(n){
        nums.insert(n % 10);
        n /= 10;
    }
}
 //Begin of the code
#undef int
int main() {
#define int long long
    int maks = 0;
    int t;
    cin>>t;
    REP(q,t){
        int a;
        cin>>a;
        cout<<"Case #"<<q + 1<<": ";
        if(a == 0){
            cout<<"INSOMNIA";
        } else{
            set<int> nums;
            int j = a;
            ciphers(j, nums);
            while(nums.size() != 10){
                j += a;
                ciphers(j, nums);
            }
            cout<<j;
        }
        cout<<"\n";
    }

    return 0;
}
