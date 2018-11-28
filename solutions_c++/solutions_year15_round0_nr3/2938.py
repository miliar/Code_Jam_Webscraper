#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <string.h>
#include <vector>

//#include <bits/stdc++.h>

using namespace std;

#define swap_flaga flaga=(flaga==0?1:0)
#define swap_flagb flagb=(flagb==0?1:0)
#define swap_flagc flagc=(flagc==0?1:0)

int CoCk[10004];

char S[10004], A[10004];
char Z[5][5];

int main()
{
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("output3.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	
	for(int test=1; test<=T; test++)
	{
		printf("Case #%d: ", test);
		
		int L, X;
		scanf("%d %d %s", &L, &X, S);
		
		memset(CoCk, 0, sizeof(CoCk));
		
		int k = 0;
		
		for(int i=0; i<X; i++)
		{
			for(int j=0; S[j]!='\0'; j++)
			{
				A[k++] = S[j];
			}
		}
		
		A[k] = '\0';
		
		int a = 0, b, c, flaga = 0, flagb, flagc, yes = 0;
		
		c = flagc = 0;
						
		for(int l=k-1; l>=0; l--)
		{
			if(A[l]=='i')
			{
				if(c==1)
				{
					swap_flagc;
					c = 0;
				}
				else if(c==2)
					c = 3;
				else if(c==3)
				{
					swap_flagc;
					c = 2;
				}
				else
					c = 1;
			}
			else if(A[l]=='j')
			{
				if(c==1)
				{
					swap_flagc;
					c = 3;
				}
				else if(c==2)
				{
					swap_flagc;
					c = 0;
				}
				else if(c==3)
					c = 1;
				else
					c = 2;
			}
			else if(A[l]=='k')
			{
				if(c==1)
					c = 2;
				else if(c==2)
				{
					swap_flagc;
					c = 1;
				}
				else if(c==3)
				{
					swap_flagc;
					c = 0;
				}
				else
					c = 3;
			}
			
			if(flagc==0 && c==3)
				CoCk[l] = 1;
		}
		
		for(int i=0; i<k; i++)
		{
			if(A[i]=='i')
			{
				if(a==1)
				{
					swap_flaga;
					a = 0;
				}
				else if(a==2)
				{
					swap_flaga;
					a = 3;
				}
				else if(a==3)
					a = 2;
				else
					a = 1;
			}
			else if(A[i]=='j')
			{
				if(a==1)
					a = 3;
				else if(a==2)
				{
					swap_flaga;
					a = 0;
				}
				else if(a==3)
				{
					swap_flaga;
					a = 1;
				}
				else
					a = 2;
			}
			else if(A[i]=='k')
			{
				if(a==1)
				{
					swap_flaga;
					a = 2;
				}
				else if(a==2)
					a = 1;
				else if(a==3)
				{
					swap_flaga;
					a = 0;
				}
				else
					a = 3;
			}
			
			if(flaga==0 && a==1)
			{
				flagb = b = 0;
					
				for(int j=i+1; j<k; j++)
				{
					if(A[j]=='i')
					{
						if(b==1)
						{
							swap_flagb;
							b = 0;
						}
						else if(b==2)
						{
							swap_flagb;
							b = 3;
						}
						else if(b==3)
							b = 2;
						else
							b = 1;
					}
					else if(A[j]=='j')
					{
						if(b==1)
							b = 3;
						else if(b==2)
						{
							swap_flagb;
							b = 0;
						}
						else if(b==3)
						{
							swap_flagb;
							b = 1;
						}
						else
							b = 2;
					}
					else if(A[j]=='k')
					{
						if(b==1)
						{
							swap_flagb;
							b = 2;
						}
						else if(b==2)
							b = 1;
						else if(b==3)
						{
							swap_flagb;
							b = 0;
						}
						else
							b = 3;
					}
					
					if(flagb==0 && b==2)
					{
						if(CoCk[j+1])
						{
							yes = 1;
							break;
						}
					}
				}
				
				if(yes)
					break;
			}
			
			if(yes)
				break;
		}
		
		if(yes)
			printf("YES\n");
		else
			printf("NO\n");
	}
	
	fclose(stdin);
	fclose(stdout);
	
	return 0;
}
