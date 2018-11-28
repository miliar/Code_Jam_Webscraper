// prob1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <queue>
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

enum winner
{
	eRichard,
	eGabriel
};



int _tmain(int argc, _TCHAR* argv[])
{
    freopen("input.txt","r",stdin); freopen("A-out.txt","w",stdout);
    int N;
	 int X, R, C;
	winner win;
    scanf("%d", &N);
 //   cout << "Total = " << N << endl;
    for(int n=1; n<=N; n++)
    {
        scanf("%d %d %d", &X, &R, &C);
		win = eRichard;
		if((X == 1) && (R!=0) && (C!=0))
		{
			win = eGabriel;
		}
		else if((X == 2) && ((R*C)%X == 0))
		{
			win = eGabriel;
		}
		else if((X == 3) && ((R*C)%X == 0))
		{
			if((R==1)||(C==1))
			{
				win = eRichard;
			}
			else
			{
				win = eGabriel;
			}
		}
		else if((X >=4) && (X<7) && ((R*C)%X == 0))
		{
			 int new_temp = X -1;
			if( ( (R-new_temp) >= 1 && (C > 1) ) || ( (C-new_temp) >= 1 && (R > 1) ) )
			{
				//win = eGabriel;
				 int nr, nc;
				if(X%2==0)
				{
					nr = X/2;
					nc = nr+1;
				}
				else
				{
					nc = nr = X/2 + 1;
				} 
				if( ( (R-nr) >= 1 && ((C-nc) >= 1) ) || ( (C-nr) >= 1 && ((R-nc) >= 1) ) )
				{
					win = eGabriel;
				}
			}
		}
		else
		{
			win = eRichard;
		}

		if(win == eGabriel)
		{
			cout <<"Case #" << n << ": GABRIEL" << endl;
		}
		else
		{
			cout <<"Case #" << n << ": RICHARD" << endl;
		}
//		cout << "X = " << X << " , R = " << R << " , C = " << C << endl;
    }
	return 0;
}


