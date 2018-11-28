#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <memory>

using namespace std;

bool minus;
char multiply(char x, char y)
{
	minus = false;
	if(x == '1') return y;
	if(x == 'i')
	{
		if(y == '1') 
		{
			return 'i';
		}
		if(y == 'i') 
		{
			minus = true;
			return '1';
		}
		if(y == 'j') 
		{
			return 'k';
		}
		if(y == 'k') 
		{
			minus = true;
			return 'j';
		}
	}
	if(x == 'j')
	{
		if(y == '1') 
		{
			return 'j';
		}
		if(y == 'i') 
		{
			minus = true;
			return 'k';
		}
		if(y == 'j') 
		{
			minus = true;
			return '1';
		}
		if(y == 'k') 
		{
			return 'i';
		}
	}
	if(x == 'k')
	{
		if(y == '1') 
		{
			return 'k';
		}
		if(y == 'i') 
		{
			return 'j';
		}
		if(y == 'j') 
		{
			minus = true;
			return 'i';
		}
		if(y == 'k') 
		{
			minus = true;
			return '1';
		}
	}
}


int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	
	
	int T;
	char str[10005];
	scanf("%d",&T);
	for(int t = 1; t<=T; t++)
	{
		int X,L;
		scanf("%d %d",&X,&L);
		scanf("%s",&str);
		int j = 0;
		char res = '1';
		bool neg = false;
		int search = 1;
		while(j<L)
		{
			for(int i = 0; i<X; i++)
			{
				res = multiply(res, str[i]);
				if((neg && !minus) || (!neg && minus))
				{
					neg = true;
				}
				else 
				{
					neg = false;
				}
				if(!neg && search < 3)
				{
					if(search == 1 && res == 'i')
					{
						search = 2;
						res = '1';
						neg = false;
					}
					else if(search == 2 && res == 'j')
					{
						search = 3;
						res = '1';
						neg = false;
					}
				}
			}
			j++;
		}


		if(search == 3 && res == 'k' && !neg)
			printf("Case #%d: YES\n",t);
		else 
			printf("Case #%d: No\n",t);
	}
}
