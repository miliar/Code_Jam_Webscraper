#include<bits/stdc++.h>
using namespace std;
//int array[100000][1000];
int main(){
	int t,i,j,z;
	long long int n,p,x;
	cin>>t;
	for(i=1;i<=t;i++){
		cin>>n;
		cout<<"Case #"<<i<<": ";
		if(n==0){
			cout<<"INSOMNIA"<<endl;
			
		}
		else
		{
			int a[10]={0};
			x=n;
			p=1;
			z=1;
			while(z==1){
				x=n*p;
				while(x){
					a[x%10]=1;
					x/=10;
				}
				z=0;
				for(j=0;j<10;j++){
					if(a[j]==0){
						z=1;
						break;
					}
					
				}
				if(z==1){
					p++;
				}
			}
			cout<<n*p<<endl;
		}
		n++;
	}
		
	
}
