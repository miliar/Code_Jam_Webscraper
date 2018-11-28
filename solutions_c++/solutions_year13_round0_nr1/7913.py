#include<iostream>
//#include<conio.h>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#define mod 1000000007

using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int tc,t,i,j,c,x,y;
	char b[4][4];
    scanf("%d", &t);

	for(tc=1;tc<=t;++tc)
	{
		c=0;
		for(i=0;i<4;i++)
		{
				scanf("%s", &b[i]);
				for(j=0;j<3;++j)
				{
					if(b[i][j]=='.')
						++c;
                }
		}

		for(i=0;i<4;++i)
		{
			x=y=0;
			for(j=0;j<4;++j)
			{
				if(b[i][j]=='X' || b[i][j]=='T')
					++x;
				if(b[i][j]=='O' || b[i][j]=='T')
					++y;
			}
			if(x==4)
			{
				printf("Case #%d: X won\n",tc);
				goto q;
			}
			else if(y==4)
			{
				printf("Case #%d: O won\n",tc);
				goto q;
			}
		}

		for(i=0;i<4;++i)
		{
			x=y=0;
			for(j=0;j<4;++j)
			{
				if(b[j][i]=='X' || b[j][i]=='T')
					++x;
				if(b[j][i]=='O' || b[j][i]=='T')
					++y;
			}
			if(x==4)
			{
				printf("Case #%d: X won\n",tc);
				goto q;
			}
			else if(y==4)
			{
				printf("Case #%d: O won\n",tc);
				goto q;
			}
		}

		x=y=0;
		for(i=0;i<4;++i)
		{
			if(b[i][i]=='X' || b[i][i]=='T')
					++x;
			if(b[i][i]=='O' || b[i][i]=='T')
					++y;
		}
		if(x==4)
			{
				printf("Case #%d: X won\n",tc);
				goto q;
			}
		else if(y==4)
			{
				printf("Case #%d: O won\n",tc);
				goto q;
			}

		x=y=0;
		for(i=0;i<4;++i)
		{
			if(b[i][3-i]=='X' || b[i][3-i]=='T')
					++x;
			if(b[i][3-i]=='O' || b[i][3-i]=='T')
					++y;
		}
		if(x==4)
			{
				printf("Case #%d: X won\n",tc);
				goto q;
			}
		else if(y==4)
			{
				printf("Case #%d: O won\n",tc);
				goto q;
			}


		if(c==0)
		printf("Case #%d: Draw\n",tc);
		else
			printf("Case #%d: Game has not completed\n",tc);
q: ;		
    }
	
//getch();
return 0;

}


