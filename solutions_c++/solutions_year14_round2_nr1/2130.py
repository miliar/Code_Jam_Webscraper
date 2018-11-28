#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t,i,j,k,n, cnt;
	scanf("%d", &t);
	for(int ii = 1; ii<=t; ii++)
	{
		//char a[105], b[105];
		char *a = (char *)calloc(105, sizeof(char));
		char *b = (char *)calloc(105, sizeof(char));
		cnt = 0;int flag = 1;
		scanf("%d %s %s", &n, a, b);

		int *fa = (int *)calloc(105, sizeof(int));
		int *fb = (int *)calloc(105, sizeof(int));
		char ca, cb;
		char *na = (char *)calloc(105, sizeof(char));
		char *nb = (char *)calloc(105, sizeof(char));
		memset(na, '.', sizeof(char)*105);
		memset(nb, '.', sizeof(char)*105);

		ca = a[0]; cb = b[0];
		int cntr = 0, j=0;
		for(i=0; a[i]!='\0'; )
		{
			cntr = 0;
			while (a[i] == ca && a[i]!='\0')
			{
				cntr++;
				i++;
			}
			na[j] = ca;
			fa[j++] = cntr;
			ca = a[i];
		}


		cntr = 0; j=0;
		for(i=0; b[i]!='\0'; )
		{
			cntr = 0;
			while (b[i] == cb && b[i]!='\0')
			{
				cntr++;
				i++;
			}
			nb[j] = cb;
			fb[j++] = cntr;
			cb = b[i];
		}

		for(i=0; i<105; i++)
		{
			if(na[i] == nb[i])
				cnt += abs(fa[i] - fb[i]);
			else
			{
				flag = 0;
				break;
			}
		}
		if(!flag)
			printf("Case #%d: Fegla Won\n",ii);
		else
			printf("Case #%d: %d\n", ii, cnt);
		cnt=0;
		free(a);free(b);free(na);free(nb);free(fa);free(fb);
	}
	return 0;
}