#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#define LL long long int
using namespace std;
int main()
{
	int tc,i,j,k,l;
	scanf("%d",&tc);
	char str[4][5];
	int X,O,inc,a,b,t;
	l=1;	
	while(l<=tc)
	{
		for(i=0;i<4;i++)
			scanf("%s",str[i]);
		X=O=inc=0;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
			{
				if(str[i][j]=='.')
					inc=1;
				// first diagonal
				if(i+3<4 && j+3<4)
				{
					a=b=t=0;
					for(k=0;k<4;k++)
					{
						if(str[i+k][j+k]=='X')
							a++;
						else
						if(str[i+k][j+k]=='O')
							b++;
						else
						if(str[i+k][j+k]=='T')
							t++;						
					}
					if(a==3 && t==1)
						X=1;
					else
					if(b==3 && t==1)
						O=1;
					else
					if(a==4)
						X=1;
					else
					if(b==4)
						O=1;				
					
				}
				// second diagonal
				if(i-3>=0 && j+3<4)
				{
					a=b=t=0;
					for(k=0;k<3;k++)
					{
						if(str[i-k][j+k]=='X')
							a++;
						else
						if(str[i-k][j+k]=='O')
							b++;
						else
						if(str[i-k][j+k]=='T')
							t++;						
					}
					if(a==3 && t==1)
						X=1;
					else
					if(b==3 && t==1)
						O=1;
					else
					if(a==4)
						X=1;
					else
					if(b==4)
						O=1;				
					
				}
				// third diagonal
				if(i+3<4 && j-3>=0)
				{
					a=b=t=0;
					for(k=0;k<4;k++)
					{
						if(str[i+k][j-k]=='X')
							a++;
						else
						if(str[i+k][j-k]=='O')
							b++;
						else
						if(str[i+k][j-k]=='T')
							t++;						
					}
					if(a==3 && t==1)
						X=1;
					else
					if(b==3 && t==1)
						O=1;
					else
					if(a==4)
						X=1;
					else
					if(b==4)
						O=1;				
					
				}
				// fourth diagonal
				if(i-3>=0 && j-3>=0)
				{
					a=b=t=0;
					for(k=0;k<4;k++)
					{
						if(str[i-k][j-k]=='X')
							a++;
						else
						if(str[i-k][j-k]=='O')
							b++;
						else
						if(str[i-k][j-k]=='T')
							t++;						
					}
					if(a==3 && t==1)
						X=1;
					else
					if(b==3 && t==1)
						O=1;
					else
					if(a==4)
						X=1;
					else
					if(b==4)
						O=1;				
					
				}
				// right
				if(j+3<4)
				{
					a=b=t=0;
					for(k=0;k<4;k++)
					{
						if(str[i][j+k]=='X')
							a++;
						else
						if(str[i][j+k]=='O')
							b++;
						else
						if(str[i][j+k]=='T')
							t++;						
					}
					if(a==3 && t==1)
						X=1;
					else
					if(b==3 && t==1)
						O=1;
					else
					if(a==4)
						X=1;
					else
					if(b==4)
						O=1;				
					
				}
				//down
				if(i+3<4)
				{
					a=b=t=0;
					for(k=0;k<4;k++)
					{
						if(str[i+k][j]=='X')
							a++;
						else
						if(str[i+k][j]=='O')
							b++;
						else
						if(str[i+k][j]=='T')
							t++;						
					}
					if(a==3 && t==1)
						X=1;
					else
					if(b==3 && t==1)
						O=1;
					else
					if(a==4)
						X=1;
					else
					if(b==4)
						O=1;				
					
				}
				// left
				if(j-3>=0)
				{
					a=b=t=0;
					for(k=0;k<4;k++)
					{
						if(str[i][j-k]=='X')
							a++;
						else
						if(str[i][j-k]=='O')
							b++;
						else
						if(str[i][j-k]=='T')
							t++;						
					}
					if(a==3 && t==1)
						X=1;
					else
					if(b==3 && t==1)
						O=1;
					else
					if(a==4)
						X=1;
					else
					if(b==4)
						O=1;				
					
				}
				//up
				if(i-3>=0)
				{
					a=b=t=0;
					for(k=0;k<4;k++)
					{
						if(str[i-k][j]=='X')
							a++;
						else
						if(str[i-k][j]=='O')
							b++;
						else
						if(str[i-k][j]=='T')
							t++;						
					}
					if(a==3 && t==1)
						X=1;
					else
					if(b==3 && t==1)
						O=1;
					else
					if(a==4)
						X=1;
					else
					if(b==4)
						O=1;				
					
				}
			}
		printf("Case #%d: ",l);
		if(X==1 && O==0)
			printf("X won\n");
		else
		if(X==0 && O==1)
			printf("O won\n");
		else
		if(X==0 && O==0 && inc==0)
			printf("Draw\n");
		else
		if(X==0 && O==0 && inc==1)
			printf("Game has not completed\n");
		l++;	
	}
	return 0;
}
