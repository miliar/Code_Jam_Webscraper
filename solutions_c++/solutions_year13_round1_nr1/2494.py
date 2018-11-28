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

long long maxblacks(long long r,long long t){

long long u1=r*2+1;
double ans=sqrt((u1-2)*(u1-2)+8*t);
ans+=2-u1;
long long ians=ans/4;
return ians;
}

int main()
{
    ifstream fin("A-small-attempt0(1).in");
    ofstream fout("out.txt");
    int T;
    fin>>T;
    rep(i,T){   // For each test case
        fout<<"Case #"<<i+1<<": ";      // Print Case #i:
        long long r,t;
        fin>>r>>t;
        fout<<maxblacks(r,t)<<endl;


    }
    return 0;
}
