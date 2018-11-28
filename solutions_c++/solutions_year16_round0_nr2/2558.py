#include<bits/stdc++.h>
using namespace std;
#define ll long long int
main(){
	ll a,b,c,d,t,i,j,x,n;
	  cin>>t;
	for (i = 1; i <=t; ++i)
	{
		char A[110];
		cin>>A;
		n= strlen(A);
       c=0;
		for(j=n-1; j>=0; j--){
			  x=j;
			if(A[j]=='-'){
				c++;
              while(x>=0){
              	if(A[x]=='-'){
              		A[x]='+';
              	}
              	else{
              		A[x]='-';
              	}
              	x--;
              }
			}
		}
		
		cout<<"Case #"<<i<<": "<<c<<endl;
	}

}