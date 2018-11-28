#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
using namespace std;
int main()
{
  int t,x=1,cnt,cnt2,flag=0;
  int arr[20][20];
  scanf("%d",&t);
  while(t--)
  {
	flag=0;
	int n,m;
	scanf("%d%d",&n,&m);
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			scanf("%d",&arr[i][j]);
		}
	}
 	//for small input file
	int min=1;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			if(arr[i][j]==min)
			{
				cnt=cnt2=0;
				for(int k=0;k<n;k++)
				if(arr[k][j]==min)
				cnt++;
				for(int k=0;k<m;k++)
				if(arr[i][k]==min)
				cnt2++;	
				if(cnt!=n && cnt2!=m)
				{	flag=1;break;}
			}
	//	if(flag) break;

		}
		if(flag) break;
	}
	if(flag==0) printf("Case #%d: YES\n",x++);
	else printf("Case #%d: NO\n",x++);
  }
}
