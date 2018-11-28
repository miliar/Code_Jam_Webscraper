#include<bits/stdc++.h>
using namespace std;
#define endll           "\n"
#define INIT(n,m)       memset(n,m,sizeof(n))
#define REP(i,n)        for(int i=0;i<n;i++)
#define FOR(i,a,b)      for(int i=a;i<=b;i++)
#define FORD(i,a,b)     for(int i=a;i>=b;i--)
#define PB              push_back
#define IN(a,b)         substr(a,b-a+1)
#define FF              first
#define SS              second
#define LEN(x)          ((int)x.size())
#define MM              1000000007
#define CHECK(x,y)      (((x%=y)+=y)%=y)
#define DEBUG(x)        {cout<<#x<<" = ";cout << (x) << endll;}
#define PR(v)           {cout<<#v<<" = ";for(auto _:v)cout<<_<<' ';cout<<endll;}
#define PRR(a,b,n)      {cout<<#a<<" = ";FOR(_,b,n)cout<<a[_]<<' ';cout<<endll;} 
#define FOREACH(it, c)  for(__typeof((c).begin())it=(c).begin();it!=(c).end();++it)
#define FILE_IO(a,b)    {freopen(a,"r",stdin);freopen(b,"w",stdout);}
struct  IO              {IO(){ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);}}_;
typedef long long ll;
typedef pair<int,int> ii;
int n,m,len,k,t,a,b;

ll pow(ll b,  ll e){
	if(e == 0) return 1;
	if(e == 1) return b;
	if(e%2 == 1) return b * pow(b,e-1);
	ll one = pow(b,e/2);
	return one * one;
}

int main(){
	FILE_IO("D-small-attempt0.in","output.txt");
	cin >> t;
	REP(tc,t){
		ll k,c,s;
		cin >> k >> c >> s;
		cout << "Case #" << tc+1 << ": ";
		ll con = pow(k,c-1);
		REP(i,k){
			if(i) cout << " ";
			cout << con * i + 1LL;
		}
		cout << endll;
	}
	return 0;
}
