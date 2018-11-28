#include<iostream>
using namespace std;
int main(){
	
	int t,r;
	cin>>t;
	for(r=1;r<=t;r++){
		int a,b,k;
		long long int c=0;
		cin>>a>>b>>k;
		for(int i=0;i<a;i++)
		{
			for(int j=0;j<b;j++)
			{
				if((i&j)<k)
				c++;
			}
		}
		cout<<"Case #"<<r<<": "<<c<<endl;
	}
	
			
		
}
