/* ----Akash Agarwal---- */

#include<stdio.h>
#include<iostream>
#include<string.h>
#include<algorithm>
#include<stdlib.h>
#include<fstream>
#include<string>
#include<cmath>
#include <utility> 
#include <iomanip> 
#include <vector>
#include<stack>
#include<queue>
#include <sstream>


using namespace std;

#define LL long long int
#define iin(a) int a;cin >> a;
#define lin(a) LL a;cin >> a;
#define sin(a) string a;cin >> a;

#define myf(a,b,i) for(int i=a;i<b;i++)

#define mod 1000000007

int main()
{
	iin(t);
	for (int x = 0; x < t; ++x)
	{
		int r1,r2;
		int a[4][4],b[4][4];
		cin >> r1;
		myf(0,4,i)
			myf(0,4,j)
				cin >> a[i][j];
		cin >> r2;
		myf(0,4,i)
			myf(0,4,j)
				cin >> b[i][j];		

		int card,count=0;

		myf(0,4,i)
			myf(0,4,j)
			{
				if (a[r1-1][i]==b[r2-1][j])
				{
					//cout << a[r1-1][i] << " " << b[r2-1][j] << " " << i << " " << j << endl;
					count++;
					card=a[r1-1][i];
				}
			}

		if (count==0)
		{
			cout << "Case #" << x+1 << ": Volunteer cheated!" << endl;
		}
		else if (count>1)
		{
			cout << "Case #" << x+1 << ": Bad magician!" << endl;
		}
		else
		{
			cout << "Case #" << x+1 << ": " << card << endl;
		}

	}

	return 0;
}
