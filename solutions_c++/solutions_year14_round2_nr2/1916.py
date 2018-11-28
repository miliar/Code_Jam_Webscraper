#include<stdio.h>
#include<iostream>
using namespace std;
int main(){
freopen ("c.in","r",stdin);
freopen ("cout.txt","w",stdout);
 int T,c=1;
 cin>>T;
 while(T--){

		int a,b,k;
		long long count=0;
		cin>>a>>b>>k;
		for(int i=0;i<a;i++)
		{
			for(int j=0;j<b;j++)
			if((i&j)<k) count++;
		}
		cout<<"Case #"<<c++<<": "<<count << endl;
	}
}
