// Standing_ovation.cpp: главный файл проекта.

#include "stdafx.h"
#include <iostream>
#include <string>
using namespace std;


int solve (short n)
{
	int Smax, sum=0, razn=0, k=0;
	cin >> Smax;
	string 	a ;
	cin >> a;
	//sum=(a[0]-'0');
	for (int i=1; i<Smax+1; i++)
	{sum+=a[i-1]-'0';
	if ( (a[i]-'0')!=0 && i-sum>0) {razn=i-sum; sum+=razn; k+=razn;}
	}

	return k;
}

int main( )
{
//freopen("input.txt", "r", stdin); 
//freopen("A-small-attempt1.in", "r", stdin); 	
	freopen("A-large.in", "r", stdin); 
freopen("output.txt", "w", stdout);

short T, i;
cin >> T;

for (i=0; i<T; i++)
{
cout <<    "Case #" << i+1 << ": " <<  solve(i) << endl;
}

    return 0;
}
