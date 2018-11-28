#include<iostream>
using namespace std;

char grid [4][5];

int checkstat ()
{
	int x, y, endgame=0; char check='-';
	for ( x=0; x<4; x++ )
	{
		//cout<<"Entered loop "<<x<<endl;
		check='-';
		int linecheck=0, win=0;
		for ( y=0; y<4; y++ )
		{
			//cout<<"Entered inner loop "<<y<<endl;
			if ( grid[x][y]=='.' )
			{
				endgame=1;
				linecheck=1;
				win=1;
				break;
			}
			if ( grid[x][y]=='T' ) continue;
			else
			{
				if ( check=='-' )
				{
					check=grid[x][y];
					continue;
				}
				else
				{
					if ( check==grid[x][y] ) continue;
					else win=1;
				}
			}
		}

		if ( win==0 )
		{
			//cout<<"Win detected "<<check;
			if ( check=='X' ) return 0;
			else return 1;
		}
	}
	
	for ( y=0; y<4; y++ )
	{
		check='-';
		int linecheck=0, win=0;
		for ( x=0; x<4; x++ )
		{
			if ( grid[x][y]=='.' )
			{
				linecheck=1;
				break;
			}
			if ( grid[x][y]=='T' ) continue;
			else
			{
				if ( check=='-' )
				{
					check=grid[x][y];
					continue;
				}
				else
				{
					if ( check==grid[x][y] ) continue;
					else { win=1; break; }
				}
			}
		}
		if ( linecheck==1 ) continue;
		if ( win==0 )
		{
			if ( check=='X' ) return 0;
			else return 1;
		}
	}

	check='-';
	for ( x=0; x<4; x++ )
	{
		if ( grid[x][x]=='.' ) break;
		if ( grid[x][x]=='T' ) continue;
		else
		{
			if ( check=='-' )
			{
				check=grid[x][x];
				continue;
			}
			else
			{
				if ( grid[x][x]==check ) continue;
				else break;
			}
		}
	}
	if ( x==4 )
	{
		if ( check=='X' ) return 0;
		else return 1;
	}
	check='-';
	for ( x=0; x<4; x++ )
	{
		y=3-x;
		if ( grid[x][y]=='.' ) break;
		if ( grid[x][y]=='T' ) continue;
		else
		{
			if ( check=='-' )
			{
				check=grid[x][y];
				continue;
			}
			else
			{
				if ( grid[x][y]==check ) continue;
				else break;
			}
		}
	}
	if ( x==4 )
	{
		if ( check=='X' ) return 0;
		else return 1;
	}
	
	if ( endgame==0 ) return 2;
	return 3;
}



int main()
{
	int testcases, i, j, k, sol[1000];
	cin>>testcases;
	int t=testcases;
	while ( testcases -- )
	{
		for ( i=0; i<4; i++ ) cin>>grid[i];
		
		cout<<endl;
		sol[testcases]=checkstat();
	
	}
	int tee=t;
	t--;
	for ( i=1; i<=tee; i++, t-- )
	{
		switch ( sol[t] )
		{
			case 0	:	cout<<"Case #"<<i<<": X won"<<endl; break;
			case 1	:	cout<<"Case #"<<i<<": O won"<<endl; break;
			case 2	:	cout<<"Case #"<<i<<": Draw"<<endl; break;
			case 3	:	cout<<"Case #"<<i<<": Game has not completed"<<endl; break;
		}
	}

	return 0;
}

