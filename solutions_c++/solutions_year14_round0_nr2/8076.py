#include <iostream>
#include<iomanip>
using namespace std;

int main() {
	// your code goes here
	int t;
	double c,f,x,T,r,balance,w,f1;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		T=0;
		r=2;
		balance=0;
		cin>>c>>f>>x;
		if(x<=c)
		{
			T=x/r;
			cout<<"Case #"<<k<<": "<<fixed<<setprecision(7)<<T<<endl;
		}
		else
		{
				w=x/r;
					f1=c/r;
				while(1)
				{
					r=r+f;
					if(f1+x/r>w)
					{
						break;
					}
					T+=f1;
					f1=c/r;
					w=x/r;
				}
				T+=w;
				cout<<"Case #"<<k<<": "<<fixed<<setprecision(7)<<T<<endl;
			
		}
	}
	return 0;
}