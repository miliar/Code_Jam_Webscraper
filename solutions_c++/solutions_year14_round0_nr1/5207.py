#include <iostream>
#include<cstdio>
using namespace std;

int main() {
	int t;
freopen ("A-small-attempt0.in","r",stdin);
	freopen ("out.txt","w",stdout);
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++)
	{
		int a[16],b[4][4],d[4][4];
		int ch1,ch2;
		scanf("%d",&ch1);
		ch1--;
		for(int i=0;i<16;a[i++]=0);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				scanf("%d",&b[i][j]);
				b[i][j]--;
				if(i==ch1)
					a[b[i][j]]=1;
			}
		scanf("%d",&ch2);
		ch2--;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				scanf("%d",&d[i][j]);
				d[i][j]--;
			}
		bool f1=false,f2=false;
		int ans=0;
		for(int j=0;j<4;j++)
		{
			if(a[d[ch2][j]])
			{
				if(f1)
				{
					f2=true;
					break;
				}
				else
				{
					ans=d[ch2][j];
					f1=true;
				}
			}
		}
		if(!f1)
		{
			cout<<"Case #"<<tc<<": Volunteer cheated!\n";
		}
		else if(f2)
			cout<<"Case #"<<tc<<": Bad Magician!\n";
		else
			cout<<"Case #"<<tc<<": "<<ans+1<<"\n";

	}


	return 0;
}
