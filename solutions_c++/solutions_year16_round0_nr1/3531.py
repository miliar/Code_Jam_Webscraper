#include<iostream>
#include<fstream>
using namespace std;
int main(){
	int t,i,j,k,x,l;
	cin>>t;
	
	for(k=1;k<=t;++k){
		cin>>x;
		
		int a[10]={0};
		int flag=1;
		for (i=1;i<=99;++i){
			l=x*i;
			flag=1;
			while(l){
				a[l%10]++;
				l/=10;
			}
			for (j=0;j<=9;++j) {
				if(a[j]==0) {
					flag=0;
					break;
				}
			}
			if(flag==1) break;
		}
		cout<<"Case #"<<k<<": ";
		if(flag==1) cout<<x*i;
		else cout<<"INSOMNIA";
		cout<<"\n";
	}
	
	return 0;
}
