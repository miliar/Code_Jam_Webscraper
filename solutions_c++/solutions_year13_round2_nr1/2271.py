#include <iostream>
#include <fstream>

#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>

#include <algorithm>
#include <functional>
#include <sstream>
#include <utility>

#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include "gmpxx.h"
typedef mpz_class big;

using namespace std;

typedef vector<int>     vi;
typedef pair<int,int>   ii;
typedef vector<ii>      vii;
typedef long long       ll;
typedef set<int>        si;
typedef map<string,int> msi;

#define sz(a)   int((a).size())
#define all(c)  (c).begin(),(c).end()
#define pb(a)      push_back(a);
#define rep(i,n)    for(int i(0);i<int(n);i++)
#define TRvi(c,it)  for(vi::iterator it=(c).begin();it!=(c).end();it++)
#define INF 2E9

int N;

int minop(vi &motes,long long motesize,int n)
{
    if(n==N)  return 0;

    if(motes[n]<motesize)   return minop(motes,motesize+motes[n],n+1);
    else if(motesize==1)    return 1+minop(motes,motesize,n+1);
    else    return min(1+minop(motes,motesize*2-1,n),1+minop(motes,motesize,n+1));
}

int main()
{
    ifstream fin("A-small-attempt1.in");
    ofstream fout("out.txt");
    int T;
    fin>>T;
    rep(i,T){   // For each test case
        fout<<"Case #"<<i+1<<": ";      // Print Case #i:
        long long A;
        fin>>A>>N;
        vi motes(N);
        rep(j,N){
            int a; fin>>a;
            motes[j]=a;
        }
        sort(all(motes));
        /*rep(j,motes.size()){
            if(motes[j]<A)  A+=motes[j];
            else if(motes[j]<A+A-1){
                cnt++;  A+=A-1;
            }
            else    cnt++;
        }*/
        fout<<minop(motes,A,0)<<endl;




    }
    return 0;
}
