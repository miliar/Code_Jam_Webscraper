/**
  * Author: phunshuk
  * Email: 2591kuldeep@gmail.com
*/
#include <cstdio>
#include <sstream>
#include <string>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cassert>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <cmath>
#include <utility>
#include <climits>

using namespace std ;

int main()
{
	int t=0,T;
	scanf("%d",&T);
	while(t<T)
	{
		int a[4][4],chk[2][4]; //chk : 0 rows and 1 cols
		for(int i=0;i<4;i++)
			chk[0][i]=chk[1][i]=0;
		int won=-1,flag=0,b[2]={-1,-1};
		char c;
		//scanf("%c",&c);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				scanf(" %c",&c);
				//printf("%c",c);
				if(c=='X')
					a[i][j]=1;
				else if(c=='O')
					a[i][j]=5;  // player 0
				else if(c=='.')
					a[i][j]=-1;
				else if(c=='T')
				{
					a[i][j]=0;
					b[0]=i;
					b[1]=j;
				}
				if(a[i][j]==-1)
				{
					chk[0][i]=chk[1][j]=-1;
					flag=1;
				}
				else 
				{
					if(chk[0][i]!=-1)
						chk[0][i]+=a[i][j];
					if(chk[1][j]!=-1)
						chk[1][j]+=a[i][j];
				}
				if(chk[0][i]==4 || chk[1][j]==4)
					won=1;
				else if(chk[0][i]==20 || chk[1][j]==20)
					won=0;
				
			}
		}
		//printf("won:- %d\n",won);
		int dig[2]={0,0};
		for(int i=0;i<4;i++)
		{
				if(a[i][i]>0 && dig[0]!=-1)
					dig[0]+=a[i][i];
				else if(a[i][i]==-1 && dig[0]!=-1)
					dig[0]=-1;
				
				if(a[i][3-i]>0 && dig[1]!=-1)
					dig[1]+=a[i][3-i];
				else if(a[i][3-i]==-1 && dig[1]!=-1)
					dig[1]=-1;
		}
		//cout<<"dig: "<<dig[0]<<endl;
		if(dig[0]==20||dig[1]==20)
			won=0;
		if(dig[1]==4||dig[0]==4)
			won=1;

		if(won==-1 && b[0]>=0)
		{
			//row
			if(chk[0][b[0]]==15)
				won=0;
			else if (chk[0][b[0]]==3)
				won=1;

			//col
			if(chk[1][b[1]]==15)
				won=0;
			else if (chk[1][b[1]]==3)
				won=1;
			//dig
			if(b[0]==b[1])
			{
				if(dig[0]==15)
					won=0;
				if(dig[0]==3)
					won=1;
			}
			if(b[1]==3-b[0])
			{
				if(dig[1]==15)
					won=0;
				if(dig[1]==3)
					won=1;
			}
		}
		printf("Case #%d: ",t+1);
		t++;
		if(flag==1&&won==-1)
			printf("Game has not completed");
		else if(won==-1)
			printf("Draw");
		else if(won==0)
			printf("O won");
		else
			printf("X won");
		printf("\n");
	}
	return 0;
}


