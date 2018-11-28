
#include <stdio.h>
#include <string>
#include <map>
#include <iostream>
#include <stdlib.h>
#include <algorithm>
using namespace std;
const int A = 12005;
int i, k, n,t, m, l,j,p,v;
char uy[2001];
long long res;
int main() {
	freopen("B-small-attempt0.txt", "r", stdin);
	freopen("B codejam.txt", "w", stdout);
	scanf("%d", &t);
	for (v = 1; v <= t; v++)
	{
		scanf("%s",uy);
		l = strlen(uy);
		i = l - 1;
		while (i >= 0)
		{
			if (uy[i] == '+')
				i--;
			else
				break;
		}

		if (i == 0)
			p++;
		else if(i==-1)
			p = 0;
		else
		{
			for (j = i; j > 0; j--)
				if (uy[j] != uy[j - 1])
					p++;
			p++;
		}
		printf("Case #%d: %d\n",v, p);
		p = 0;
	}
}


/*

--+-
+++-
----
++++

*/