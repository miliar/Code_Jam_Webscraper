#include <iostream>
#include<stdio.h>
using namespace std;

int main() {
int t,selected,ans=0,answer,a[4],b[4],temp,m,l,i,j;
cin>>t;
int t1=t;
while(t--)
{
		cin>>selected;
		ans=0;
		m=(selected-1)*4;
		for(i=0,l=0;i<16;i++)
		if((i>=m) && (i<m+4))
				scanf("%d",&a[l++]);
		else
			scanf("%d",&temp);
		cin>>selected;
		m=(selected-1)*4;
		for(i=0,l=0;i<16;i++)
		if((i>=m) && (i<m+4))
				scanf("%d",&b[l++]);
		else
			scanf("%d",&temp);
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		{
			if(a[i]==b[j])
			{answer=a[i];
			ans++;}
			if(ans>1)
			break;
		}
		switch(ans)
		{
			case 1: printf("Case #%d: %d\n",t1-t,answer);break;
			case 0: printf("Case #%d: Volunteer cheated!\n",t1-t);break;
			default: printf("Case #%d: Bad magician!\n",t1-t);break;
		}ans=0;
}
	return 0;
}