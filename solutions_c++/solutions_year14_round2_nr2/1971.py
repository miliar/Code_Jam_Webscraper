#include <bits/stdc++.h>
using namespace std;
int db[1000][1000] = {0};
int main()
{
	int t,i,j,k,a,b,cnt;
	for(i=0; i<1000; i++)
		for(j=0; j<1000; j++)
			db[i][j] = i&j;

	scanf("%d", &t);
	for(int ii=1; ii<=t; ii++)
	{
		scanf("%d %d %d", &a, &b, &k);
		cnt = 0;
		for(i=0; i<a; i++)
			for(j=0; j<b; j++)
				if(db[i][j] < k)
					cnt++;

		printf("Case #%d: %d\n",ii, cnt);
	}
	return 0;
}