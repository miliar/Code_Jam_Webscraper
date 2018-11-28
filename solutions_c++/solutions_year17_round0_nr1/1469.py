#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <chrono> //1e+9で割る auto end= chrono::system_clock::now()-st;  cout<<end.count()%1e+9<<endl;
using namespace std;
typedef long long ll;
typedef pair<ll,ll> P;
typedef long double db;

#define fr first
#define sc second
#define pb push_back
#define rep(i,x) for(ll i=0;i<x;i++)
#define rep1(i,x) for(ll i=1;i<=x;i++)
#define rrep(i,x) for(ll i=x-1;i>=0;i--)
#define rrep1(i,x) for(ll i=x;i>0;i--)
ll T;
string st;
ll s[1000];
ll L;
ll K;
bool b[1000];
int main()
{
	cin>>T;
	rep1(ctt,T){
		cin>>st;
		cin>>K;
		memset(b,0,sizeof(b));
		L=st.size();
		rep(i,L){
			if(st[i]=='+') s[i]=1;
			else s[i]=0;
		}
		ll ans=0;
		ll sum=0;
		rep(i,L){
			if(i>=K&&b[i-K]) sum--;
			if(i<L-K+1){
				if((s[i]+sum)%2==0){
					b[i]=1;
					sum++;
					ans++;
				}
			}
			else if((s[i]+sum)%2==0){
				cout<<"Case #"<<ctt<<": Impossible"<<endl;
				goto next;
			}
		}
		cout<<"Case #"<<ctt<<": "<<ans<<endl;
		next: ;
	}
}
