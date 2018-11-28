#include<iostream>
using namespace std;
int v[14];
int main(){
	int t;
	cin>>t;
	long long int n;
	for(int i=1;i<=t;i++){
		cin>>n;long long int q=n;int l=0;long long int k=1;
		for(int j=0;j<=10;j++)v[j]=0;
		if(n==0)cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		else{
		long long int h;
		while(l!=10){h=q;
			while(q!=0){int x=q%10;if(v[x]==0){v[x]=1;l++;}
			q=q/10;}
			k++;q=k*n;}
			
				cout<<"Case #"<<i<<": "<<h<<endl;
		}
		
		
			}
		}
		

