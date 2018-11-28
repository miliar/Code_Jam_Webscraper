#include<bits/stdc++.h>
#define mp make_pair
#define ff first
#define ss second
using namespace std;

pair<int,int > pp[100];
int ch[100];

int main()
{
	int test;
	scanf("%d",&test);
	for(int a=1;a<=test;a++)
	{
		int ans=1;
		int temp=0;
		int p;
		scanf("%d",&p);
		for(int b=0;b<p;b++)
		{
			scanf("%d",&ch[b]);
			pp[b]=mp(b+1,ch[b]);
		}
		int k=0,sh;
		bool ada=true;
		for(int c=2;c<=p;c++)
		{
			sort(pp,pp+p);
			do
			{
				ada=true;
				for(int b=0;b<c;b++)
				{
					//printf("%d ",pp[b].ff);
					if(pp[(b-1)%c].ff!=pp[b].ss && pp[b].ss!=pp[(b+1)%c].ff)
						ada=false;
				}
				if(ada==true)
				{	
					ans = c;
					break;
				}
			}while(next_permutation(pp,pp+p));
			//printf("%d\n",ada);
		}
		printf("Case #%d: %d\n",a,ans);
	}
}
