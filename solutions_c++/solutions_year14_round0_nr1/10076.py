#include<iostream.h>
#include<fstream.h>
main()
{
	int q1[4][4],q2[4][4],t,a1,a2,ans[101],count=0,m=0,cnt[101];
	ifstream a;
	a.open("A-small-attempt3.in");
	a>>t;
	for(int k=1;k<=t;k++)
	{
	a>>a1;
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			a>>q1[i][j];	
		}
	}
	a>>a2;
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			a>>q2[i][j];	
		}
	}
	for(int o=0;o<4;o++)
	{
		for(int p=0;p<4;p++)
		{
			if(q1[a1-1][o]==q2[a2-1][p])
			{
				count++;
				if(count==1)
				{
				 	ans[m]=q1[a1-1][o];
					m++;
				}
			}
		}
	}
	if(count==0)
	{
		m++;
	}
	cnt[k-1]=count;
	count=0;
}
	ofstream b;
	b.open("magop.txt");
	for(int s=1;s<=t;s++)
	{
	if(cnt[s-1]==1)
	{
		b<<"Case #"<<s<<": "<<ans[s-1]<<endl;
	}
	else if(cnt[s-1]>=2)
	{
		b<<"Case #"<<s<<": Bad magician!"<<endl;
	}
	else if(cnt[s-1]==0)
	{
		b<<"Case #"<<s<<": Volunteer cheated!"<<endl;
	}
	}
}