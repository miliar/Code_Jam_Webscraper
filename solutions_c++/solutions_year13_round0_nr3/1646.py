/*
  ------------------------- Hachiikung ---------------------------------
  ---------------------- Worrachate Bosri ------------------------------
  ------ Faculty of Computer Engineering Chulalongkorn University ------
*/
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<stack>
#include<set>
#include<map>
#include<string>
#include<utility>
using namespace std;
#define REP(i,FN) for(int i=0;i<FN;i++)
#define FOR(i,ST,FN) for(int i=ST;i<=FN;i++)
#define FORD(i,FN,ST) for(int i=FN;i>=ST;i--)
#define FORX(i,c) for(typeof(c.begin())i=c.begin();i!=c.end();i++)
#define pause system("pause")
#define S scanf
#define P printf
#define X first
#define Y second
#define pb push_back
#define PII pair<int,int>
#define sz size()

const int MOD(1000000007);
const int INF((1<<30)-1);
const int MAXN();

vector<long long>a;

bool ispalindrome(long long num){

    vector<int>b;

    while(num)
    {
        b.pb(num%10);
        num/=10;
    }

    REP(i,b.sz)
     if(b[i]!=b[b.sz-1-i])
      return 0;

    return 1;
}

int solve(int t){

    long long x,y;
    cin >> x >> y;

    int ans=0;
    REP(i,a.sz)
     if( a[i]>=x && a[i]<=y )
      ans++;

    P("Case #%d: %d\n",t,ans);
}

int main(){

    freopen("1input.txt","r",stdin);
    freopen("1output.txt","w",stdout);

    for(long long i=1;i<=10000000;i++)
     if( ispalindrome(i) && ispalindrome(i*i) )
      a.pb(i*i);

    int t;
    S("%d",&t);
    FOR(i,1,t)
     solve(i);

}










