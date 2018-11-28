#include<cstdio>
#include<iostream>
using namespace std;

int main()
{
	int max,flag,lo,hi,mid,T,N,i,j,k,a,b,c;
	int m[1010];
	int ans1,ans2;
	scanf("%d",&T);
	for(a=1;a<=T;a++)
	{
		scanf("%d",&N);
		scanf("%d",&m[0]);
		ans1=0;
		max=0;
		for(i=1;i<N;i++)
		{
			scanf("%d",&m[i]);
			if(m[i]<m[i-1])
			{
				ans1+=(m[i-1]-m[i]);
				if(m[i-1]-m[i]>max)
					max=m[i-1]-m[i];
			}
		}
		ans2=0;
		for(i=0;i<N-1;i++)
		{
			if(!max)
				break;
			if(m[i]>=max)
				ans2+=max;
			else if(m[i]<max)
				ans2+=m[i];
			//else if(m[i]%lo!=0 && m[i]>lo*10)
			//	ans2+=lo*10;
			//else if(m[i]%lo!=0 && m[i]<lo*10 && lo!=0)
			//	ans2+=(m[i]/lo)*lo;
		}
		cout<<"Case #"<<a<<": "<<ans1<<' '<<ans2<<endl;
	}
	return 0;
}

