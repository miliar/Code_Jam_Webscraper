#include<iostream>
#include <string>
#include <cstdio>
using namespace std;

int main()
{
	
	freopen("inputl.in","r",stdin);
    freopen("output.txt","w",stdout);

	float T, R,C,W, cheat;
	int ch;
	cin>> T;

	for ( int i = 1; i<= T; i++)
	{
		cin>> R>>C>>W;
		if( W==1) cout<<"Case #"<<i<<": "<<(R*C)<<endl;
		else if(C==W ) cout<<"Case #"<<i<<": "<<(R-1)+C<<endl;
		else {
			cheat = C/W;
			ch = cheat;
			if (cheat-ch == 0)
				cout<<"Case #"<<i<<": "<<W+(ch-1)+(ch *(R-1))<<endl;
			else 
				cout<<"Case #"<<i<<": "<<W+ (ch*R)<<endl;

		}
	}


	
	return 0;
}