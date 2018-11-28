#include<iostream>

using namespace std;

int landco[100][100],rw,cl;

int rwchk(int n,int m)
{
	int i;
	for(i=0;i<cl;i++)
		if(landco[n][m]<landco[n][i])
			return 0;

	return 1;
}

int clchk(int n,int m)
{
	int i;
	for(i=0;i<rw;i++)
		if(landco[n][m]<landco[i][m])
			return 0;

	return 1;
}

int main()
{
	int t,i,j,run=1,broke,ans[101];
	cin>>t;
	while(run<=t)
	{
		cin>>rw;
		cin>>cl;
		for(i=0;i<rw;i++)
			for(j=0;j<cl;j++)
				cin>>landco[i][j];
		broke=0;
		for(i=0;i<rw;i++)
		{
			for(j=0;j<cl;j++)
				if( !(rwchk(i,j) || clchk(i,j)) )
				{
					ans[run]=0;
					broke=1;
					break;
				}
			if(broke==1)
				break;
		}
		if(broke==0)
			ans[run]=1;
		run++;
	}

	for(i=1;i<t+1;i++)
		{
			if(ans[i]==0)
				cout<<"Case #"<<i<<": "<<"NO"<<"\n";
			else if(ans[i]==1)
				cout<<"Case #"<<i<<": "<<"YES"<<"\n";
		}

}
