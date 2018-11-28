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

long long basenumber[]={1,2,3,11,22, 101,111,121,202,212, 1001,1111,2002, 10001,10101,10201,11011,11111,11211,20002,20102,
                        100001,101101,110011,111111,200002, 1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002};

int main()
{
    ifstream cin("C-large-1.in");
    ofstream cout("out.txt");
    rep(i,39)   basenumber[i]*=basenumber[i];

    int T;
    cin>>T;
    rep(i,T){
        long long a,b;
        cout<<"Case #"<<i+1<<": ";
        cin>>a>>b;
        int cnt(0);
        rep(i,39){
            if(basenumber[i]>=a && basenumber[i]<=b)   cnt++;
        }
        cout<<cnt<<endl;
    }
    return 0;
}
