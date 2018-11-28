#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
using namespace std;
int main()
{
    freopen("cook.in","r",stdin);
    freopen("cookout.txt","w",stdout);
	int test,f,a=1,final;
	double C,F,X,sumC,sumX,rate,exsumX,exsumC; 
	cin>>test;
	while(test--)
	{
		cin>>C>>F>>X;
		final=1;
		exsumX=0.0;
		exsumC=0.0;
		rate=2.0;
		sumX=X/rate;
		sumC=C/rate;
		if(sumX<=sumC)
		{
		    
			cout<<"Case #"<<a<<": "<<fixed<<setprecision(7)<<sumX<<endl;
			a=a+1;
			}
		else
		{
			while(final!=0)
			{
				exsumX=sumX;
				exsumC=sumC;
				rate=rate+F;
				sumC=sumC+(C/rate);
				sumX=exsumC+(X/rate);
				if(exsumX<sumX)
				{
					cout<<"Case #"<<a<<": "<<fixed<<setprecision(7)<<exsumX<<endl;
					a=a+1;
					final=0;
					}
				}
			}
		}
	return 0;
}
