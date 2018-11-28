#include<bits/stdc++.h>
using namespace std;
#define ll long long int
main(){
	ll a,b,c,d,t,i,j,x,n;
	  cin>>t;
	for (i = 1; i <=t; ++i)
	{
		cin>>n;
		if(n==0){
        cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		}
		else{
			set < ll >  s1;
              x=1;
		while(s1.size()<10){
			d=n*x;
			c=d;
			while(c){
				s1.insert(c%10);
				c=c/10;
			}
			x++;
		}
		
		cout<<"Case #"<<i<<": "<<d<<endl;
		}
		
	}

}