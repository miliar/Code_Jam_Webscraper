#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>

#include <map>
#define LL long long
#define ff first
#define ss second
#define PB push_back
#define MP make_pair
using namespace std;
int prefwie[505][505],sufwie[505][505],sufkol[505][505],prefkol[505][505];
int t,n,m,tab[505][505];;
int main()
{
  scanf("%d",&t);
  for(int z=1;z<=t;z++)
  {
    int nie=0;
    for(int i=1;i<=n;i++)
    {
      for(int j=1;j<=m;j++)
	prefkol[i][j]=prefwie[i][j]=sufkol[i][j]=sufwie[i][j]=0;
    }
    printf("Case #%d: ",z);
    scanf("%d %d",&n,&m);
    for(int i=1;i<=n;i++)
    {
      for(int j=1;j<=m;j++)
      {
	scanf("%d",&tab[i][j]);
	prefkol[i][j]=max(prefkol[i][j-1],tab[i][j]);
	prefwie[i][j]=max(prefwie[i-1][j],tab[i][j]);
      }
    }
    
    for(int i=n;i>=1;i--)
    {
      for(int j=m;j>=1;j--)
      {
	sufkol[i][j]=max(sufkol[i][j+1],tab[i][j]);
	sufwie[i][j]=max(sufwie[i+1][j],tab[i][j]);
      }
    }
    
    for(int i=1;i<=n;i++)
    {
      for(int j=1;j<=m;j++)
      {
	if((sufkol[i][j]>tab[i][j]||prefkol[i][j]>tab[i][j])&&(sufwie[i][j]>tab[i][j]||prefwie[i][j]>tab[i][j]))
	{
	  nie=1;
	  break;
	}
      }
      if(nie==1)
	break;
    }
    
    printf(nie==1?"NO\n":"YES\n");
    
  }
}