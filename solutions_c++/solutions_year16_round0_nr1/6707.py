
#include <stdio.h>
#include <string>
#include <map>
#include <iostream>
#include <stdlib.h>
#include <algorithm>
using namespace std;
const int A = 12005;
int i, k, n,t, m, l,j,p,v;
int arr[11];
char uy[20001];
long long res;
int main() {
	freopen("P2.txt", "r", stdin);
	freopen("A.1 codejam.txt", "w", stdout);
	scanf("%d", &t);
	for (k = 1; k <= t; k++)
	{
		scanf("%d", &i);
		if (i == 0)
		{
			printf("Case #%d: %s\n", k, "INSOMNIA");
		}
		for (j = 1; j < 100; j++) {
			_itoa(i*j, uy, 10);
			p = strlen(uy);
			for (n = 0; n < p; n++)
				arr[uy[n] - '0']=1;
			for (m= 0; m< 10; m++)
					l+=arr[m];
			if (l == 10) {
				printf("Case #%d: %d\n",k,i*j);
				j = 105;
			}
			l = 0;
		}
		for (m = 0; m < 10; m++)
			arr[m] = 0;
	}
}