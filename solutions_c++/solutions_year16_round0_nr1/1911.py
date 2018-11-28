//A
//Code Jam 2016
#include <bits/stdc++.h>
using namespace std;
int main(){
	int t,t1;
	cin>>t;
	t1=t;
	while(t--){
		cout<<"Case #"<<t1-t<<": ";
		unsigned long long n;
		cin>>n;
		int v[10];
		memset(v,0,sizeof v);
		if(n>0){
			bool a = true;
			unsigned long long j=1;
			do{
				a = true;
				unsigned long long temp=n*j;
				//cout<<temp<<endl;
				while(temp>0){
					v[temp%10]=1;
					temp/=10;
				}				
				for (int i = 0; i < 10; i++)
				{
					if(!v[i]){
						a = false;
						break;
					}
				}	
				if(a)break;
				j++;
			}while(!a);
			cout<<n*j;
		}else{
			cout<<"INSOMNIA";
		}
		cout<<endl;
	}
	return 0;
}
