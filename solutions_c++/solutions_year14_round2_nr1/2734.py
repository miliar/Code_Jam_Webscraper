#include<iostream>
#include<cstdio>
#include<string>

using namespace std;
string A[200];
int B[200];
int AA[200][200];
int k[200];
char c[200][200];


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	int N;
	cin>>T;
	int x;
	for (x=1;x<=T;x++)
	{
		int flag=false;
		int ans=0;
		cin>>N;
		for(int  i=0;i<N;i++)
		{
			cin>>A[i];
			k[i]=0;
			AA[0][i]++;
			B[0]++;
			c[0][i]=A[i][0];
			for(int j=1;j<A[i].length();j++)
			{
				if (A[i][j-1]!=A[i][j]) k[i]++;
				c[k[i]][i]=A[i][j];
				AA[k[i]][i]++;
				B[k[i]]++;
			}
		}
		for (int i=0;i<N;i++)
			for(int j=0;j<N;j++)
				if (k[i]!=k[j]) flag=true;
		for (int i=0;(i<N)&&(!flag);i++)
			for(int j=0;j<N;j++)
				for (int y=0;y<=k[0];y++)
					if (c[y][i]!=c[y][j]) flag=true;
		for(int j=0;(j<=k[0]) && (!flag);j++)
		{
			if ((B[j]<N) && (B[j]!=0)) flag=true; 
			B[j]/=N;
		}
		for(int i=0;(i<N) && (!flag);i++)
			for (int j=0;j<=k[0];j++)
			{
				ans=ans+abs(AA[j][i]-B[j]);
				if ((AA[j][i]==0) && (B[j]!=0)) 
				{
					flag=true; 
					break;
				}
			}
		cout<<"Case #"<<x<<": ";
		if (flag) cout<<"Fegla Won"<<endl; else cout<<ans<<endl;
		for (int i=0;i<N;i++)
			for(int j=0;j<200;j++)
			{
				AA[j][i]=0;
				B[j]=0;
				c[i][j]=0;
				k[j]=0;
			}
	}
	return 0;
}