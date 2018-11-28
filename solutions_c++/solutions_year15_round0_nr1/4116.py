#include <bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define rep1(i,n) for(int i=1;i<=(int)(n);i++)
#define all(c) c.begin(),c.end()
#define pb push_back
#define fs first
#define sc second
#define show(x) cout << #x << " = " << x << endl
#define chmin(x,y) x=min(x,y)
#define chmax(x,y) x=max(x,y)
using namespace std;
int main(){
	int T;
	cin>>T;
	rep1(tt,T){
		int N;
		string s;
		cin>>N>>s;
		int sum=0,ans=0;
		rep(i,N+1){
			if(sum<i) ans++,sum++;
			sum+=s[i]-'0';
		}
		printf("Case #%d: %d\n",tt,ans);
	}
}
