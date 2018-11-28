#include <stdio.h>
#include <sstream>
#include <iostream>
#include <math.h>
#include <string>
#include <map>

using namespace std;

#define sf scanf
#define pf printf
#define fr(x,a,b) for( int x = a; x < b; ++x )
#define clr(x) memset(x,0,sizeof(x));


char g[5][5];

int Check(char x)
{
	fr(i,0,4)
	{
		int ok = 1;
		fr(j,0,4)
		{
			if(g[i][j] != x && g[i][j] != 'T')
			{
				ok = 0;
				break;
			}
		}
		if( ok == 1 )
			return 1;
		ok = 1;
		fr(j,0,4)
		{
			if(g[j][i] != x && g[j][i] != 'T')
			{
				ok = 0;
				break;
			}
		}
		if( ok == 1 )
			return 1;
		
	}
	

	int ok = 1;
	fr(i,0,4)
	{
		if(g[i][i] != x && g[i][i] != 'T')
		{
			ok = 0;
			break;
		}
	}
	if( ok == 1 )
		return 1;
	
	ok = 1;
	fr(i,0,4)
	{
		if(g[i][3-i] != x && g[i][3-i] != 'T')
		{
			ok = 0;
			break;
		}
	}
	if( ok == 1 )
		return 1;

	return 0;

}


int HasEmpty()
{
	fr(i,0,4)
		fr(j,0,4)
		if(g[i][j] == '.' )return 1;
	return 0;
}

int main()
{
	int T;
	sf("%d",&T);
	fr(ca,0,T)
	{
		gets(g[0]);
		fr(i,0,4)
		{
			gets(g[i]);
		}
		if(Check('X'))
		{
			pf("Case #%d: X won",ca+1);
		}
		else if( Check('O') )
		{
			pf("Case #%d: O won",ca+1);
		}
		else if( HasEmpty( ))
		{
			pf("Case #%d: Game has not completed",ca+1);
		}
		else 
		{
			pf("Case #%d: Draw",ca+1);
		}
		pf("\n");

	}
}
