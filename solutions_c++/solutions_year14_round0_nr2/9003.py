#include<iostream>
#include <iomanip>
#include <stdio.h>
using namespace std;

int main()
{
	int T;
    long double C,F,X,ind,S,arf,tar;


	freopen("B-large.in","rt",stdin);

	freopen("output.in","wt",stdout);

	cin>>T;

	for(int i= 1;i<=T;i++)
	{
		cin>>C>>F>>X;
		ind=2.0;

		tar=0.0 ;
		S=X/ind;
		while(1)
    {
		    arf=tar+(X/(ind+F))+(C/ind);
			if ((S-arf)<0)
          		break;
			 else
        {
		          S=arf;
		          tar+=C/ind;
		          ind+=F;

            }
        }
		cout << fixed;
	    cout <<"Case #"<<setprecision(7)<<i<<": "<<S<<endl;
	 }
	return 0;
}
