#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,j;
	freopen("A-large (1).in","r",stdin);
	freopen("A-large-practice(1).out","w",stdout);
	cin>>t;
	char z[26]={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
	for(j=1;j<=t;j++){
		int n,i,b=0,c;
		cin>>n;
		int a[n];
		for(i=0;i<n;i++)
		{
			cin>>a[i];
		}
		if(n==2){
			cout<<"Case #"<<j<<": ";
			while(a[0]--){
				cout<<"AB"<<" ";
			}
			cout<<endl;
		}
		else if(n%2!=0){
			cout<<"Case #"<<j<<": ";
			while(b!=1){
				b=0;
			for(i=0;i<n;i++){
				if(a[i]>b){
					b=a[i];
					c=i;
				}
			}
			
			if(b==1){
				cout<<z[0]<<" ";
				for(i=1;i<n;i=i+2){
					cout<<z[i]<<z[i+1]<<" ";
				}
			}
			else{
				a[c]--;
				cout<<z[c]<<" ";	
			}
			
		}
		cout<<endl;}
		else if(n%2==0){
			cout<<"Case #"<<j<<": ";
			while(b!=1){
				b=0;
			for(i=0;i<n;i++){
				if(a[i]>b){
					b=a[i];
					c=i;
				}
			}
			
			if(b==1){
				for(i=0;i<n;i=i+2){
					cout<<z[i]<<z[i+1]<<" ";
				}
			}
			else{
				a[c]--;
				cout<<z[c]<<" ";	
			}
			
		}
		cout<<endl;}
	}
}
