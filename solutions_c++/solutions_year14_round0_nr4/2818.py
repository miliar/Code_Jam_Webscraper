#include<bits/stdc++.h>

using namespace std;

const int MAX = 1232;
int T;
int N;
double ip[MAX];
double op[MAX];
int dp[MAX][MAX];

int main()
{
	cin >> T;
	for(int _t=1;_t<=T;_t++)
	{
		cin >> N;
		for(int i=0;i<N;i++)
		{
			cin >> ip[i];
		}
		for(int i=0;i<N;i++)
		{
			cin >> op[i];
		}

		sort(ip,ip+N);
		sort(op,op+N);
		
		int ans2=0,i1=0,i2=0;
		
		while(i1<N&&i2<N)
		{
			if(ip[i1]>op[i2])
			{
				i2++;
			}else
			{
				i1++;
				i2++;
			}
		}

		ans2=N-i1;
		for(int k=0;k<=N;k++)
		{
			for(int i=0;i+k<=N;i++)
			{
				int j=i+k;
				if(k==0) 
				{
					dp[i][j]=0;
					continue;
				}

				double v=ip[N-k];
				dp[i][j]=0;
				if(v>op[i]) dp[i][j]=max(dp[i][j],dp[i+1][j]+1);
				
				dp[i][j]=max(dp[i][j],dp[i][j-1]);
			}
		}

		cout << "Case #" << _t << ": " << dp[0][N] << " " << ans2 << endl;
	}
}
