#include<iostream.h>
#include<stdio.h>
#include <iomanip.h>
void main()
{
	int t;
	freopen("ppp.in","r",stdin);
	freopen("res.txt","w",stdout);
	cin>>t;
	for(int p=1;p<=t;p++){
	double c,f,x,t1=0.0000000,t2=0.0000000;
	cin>>c>>f>>x;
	double rate=2.0000000;
	double s=0.0000000;
	while(1){
	    t1=s+x/rate;
	    s+=(c/rate);
	    rate+=f;
	    t2=s+(x/rate);
	    if(t1<=t2)
		break;
	}

	cout<<"Case #"<<p<<": "<<t1;
	cout<<endl;
       }
}
