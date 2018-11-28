#include<bits/stdc++.h>
using namespace std;
char st[10004];
int inp[10004];
int main()
{
	int t,tt,l,x,i,j,ans,isneg,fi,lk,lkn;
	int  pro[4][4]={{0,1,2,3},{1,0,3,2},{2,3,0,1},{3,2,1,0}};
	bool neg[4][4]={{0,0,0,0},{0,1,0,1},{0,1,1,0},{0,0,1,1}};
	char sym[4]={'1','i','j','k'};
	scanf("%d",&t);
	for(tt=1;tt<=t;tt++)
	{
		ans=0;
		isneg=0;
		fi=lk=lkn=-1;
		scanf("%d %d %s",&l,&x,st);
		
		for(i=0;i<l;i++)
		{
			switch(st[i])
			{
				case '1':	inp[i]=0;break;
				case 'i':	inp[i]=1;break;
				case 'j':	inp[i]=2;break;
				case 'k':	inp[i]=3;break;
				default :	assert(0);
			}
		}

		for(i=0;i<l;i++)
			for(j=0;j<x;j++)
				inp[i+j*l]=inp[i];

		for(i=0;i<l*x;i++)
		{
			if(neg[ans][inp[i]])
				isneg^=1;
			ans=pro[ans][inp[i]];
			if(fi==-1 && ans==1 && isneg==0)
				fi=i;
			if(ans==3 && isneg==0)
				lk=i;
		}
		//cout<<"\n "<<fi<<" "<<lk<<"\n";
		if(ans== 0 && isneg==1 && fi>-1 && lk>fi)
			printf("Case #%d: YES\n",tt);
		else
			printf("Case #%d: NO\n",tt);
	}
}