#include <cstdio>
#include <iostream>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <string.h>
#define lldd long long int
using namespace std;
int main()
{
freopen("A-a-attempt0.in","r",stdin);
freopen("output.txt","w",stdout);
int t;
scanf("%d",&t);
for(int q=1;q<=t;q++)
	{
		int n;
		scanf("%d",&n);
		int l[n];
		char a[n][102];
		for(int i=0;i<n;i++)
			scanf("%s",a[i]);
			// mid....
		char b[n][102];
		int k[n];
		for(int i=0;i<n;i++){ k[i]=0;l[i]=0;}
		for(int i=0;i<n;i++)
		{int j;
			for(j=0;a[i][j]!='\0';j++)
				{
				if(j==0)
					b[i][k[i]++]=a[i][j];
				else if(a[i][j]!=a[i][j-1])
					b[i][k[i]++]=a[i][j];
				}
				l[i]=j;
		}
			b[0][k[0]]='\0';b[1][k[1]]='\0';
			if(strcmp(b[0],b[1])!=0)
			{
				printf("Case #%d: Fegla Won\n",q);
				continue;
			}
			//mid.. end
			//cout<<"="<<l[0]<<" "<<l[1]<<"="<<endl;
			lldd ans=0;
			int k1=0,k2=0;
			while(k1!=(l[0]-1) && k2!= (l[1]-1))
			{
				if(a[0][k1]==a[1][k2])
				{
					k1++;k2++;
				}
				else if(a[0][k1]==a[0][k1-1])
				{
					ans++;
					k1++;
				}
				else
				{
					ans++;
					k2++;
				}
			//	cout<<"*"<<k1<<" "<<k2<<"*";
				//getchar();
			}
			ans=ans+l[0]+l[1]-2-k1-k2;
		printf("Case #%d: %lld\n",q,ans);
	}
return 0;	
}