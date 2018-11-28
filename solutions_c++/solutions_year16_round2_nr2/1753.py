#include <iostream>
#include <string.h>
#include <math.h>
#include <stdlib.h>
using namespace std;

char a[2][20];
int minn,minc,minj,n;

void dfs(int typ, int loc)
{
	if(loc < 0)
	{
		if(!typ)
		{
			dfs(1,n-1);
			return;
		}
		int c = atoi(a[0]);
		int j = atoi(a[1]);
//			cout << c << " " << j << endl;
		int diff = c>j ? c-j : j-c;
		if(diff < minn)
		{
			minn = diff;
			minc = c;
			minj = j;
		}else if(diff == minn)
		{
			if(c < minc)
			{
				minc = c;
				minj = j;
			}
			else if(c == minc && j < minj)
				minj = j;
		}
		return;
	}
	
	if(a[typ][loc]!='?')
	{
		dfs(typ,loc-1);
		return;
	}

	for(int i=0 ; i<10 ; ++i)
	{
		a[typ][loc] = i+'0';
		dfs(typ,loc-1);
	}
	a[typ][loc] = '?';
}

int main() {
	int tc,tst;
	cin >> tst;

	for(tc=1 ; tc<=tst ; ++tc)
	{
		int i,j;

		cin >> a[0] >> a[1];
		
		for(n=0 ; a[0][n] ; ++n)	{}

		minn = minc = minj = 1000;
		dfs(0,n-1);

		for(i=n-1 ; i>=0 ; --i)
		{
			a[0][i] = (minc%10) + '0';	minc /= 10;
			a[1][i] = (minj%10) + '0';	minj /= 10;
		}

		cout << "Case #" << tc << ": " ;
		//cout << minc << " " << minj << " " << minn << " " << n << endl;
		cout << a[0] << " " << a[1] << endl;
	}
	return 0;
}
