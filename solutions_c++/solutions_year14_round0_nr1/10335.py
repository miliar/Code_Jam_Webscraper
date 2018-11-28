#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const unsigned int mod=1000000007;
int main()
{	int a[4],b[4],d,cas=1,i,j,k,l,m,n,q,r,t,v,w,x,y,z;
	for(scanf("%d",&t);t--;)
	{	
		scanf("%d",&r);//scanf("%s",s);//l=strlen(s);
		for(i=1;i<r;i++)
			for(j=1;j<=4;j++)
				scanf("%*d");
		for(j=0;j<4;j++)
			scanf("%d",a+j);
		for(i=r+1;i<=4;i++)
			for(j=0;j<4;j++)
				scanf("%*d");
		
		scanf("%d",&r);//scanf("%s",s);//l=strlen(s);
		for(i=1;i<r;i++)
			for(j=1;j<=4;j++)
				scanf("%*d");
		for(j=0;j<4;j++)
			scanf("%d",b+j);
		for(i=r+1;i<=4;i++)
			for(j=0;j<4;j++)
				scanf("%*d");
		
		r=0;//possible answers
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
				if(a[i]==b[j])
					break;
			if(j<4)
			{
				r++;
				x=a[i];
			}
		}
//		printf("			r : %d\n",r);
		printf("Case #%d: ",cas++);
		if(r==1)
			printf("%d\n",x);
		else if(r==0)
			printf("Volunteer cheated!\n");
		else
			printf("Bad magician!\n");
	}
	return 0;}
