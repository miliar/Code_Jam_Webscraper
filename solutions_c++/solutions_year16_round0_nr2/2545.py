#include<bits/stdc++.h>
using namespace std;
char tab[1009];
int main()
{
	int n;
	scanf("%d", &n);
	for(int tt=1; tt<=n; tt++)
	{
		scanf("%s", tab);
		int m=0;
		while(tab[m]!=0)
			m++;
		tab[m]='+';
		int wyn=0;
		for(int i=0; i<m; i++)
			if(tab[i]!=tab[i+1])
				wyn++;
		printf("Case #%d: %d\n", tt, wyn);
	}


}
