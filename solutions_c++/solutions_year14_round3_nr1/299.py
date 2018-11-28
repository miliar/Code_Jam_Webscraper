#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

template<class T>T gcd(T a,T b){while(b!=0){T r=a%b;a=b;b=r;}return a;}


void solve(){
	string s;
	LL a,b;
	scanf("%I64d/%I64d",&a,&b);
	LL g=gcd(a,b);
	a/=g;
	b/=g;
	if(b!=(b&-b)){cout<<"impossible"<<endl;return;}
	int ret=0;
	while(a<b){
		a*=2;++ret;
	}
	cout<<ret<<endl;
}

int main() {
	//ios_base::sync_with_stdio(0);
	cin.tie(0);
	int T;
	cin>>T;
	for(int i=1;i<=T;++i){
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
