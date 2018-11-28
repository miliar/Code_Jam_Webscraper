#include <iostream>
#include <iomanip.h>
#include <fstream.h>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <queue>
using namespace std;


int main()
{
	
 	ifstream f1("d:\\B-large.in");
 	ofstream f2("d:\\B-large.out");
 	int t,n,a;
 	double C,F,X,num,T;
	f1>>t;
	for (int i=1;i<=t;i++)
	{
		f2<<"Case #"<<i<<": "; 
		f1>>C>>F>>X;
		num=(F*X/C-2)/F;
		n=int (num+1E-10);
		if (n<0) n=0;
	//	cout<<n<<endl;
		T=X/(n*F+2);
		for (a=n-1;a>=0;a--)
		{
			T+=C/(a*F+2);
		}	
		f2 <<setprecision(7) <<fixed <<T<<endl;
	}
    return 0;
}
