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

set<int> s;

void add(int x){
	while(x){
		s.insert(x%10);
		x/=10;
	}	
}

int main(){
	FILE_IO("A-large.in","output.txt");
	cin >> t;
	REP(tc,t){
		cin >> n;
		if(n == 0){
			cout << "Case #" << tc+1 << ": INSOMNIA\n";
			continue;
		}
		s.clear();
		int i;
		for(i=1;;i++){
			add(i*n);
			if(LEN(s) == 10){
				break;
			}
		}
		
		cout << "Case #" << tc+1 << ": " << i*n << endll;
	}
	return 0;
}
