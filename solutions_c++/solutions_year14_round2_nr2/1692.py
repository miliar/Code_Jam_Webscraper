#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<cstdlib>
using namespace std;

int main(){
	int t,a,b,k,ca=0,c=0,i,j;
	cin>>t;
	
	while(t--){
		c=0;
		cin>>a>>b>>k;
		ca++;
		for(i=0;i<a;i++){
			for(j=0;j<b;j++){
				if((i&j)<k)
					c++;
			}
		}
		cout<<"Case #"<<ca<<": "<<c<<endl;
	}
	
	return 0;
}
