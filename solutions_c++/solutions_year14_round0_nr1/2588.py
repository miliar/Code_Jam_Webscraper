#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    freopen("A-small-attempt0.in", "rt", stdin);
    freopen("A-small.out", "wt", stdout);
	int tc,a[5],b[5],ch,n;
	scanf("%d",&tc);
	for(int x=1;x<=tc;x++)
	{
		scanf("%d",&ch);
		for(int i=1;i<=4;i++)
		{
			if(i==ch)
			{
				for(int j=1;j<=4;j++)
						scanf("%d",&a[j]);
			}
			else
			{
				for(int j=1;j<=4;j++)
					scanf("%d",&n);
			}
		}
		scanf("%d",&ch);
		for(int i=1;i<=4;i++)
		{
			if(i==ch)
			{
				for(int j=1;j<=4;j++)
					scanf("%d",&b[j]);
			}
			else
			{
				for(int j=1;j<=4;j++)
					scanf("%d",&n);
			}
		}
		n=0;
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
				if(b[i]==a[j])
				{
					ch=a[j];
					n++;
				}
		if(n==0)
			printf("Case #%d: Volunteer cheated!\n",x);
		else if(n==1)
			printf("Case #%d: %d\n",x,ch);
		else
			printf("Case #%d: Bad magician!\n",x);
	}
	return 0;
}
