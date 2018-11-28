#include<stdio.h>
#include<string>
#include<string.h>
#include<map>
#include<vector>
#include<math.h>
#include<stdlib.h>
#include<algorithm>
#include<iostream>
using namespace std;
int main()
{
	char a[10][10];
	freopen ("A-large (1).in","r",stdin);
	freopen ("output.txt","w",stdout);
	int i , j;
	int t;
	int counter=1;
	cin >> t;
	while(t--)
	{
		int z=0;
		for(i=0;i<4;i++)
				cin>>a[i];
		/*if (counter==29||counter==38||counter==39)
		{
		for(i=0;i<4;i++)
				cout << a[i]<< endl;
				cout << endl;
		}*/
		{
			for(i=0;i<4;i++)
			{
				if((a[i][0]=='X'||a[i][0]=='T')&&(a[i][1]=='X'||a[i][1]=='T')&&(a[i][2]=='X'||a[i][2]=='T')&&(a[i][3]=='X'||a[i][3]=='T'))
				{
					z=1;
					//if (counter==2) cout << "X - row " ;
					break;
				}
				else if((a[i][0]=='.'||a[i][1]=='.'||a[i][2]=='.'||a[i][3]=='.')&&z==0)
				{
					z=5;
				}
			}
		}
		{
			for(i=0;i<4;i++)
			{
				if((a[0][i]=='X'||a[0][i]=='T')&&(a[1][i]=='X'||a[1][i]=='T')&&(a[2][i]=='X'||a[2][i]=='T')&&(a[3][i]=='X'||a[3][i]=='T'))
				{
					z=1;
			//		if (counter==2) cout << "X - col " ;
					break;
				}
				else if((a[0][i]=='.'||a[1][i]=='.'||a[2][i]=='.'||a[3][i]=='.')&&z==0)
				{
					z=5;
				}
			}
		}
		{
			for(i=0;i<4;i++)
			{
				if((a[i][0]=='O'||a[i][0]=='T')&&(a[i][1]=='O'||a[i][1]=='T')&&(a[i][2]=='O'||a[i][2]=='T')&&(a[i][3]=='O'||a[i][3]=='T'))
				{
					z=2;
					break;
				}
				else if((a[i][0]=='.'||a[i][1]=='.'||a[i][2]=='.'||a[i][3]=='.')&&z==0)
				{
					z=5;
				}
			}
		}
		{
			for(i=0;i<4;i++)
			{
				if((a[0][i]=='O'||a[0][i]=='T')&&(a[1][i]=='O'||a[1][i]=='T')&&(a[2][i]=='O'||a[2][i]=='T')&&(a[3][i]=='O'||a[3][i]=='T'))
				{
						z=2;
						break;
				}
				else if((a[0][i]=='.'||a[1][i]=='.'||a[2][i]=='.'||a[3][i]=='.')&&z==0)
				{
					z=5;
				}
			}
		}
		{
			if((a[0][3]=='O'||a[0][3]=='T')&&(a[1][2]=='O'||a[1][2]=='T')&&(a[2][1]=='O'||a[2][1]=='T')&&(a[3][0]=='O'||a[3][0]=='T'))		
				z=2;
			else if((a[0][3]=='.'||a[1][2]=='.'||a[2][1]=='.'||a[3][0]=='.')&&z==0)
				z=5;
		}
		{
			if((a[0][3]=='X'||a[0][3]=='T')&&(a[1][2]=='X'||a[1][2]=='T')&&(a[2][1]=='X'||a[2][1]=='T')&&(a[3][0]=='X'||a[3][0]=='T'))
				z=1;
			else if((a[0][3]=='.'||a[1][2]=='.'||a[2][1]=='.'||a[3][0]=='.')&&z==0)
				z=5;
		}
		{
			if((a[0][0]=='O'||a[0][0]=='T')&&(a[1][1]=='O'||a[1][1]=='T')&&(a[2][2]=='O'||a[2][2]=='T')&&(a[3][3]=='O'||a[3][3]=='T'))
				z=2;
			else if((a[0][0]=='.'||a[1][1]=='.'||a[2][2]=='.'||a[3][3]=='.')&&z==0)
				z=5;
		}
		{
			if((a[0][0]=='X'||a[0][0]=='T')&&(a[1][1]=='X'||a[1][1]=='T')&&(a[2][2]=='X'||a[2][2]=='T')&&(a[3][3]=='X'||a[3][3]=='T'))
				z=1;
			else if((a[0][0]=='.'||a[1][1]=='.'||a[2][2]=='.'||a[3][3]=='.')&&z==0)
				z=5;
		}
		if(z==1)
			printf("Case #%d: X won\n",counter);
		else if(z==2)
			printf("Case #%d: O won\n",counter);
		else if(z==5)
			printf("Case #%d: Game has not completed\n",counter);
		else
			printf("Case #%d: Draw\n",counter);
		counter++;
	}
    return 0;
}
