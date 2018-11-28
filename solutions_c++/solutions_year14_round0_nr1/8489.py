#include<bits/stdc++.h>
using namespace std;

int i,t,j,k,l,a[4][4],b[4][4],u,v,mark1[4][4],mark2[4][4];
int cnt;
int main()
{
	ifstream iff("A-small-attempt1.in");
	ofstream off("hell.txt");
	iff>>t;
	for(i=1;i<=t;i++)
	{
		iff>>u;
		cnt=0;
		memset(mark1,0,sizeof(mark1));
		memset(mark2,0,sizeof(mark2));
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				iff >> a[j][k];
			}
		}
		
		iff>>v;
		
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				iff >> b[j][k];
			}
		}
		int l;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				if(a[u-1][k]==b[v-1][j] && mark1[u-1][k]==0 && mark2[v-1][j]==0)
				{
					cnt++;
					mark1[u-1][k]=1;
					mark2[v-1][j]=1;
					l=a[u-1][k];
				}
			}
		}
	//	off<<cnt<<endl;
		if(cnt==0)
		{
			off<<"Case #"<<i<<": Volunteer cheated!"<<endl;
		}
		if(cnt==1)
		{
			off<<"Case #"<<i<<": "<<l<<endl;
		}
		if(cnt>1)
		{
			off<<"Case #"<<i<<": Bad magician!"<<endl;
		}
		
	}
	return 0;
}
