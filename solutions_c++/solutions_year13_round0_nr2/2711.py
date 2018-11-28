#include<stdio.h>
int t[100][100];
int main()
{
    int zes;scanf("%d",&zes);
    for (int z=0;z<zes;z++)
    {
	int ma = -1;
	int n,m;scanf("%d%d",&n,&m);
	for (int i =0;i<n;i++)
	    for (int j=0;j<m;j++)
	    {
		scanf("%d",&t[i][j]);
		if(t[i][j]>ma) ma=t[i][j];
	    }
	bool res=1;
	for (int i=0;i<n;i++)
	    for (int j=0;j<m;j++)
	    {
		if(t[i][j]==ma) continue;
		bool ok =1;
		for (int k=0;k<n;k++)
		    if(t[k][j] != t[i][j]) { ok = 0 ;break;}
		if(ok) { continue;}
		ok=1;
		for (int k=0;k<m;k++)
		    if(t[i][k]!=t[i][j]) { ok = 0; break;}
		if(!ok){res=0;break;}
	    }
	if(res)
	    printf("Case #%d: YES\n",z+1);
	else
	    printf("Case #%d: NO\n",z+1);




    }
}
