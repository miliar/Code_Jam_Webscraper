#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <string.h>
#include <vector>

//#include <bits/stdc++.h>

using namespace std;

#define gab printf("GABRIEL\n")
#define rich printf("RICHARD\n")

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("output4.txt", "w", stdout);
	
	int T;
	scanf("%d", &T);
	
	for(int test=1; test<=T; test++)
	{
		printf("Case #%d: ", test);
		
		int X, R, C;
		scanf("%d %d %d", &X, &R, &C);
		
		if(X==1)
		{
			gab;
		}
		else if(X==2)
		{
			if(R%2==0 || C%2==0)
				gab;
			else
				rich;
		}
		else if(X==3)
		{
			if(R==1 || C==1)
				rich;
			else
			{
				if(R%3==0 || C%3==0)
					gab;
				else
					rich;
			}
		}
		else
		{
			if((R==3 && C==4) || (R==4 && C==3) || (R==4 && C==4))
				gab;
			else
				rich;
		}
	}
	
	fclose(stdin);
	fclose(stdout);
	
	return 0;
}
