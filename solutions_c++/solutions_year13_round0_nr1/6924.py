
#include <cstdlib>
#include <cstdio>
#include <string>
#include <iostream>
using namespace std;

//#define SMALL
#define LARGE
char s[4][4];



string solve() {
int xCount[10] = {0,0,0,0,0,0,0,0,0,0};
int oCount[10] = {0,0,0,0,0,0,0,0,0,0};		
	for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(s[i][j] == 'X')
				{
					xCount[i]+=1;
				}
				if(s[i][j] == 'O')
				{
					oCount[i]+=1;
				}
				if(s[i][j] == 'T')
				{
					oCount[i]+=1;
					xCount[i]+=1;
				}	
			}
		}
		for(int j=0;j<4;j++){
			for(int i=0;i<4;i++){
				if(s[i][j] == 'X')
				{
					xCount[j+4]+=1;
				}
				if(s[i][j] == 'O')
				{
					oCount[j+4]+=1;
				}
				if(s[i][j] == 'T')
				{
					oCount[j+4]+=1;
					xCount[j+4]+=1;
				}						
			}
		}
			for(int i=0;i<4;i++)
			{
				if(s[i][i] == 'O')
				{
					oCount[8] +=1;
				}
				if(s[i][i] == 'X')
				{
					xCount[8] +=1;
				}
				if(s[i][i] == 'T')
				{
					oCount[8] +=1;
					xCount[8] +=1;
				}				
				if(s[i][3-i] == 'O')
				{
					oCount[9] +=1;
				}
				if(s[i][3-i] == 'X')
				{
					xCount[9] +=1;
				}	
				if(s[i][3-i] == 'T')
				{
					oCount[9]+=1;
					xCount[9]+=1;
				}
			}
		
int xWin=0;
int oWin =0;
int final =0;
for(int i=0;i<10;i++)
{
	if(xCount[i] == 4)
	{
		xWin+=1;
	}
	if(oCount[i] == 4)
	{
		oWin+=1;
	}
}
if(xWin>0||oWin>0)
{
	if(xWin>oWin)
	{
		final =1;
	}else if(oWin>xWin)
	{
		final =2;
	}
}else{
	for(int i =0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			if(s[i][j] == '.')
			{
				final = 3;
			}
		}
	}
}
string result;
switch (final){
case 1:
	result = "X won";
	break;
case 2:
	result = "O won";
	break;
case 3:
	result = "Game has not completed";
	break;
case 0:
	result = "Draw";
	break;
default:
	result = "error";
	break;
}

return result;
}

int main() {
	freopen("A-sample.in", "rt", stdin);
	#ifdef SMALL
		freopen("A-small-attempt2.in", "rt", stdin);
		freopen("A-small-attempt2.out", "wt", stdout);
	#endif
	#ifdef LARGE
		freopen("A-large.in", "rt", stdin);
		freopen("A-large.out", "wt", stdout);
	#endif
	
	int T;					//The number of test cases	
	cin >> T;
	for (int i = 1; i <= T; i++) {
		for(int k =0;k<4;k++){	
			for(int j=0;j<4;j++)
			{
				cin>>s[k][j];
			}
		}
		cout << "Case #" << i << ": ";
		cout << solve();
		cout << endl;
	}	
	return 0;
}