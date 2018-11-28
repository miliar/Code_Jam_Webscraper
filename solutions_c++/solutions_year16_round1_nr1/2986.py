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

/*
BAAA
*/
int main(){
	FILE_IO("A-large.in","output.out");
	cin >> t;
	REP(tc,t){
		string s; cin >> s;
		deque<char> dq;
		for(auto cur:s){
			if(LEN(dq) == 0){
				dq.push_back(cur);
				continue;
			}
			
			if(cur < dq.front()){
				dq.push_back(cur);
			}
			else if(cur > dq.front()){
				dq.push_front(cur);
			}
			else{
				char c = '0';
				for(auto cur2:dq){
					if(cur2 != dq.front()){
						c = cur2;
						break;
					}
				}
				
				if(c == '0'){
					dq.push_front(cur);
				}
				else if(c > dq.front()){
					dq.push_back(cur);
				}
				else{
					dq.push_front(cur);
				}
			}
		}
		cout << "Case #" << tc+1 << ": ";
		for(auto cur:dq) cout << cur;
		cout << endll;
	}
	return 0;
}
