#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<fstream>
using namespace std;
int t, Smax;
char a[1007];
void inmake()
{ scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{ scanf("%d %s", &Smax, &a);
		int current = a[0] - '0', ans = 0;
		for (int j = 1; j < Smax + 1; j++)
		{ if (current >= j) current += (a[j] - '0');
			else
			{ ans += (j - current);
				current += (j - current) + (a[j] - '0');
			 }
		 }
		
		printf("Case #%d: %d\n", i + 1, ans);
	 }
}

int main()
{ 
	freopen("stov.out", "w", stdout);
	inmake();
	
	return 0;
}

