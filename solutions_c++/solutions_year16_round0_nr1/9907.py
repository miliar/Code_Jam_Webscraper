#include <iostream>
using namespace std;
int finish(int *);
int main(){
	int t;
	cin>>t;
	int i;
	for(i=1;i<=t;i++){
		long long n,m,k;
		int j=1;
		cin>>n;
		int a[10]={0};
		if(n==0){
			cout<<"Case #"<<i<<": INSOMNIA";
		}
		else{
			k=n;
			while(1){
			
				n=k*j;
				m=n;
				while(m){
					a[m%10]=1;
					m/=10;
				}	
				if(finish(a)==1){
					cout<<"Case #"<<i<<": "<<n;
					break;
				}
				j++;
		}	
		}
		cout<<endl;
	}
}
int finish(int *a){

	int i=0;
	for(i=0;i<10;i++)
	if(a[i]==0)
	break;
	if(i<10)
	return 0;
	else
	return 1;
}
