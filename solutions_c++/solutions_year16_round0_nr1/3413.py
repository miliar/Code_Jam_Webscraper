#include<bits/stdc++.h>
#define endl "\n"
using namespace std;
typedef long long ll;
int a[10];
int main(){	
	ios_base::sync_with_stdio(0);
	int T;
	cin>>T;
	for(int xx=1;xx<=T;xx++){
		memset(a,0,sizeof(a));
		ll N;
		cin>>N;
		ll ori=N;
		if(N==0){cout<<"Case #"<<xx<<": "<<"INSOMNIA"<<endl;continue;}
		while(true){
			ll temp=N;
			while(temp>0){
				int digit=temp%10;
				temp/=10;
				a[digit]=1;
			}
			bool fg=true;
			for(int i=0;i<=9;i++){
				if(a[i]==0)fg=false;
			}
			if(fg){break;}
			N+=ori;
		}
		cout<<"Case #"<<xx<<": "<<N<<endl;
	}
	return 0;
}