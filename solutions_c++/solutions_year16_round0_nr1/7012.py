#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long t,n,i,j,k,r,p,q;
	int f,a[10];
	cin>>t;
	for(j=1;j<=t;j++){
		k=1;
		cin>>n;
		if(n==0){
			cout<<"Case #"<<j<<": INSOMNIA"<<endl;
		}
		else{
			for(i=0;i<10;i++){
				a[i]=0;
			}
			a:
			f=0;
			p=q=k*n;
			while(p){
				r=p%10;
				if(a[r]==0){
					a[r]=1;
				}
				p/=10;
			}
			for(i=0;i<10;i++){
				if(a[i]==0){
					f=1;
					break;
				}
			}
			if(f){
				k++;
				goto a;
			}
			else{
				cout<<"Case #"<<j<<": "<<q<<endl;
				continue;
			}
		}
		
	}
	return 0;
}
