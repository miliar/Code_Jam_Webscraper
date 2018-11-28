#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <string.h>
#include <vector>

//#include <bits/stdc++.h>

using namespace std;

char S[1005];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output12.txt", "w", stdout);
	
	int T;
	scanf("%d", &T);
	
	for(int test = 1; test<=T; test++)
	{
		printf("Case #%d: ", test);
		
		int Smax;
		scanf("%d %s", &Smax, S);
		
		int ans = 0, people = 0;
		
		for(int i=0; S[i]!='\0'; i++)
		{
			if(i>people)
			{
				ans+= i-people;
				people+= i-people;
			}
			
			people+= S[i]-'0';
		}
		
		printf("%d\n", ans);
	}
	
	fclose(stdin);
	fclose(stdout);
	
	return 0;
}
