#include <stdio.h>
#include <vector>
#include <string>

using namespace std;

vector<vector<vector<string> > > ominos;

void init()
{
	ominos.resize(4);
	string mono = "*";
	ominos[0].resize(1);
	ominos[0][0].push_back(mono);

	// domino

	string domino = "**";
	ominos[1].resize(1);
	ominos[1][0].push_back(domino);
	domino = "*\n*";
	ominos[1][0].push_back(domino);

	// trominos

	string tromino = "***";
	ominos[2].resize(2);
	ominos[2][0].push_back(tromino);
	tromino = "*\n*\n*";
	ominos[2][0].push_back(tromino);

	tromino = "*\n**";
	ominos[2][1].push_back(tromino);
	tromino = "**\n*";
	ominos[2][1].push_back(tromino);
	tromino = ".*\n**";
	ominos[2][1].push_back(tromino);
	tromino = "**\n.*";
	ominos[2][1].push_back(tromino);

	// tetromino

	string tetromino = "****";
	ominos[3].resize(5);
	ominos[3][0].push_back(tetromino);
	tetromino = "*\n*\n*\n*";
	ominos[3][0].push_back(tetromino);
	
	tetromino = "**\n**";
	ominos[3][1].push_back(tetromino);
	
	tetromino = "*\n*\n**";
	ominos[3][2].push_back(tetromino);
	tetromino = "***\n*";
	ominos[3][2].push_back(tetromino);
	tetromino = "**\n.*\n.*";
	ominos[3][2].push_back(tetromino);
	tetromino = "..*\n***";
	ominos[3][2].push_back(tetromino);
	
	tetromino = ".*\n.*\n**";
	ominos[3][2].push_back(tetromino);
	tetromino = "*\n***";
	ominos[3][2].push_back(tetromino);
	tetromino = "**\n*\n*";
	ominos[3][2].push_back(tetromino);
	tetromino = "***\n..*";
	ominos[3][2].push_back(tetromino);

	tetromino = "*\n**\n.*";
	ominos[3][3].push_back(tetromino);
	tetromino = ".**\n**";
	ominos[3][3].push_back(tetromino);
	
	tetromino = ".*\n**\n*";
	ominos[3][3].push_back(tetromino);
	tetromino = "**\n.**";
	ominos[3][3].push_back(tetromino);
	
	tetromino = "***\n.*";
	ominos[3][4].push_back(tetromino);
	tetromino = ".*\n**\n.*";
	ominos[3][4].push_back(tetromino);
	tetromino = ".*\n***";
	ominos[3][4].push_back(tetromino);
	tetromino = "*\n**\n*";
	ominos[3][4].push_back(tetromino);
}


char mymap[5][5];
int X,R,C,T,Tcnt=0;
bool isfinished;

bool checkfinished()
{
	for(int i=0;i<R;i++)
	{
		for(int j=0;j<C;j++)
		{
			if(mymap[i][j] != '*')
			{
				return false;
			}
		}
	}
	return true;
}

void setPuzzle(int y,int x,int p,int k,bool set)
{
	//load
	int cy = y,cx = x;
	int cp = 0;
	string fragment = ominos[X-1][k][p];
	//printf("Loaded\n%s\n\n",fragment.c_str());
	
	if(fragment[0] == '.')
	{
		cx--;
		x = cx;
	}else if(fragment[0] == '.' && fragment[1] == '.')
	{
		cx-=2;
		x = cx;
	}

	for(int i=0;i<fragment.length();i++)
	{
		char ch = fragment[i];

		switch(ch)
		{
		case '.':
			cx++;
			break;
		case '*':
			if(set)
			{
				mymap[cy][cx] = '*';
			}
			else
			{
				mymap[cy][cx] = '.';
			}
			cx++;
			break;
		case '\n':
			cx = x;
			cy++;
			break;
		}
	}

	/*if(set)
	{
		puts("set");
	}
	else
	{
		puts("unset");
	}
	for(int i=0;i<R;i++)
	{
		puts(mymap[i]);
	}*/
}

bool checkcanset(int y,int x,int p,int k)
{
	// load
	int cy = y,cx = x;
	string fragment = ominos[X-1][k][p];
	//printf("Check\n%s\n\n",fragment.c_str());
	int cp = 0;
	
	if(fragment[0] == '.')
	{
		cx--;
		x = cx;
	}else if(fragment[0] == '.' && fragment[1] == '.')
	{
		cx-=2;
		x = cx;
	}

	for(int i=0;i<fragment.length();i++)
	{
		char ch = fragment[i];

		switch(ch)
		{
		case '.':
			cx++;
			break;
		case '*':
			if((0<= cx&&cx < C) && (0<= cy&&cy < R))
			{
				if(mymap[cy][cx] != '.')
				{
					return false;
				}
				cx++;
			}
			else
			{
				return false;
			}
			break;
		case '\n':
			cx = x;
			cy++;
			break;
		}
	}

	return true;
}

void doPuzzle()
{
	if(isfinished)
	{
		return;
	}
	if(checkfinished() && Tcnt > 0)
	{
		isfinished = true;
		return;
	}
	//calc left-top blank
	int y = -1,x;
	for(int i=0;i<R;i++)
	{
		for(int j=0;j<C;j++)
		{
			if(mymap[i][j] == '.')
			{
				y = i;
				x = j;
				break;
			}
		}
		if(y != -1)
		{
			break;
		}
	}
	if( y == -1)
	{
		return;
	}
	for(int i=0;i<ominos[X-1].size();i++)
	{
		for(int j=0;j<ominos[X-1][i].size();j++)
		{
			if(checkcanset(y,x,j,i))
			{
				setPuzzle(y,x,j,i,true);
				if(i == T)
				{
					Tcnt++;
				}
				doPuzzle();
				if(isfinished)
				{
					return;
				}
				setPuzzle(y,x,j,i,false);
				if(i == T)
				{
					Tcnt--;
				}
			}
		}
	}
}


int main()
{
	init();

	int t,c=1;
	scanf("%d",&t);
	while(t--)
	{
		int total = 1;
		scanf("%d%d%d",&X,&R,&C);

		for(int i=0;i<ominos[X-1].size();i++)
		{
			T = i;
			isfinished = false;
			Tcnt = 0;
			memset(mymap,0,5*5);
			for(int c=0;c<R;c++)
			{
				for(int j=0;j<C;j++)
				{
					mymap[c][j] = '.';
				}
			}

			doPuzzle();

			if(isfinished && Tcnt > 0)
			{
				total&=1;
			}
			else
			{
				total&=0;
			}
		}
		if(total)
		{
			printf("Case #%d: GABRIEL\n",c++);
		}
		else
		{
			printf("Case #%d: RICHARD\n",c++);
		}
	}	
	return 0;
}