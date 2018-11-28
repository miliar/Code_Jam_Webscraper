#include<iostream>
#include <fstream>
#include <cstdio>
#include<cstring>
using namespace std;
int main()
{

	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,in,cnt,res,m,n,i,j;
	scanf("%d",&t);
    for(in=1;in<=t;in++)	
	{
		int a1[4][4],a2[4][4];
		memset(a1,0,sizeof(a1));memset(a2,0,sizeof(a2));
		cnt = res = 0;
	scanf("%d",&m);
		for(i=0;i<4;i++)
		 for(j=0;j<4;j++)scanf("%d",&a1[i][j]);
		
	scanf("%d",&n);
		for(int i=0;i<4;i++)
		 for(int j=0;j<4;j++)scanf("%d",&a2[i][j]);
		
		for(int i=0;i<4;i++)
		 for(int j=0;j<4;j++)
		{
		   if(a1[m-1][i]==a2[n-1][j])
		   {
   				cnt++;   	
				res=a1[m-1][i];	
   		   }
		}
printf("Case #%d: ",in);
		 if(cnt==1)printf("%d\n",res);
		else if(cnt==0)printf("Volunteer cheated!\n");
		else if(cnt>1)printf("Bad magician!\n");
		
	
	}
return 0;		
}