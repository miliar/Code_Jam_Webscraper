/*
 * qualA.cpp
 *
 *  Created on: 2014-04-12
 *      Author: aabdelsa
 */

#include <iostream>
#include <string>
#include <cmath>
#include <cstdio>
#include <iomanip>

using namespace std;

int g1 [4][4];
int g2 [4][4];

int f;
int inter (int r1, int r2)
{
	int res = 0;
	for ( int i = 0 ; i < 4 ; i ++)
		for ( int j = 0; j < 4 ; j ++)
			if ( g1[r1][i] == g2[r2][j])
			{
				f = g1[r1][i];
				res ++;
			}
	return res;
}




int main ()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("a.out","w",stdout);

	int cases;
	cin >> cases;

	for ( int t = 1; t<=cases; t++)
	{
		int r1,r2;
		cin >> r1;
		for ( int i = 0 ; i < 4 ; i ++)
			for ( int j = 0; j < 4 ; j ++)
				cin >> g1[i][j];

		cin >> r2;
		for ( int i = 0 ; i < 4 ; i ++)
			for ( int j = 0; j < 4 ; j ++)
				cin >> g2[i][j];

		cout << "Case #" <<t<<": ";

		int res = inter(r1-1,r2-1);

		if ( res == 0)
			cout << "Volunteer cheated!"<<endl;
		if ( res == 1 )
			cout <<f<<endl;
		if ( res > 1)
			cout <<"Bad magician!" << endl;
	}
	return 0;
}
