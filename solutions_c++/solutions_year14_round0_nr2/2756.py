#include <stdlib.h>
#include <fstream>
#include <iostream>
#include <iomanip>
using namespace std;

int main ()
{
	ifstream R("B-large.in");
    ofstream W("B-large.out");
    
    int t;
    R>>t;
    int ans1, ans2, table1[5][5], table2[5][5];
    for (int ti=1;ti<=t;++ti)
    {
		double C,F,X;
		R>>C>>F>>X;
		double timethis = X/2.0;
		double timenext;
		double timepurchase=0;
		for(int i = 1;;i++)
		{
			timepurchase +=C/(2+(i-1)*F);
			timenext = timepurchase + X/(2+i*F);
			if(timenext > timethis )
				break;
			//cout<<timethis<<endl;
			//system("pause");
			timethis = timenext;
		}
    	

		W<<"Case #"<<ti<<": "<<fixed<<setprecision(7)<<timethis<<endl;
	}
}

