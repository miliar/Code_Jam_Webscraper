#include <bits/stdc++.h>
using namespace std;
bool cc[10];
void c(long long a){
	while(a>0)
		cc[a%10]=1,a/=10;
}
int main(){
	int T,j;cin>>T;
	long long x,n,i;
	for(int k=1;k<=T;++k){
		cin>>n;
		bool is=0;
		memset(cc,0,sizeof(cc));
		for(i=1;i<=max(n*10,10000LL);++i){
			x = n*i;
			c(x);
			bool go=1;
			for(j=0;j<10;++j)
				if(!cc[j]){
					go=0;break;
				}
			if(go){is=1;break;}
		}
		cout<<"Case #"<<k<<": ";
		if(is)cout<<(i*n)<<endl;
		else cout<<"INSOMNIA\n";
	}
}
