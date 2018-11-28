
#include<bits/stdc++.h>
using namespace std;
char key[10];
char tar[10];
typedef long long int ll;
#define mod 1000000007
int main()
{
	int t,k,l,s;
	int x=1;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d%d",&k,&l,&s);	
		scanf("%s",key);scanf("%s",tar);
		cout<<"Case #"<<x++<<": ";
		int max=0;
		int total=0;
		
		int i;
		int lim=1;
		for(i=0;i<s;i++)
			lim=lim*k;
		for(i=0;i<lim;i++)
		{
			int index=0;
			int temp=i;
			char ar[10];
			while(temp)
			{
				int d=temp%k;
				ar[index++]=key[d];
				temp=temp/k;
			}
			for(int j=index;j<s;j++)
				ar[j]=key[0];
			int count=0;
			for(int len=0;len<s;len++)
			{
				int f=0;
				for(int k=0;k<l;k++)
				{
					if(len+k<s && ar[len+k]==tar[k])
					{
						f=1;
					}
					else
					{
						f=0;
						break;
					}
				}
				if(f==1)
					count++;

			}
			if(count>max)
				max=count;
			total=total+count;
		}
		printf("%lf\n",max-(total*1.0)/lim);
	}
	return 0;
}