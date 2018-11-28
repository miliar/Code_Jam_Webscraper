#include<bits/stdc++.h>
using namespace std;

int main(){
	long long t,n,d[10],j,i;
	cin>>t;
	for(i=1;i<=t;i++){
		cin>>n;
		fill(d,d+10,0);
		cout<<"Case #"<<i<<": ";
		long long a=n;
		if(n==0){
			cout<<"INSOMNIA\n";
			continue;
		}
		while(1){
			long long b=a;
			while(b>0){
				d[b%10]=1;
				b/=10;
			}
			for(j=0;j<10;j++)
				if(d[j]==0)
					break;
			if(j==10){
				cout<<a<<"\n";
				break;
			}
			else
				a+=n;
		}
	}
	return 0;
}