#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#define prNo 1000
#define n 32
using namespace std;
vector<int> pr;
int v[11][prNo][n];
int main()
{
	freopen("Cbg.txt","w",stdout);
	int T;
	cin>>T;
	int tn,jj;
	cin>>tn>>jj;
	jj=500;
	{
		int cur=2;
		while(pr.size()!=prNo)
		{
			int i;
			for(i=2;i*i<=cur;i++)
			{
				if(cur%i==0)
					break;
			}
			if(i*i>cur)
			{
				pr.push_back(cur);
			}
			cur++;
		}
	}
	printf("Case #1:\n");
	for(int k=2;k<=10;k++)
	{
		for(int i=0;i<prNo;i++)
		{
			v[k][i][0]=1;
			for(int j=1;j<n;j++)
			{
				v[k][i][j]=(v[k][i][j-1]*k)%pr[i];
			}
		}
	}
	int nn=n-2;
	int div[11];
	int bytes[50]={0};
	bytes[n-1]=bytes[0]=1;
	for(int i=0;(i<(1<<nn))&&jj;i++)
	{
		int cur=1;
		int ii=i;
		while(ii)
		{
			bytes[cur++]=ii%2;
			ii/=2;
		}
		int j=2;
		for(j=2;j<=10;j++)
		{
			int k=0;
			for(k=0;k<prNo;k++)
			{
				int sm=0;
				for(int l=0;l<n;l++)
				{
					sm+=(bytes[l]*v[j][k][l]);
				}
				if(sm%pr[k]==0)
				{
					div[j]=pr[k];
					break;
				}
			}
			if(k==prNo)
				break;
		}
		if(j==11)
		{
			jj--;
			for(int k=n-1;k>=0;k--)
			{
				cout<<bytes[k];
			}
			for(int k=2;k<=10;k++)
				cout<<" "<<div[k];
			cout<<endl;
		}
	}
	return 0;
}