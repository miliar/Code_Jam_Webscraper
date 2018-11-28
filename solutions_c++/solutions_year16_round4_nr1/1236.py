#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

int n,a[3],b[3],ans[5000],T,ansx[5000];

void dfs(int x,int y)
{
	if (x>n) 
	{
		ans[++ans[0]]=y;
		b[y]++;
		return;
	}
	dfs(x+1,min(y,(y+1)%3));
	dfs(x+1,max(y,(y+1)%3));
}

int main()
{
//	freopen("A-large.in","r",stdin);
//	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for (int id=1; id<=T; id++)
	{
		scanf("%d%d%d%d",&n,&a[1],&a[0],&a[2]);
		int flag=0;
		ansx[1]=4;
		for (int i=0; i<3; i++)
		{
			ans[0]=b[0]=b[1]=b[2]=0;
			dfs(1,i);
			if ((b[0]==a[0])&&(b[1]==a[1])&&(b[2]==a[2])) 
			{
			flag=1;
			for (int j=1; j<=ans[0]; j++) 
			  if (ans[j]>ansx[j]) break; else
			  if (ans[j]<ansx[j]) 
			  {
			  	for (int k=0; k<=ans[0]; k++) ansx[k]=ans[k];
			  	break;
			  }
		}
		}
		printf("Case #%d: ",id);
		if (!flag) printf("IMPOSSIBLE"); else
		{
			int S=(1<<n);
			for (int i=1; i<S; i<<=1)
			  for (int j=1; j<=S; j+=(i<<1))
			  {
			  	flag=0;
			  	for (int k=0; k<i; k++)
			  	  if (ansx[j+k]>ansx[j+k+i]) {flag=1; break;} else
			  	  if (ansx[j+k]<ansx[j+k+i]) break;
			  	if (flag)
			  	for (int k=0; k<i; k++) swap(ansx[j+k],ansx[j+k+i]);
			  }
		for (int i=1; i<=ansx[0]; i++)
		  if (ansx[i]==0) printf("P"); else
		  if (ansx[i]==1) printf("R"); else 
		  				  printf("S");
		  			}
		printf("\n"); 
	}
	return 0;
}
	
