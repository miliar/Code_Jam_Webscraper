#include<iostream>
#include<algorithm>
using namespace std;

void solve(int t){
	int n,m0;
	bool f[10],g;
	cin>>n;
	fill(f,f+10,false);
	for(int i=1;i<=1000;++i){
		g=true;
		int m=i*n;
		m0=i*n;
		while(m>0){
			f[m%10]=true;
			m/=10;
		}
		for(int j=0;j<10;++j){
			if(!f[j]){
				g=false;
				break;
			}
		}
		if(g){
			break;
		}
	}
	cout<<"Case #"<<t<<": ";
	if(g){
		cout<<m0<<endl;
	}else{
		cout<<"INSOMNIA"<<endl;
	}
}

int main(){
	int T;
	cin>>T;
	for(int t=1;t<=T;++t){
		solve(t);
	}
}