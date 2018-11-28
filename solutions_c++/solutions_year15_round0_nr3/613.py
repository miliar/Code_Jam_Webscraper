#include<bits/stdc++.h>
#define maxn 200005
using namespace std;

char s[maxn];
bool dp[maxn][4][4][2];
int main()
{
	freopen("C:\\Users\\DARPAN\\Desktop\\input.in","r",stdin);
    freopen("C:\\Users\\DARPAN\\Desktop\\output.txt","w",stdout);
	int a1[4][4]={{0,1,2,3},{1,0,3,2},{2,3,0,1},{3,2,1,0}};
	int a2[4][4]={{0,0,0,0},{0,1,0,1},{0,1,1,0},{0,0,1,1}};
	int t;
	cin>>t;
	int k=1;
	while(t--)
    {
		long long l,x;
		cin>>l>>x;
        cin>>s;
		x = min(x,12LL+(x%4LL));
		for(int i=l;i<l*x;++i) s[i] = s[i%l];
		memset(dp,0,sizeof(dp));
		dp[0][0][0][0] = 1;
		for(int i=0;i<l*x;++i)
        {
			for(int j=0;j<4;++j)
                for(int p=0;p<4;++p)
                    for(int q=0;q<2;++q)
                    {
                        int c;
                        if(s[i] == 'i') c = 1;
                        else if(s[i] == 'j') c = 2;
                        else c = 3;
                        dp[i+1][j][a1[p][c]][q^a2[p][c]]= dp[i][j][p][q];
                    }

			dp[i+1][1][0][0] = dp[i+1][0][1][0];
			dp[i+1][2][0][0] = dp[i+1][1][2][0];
			dp[i+1][3][0][0] = dp[i+1][2][3][0];

			dp[i+1][1][0][1] = dp[i+1][0][1][1];
			dp[i+1][2][0][1] = dp[i+1][1][2][1];
			dp[i+1][3][0][1] = dp[i+1][2][3][1];
		}

		if(dp[l*x][3][0][0])
        {
			printf("Case #%d: YES\n",k);
		}
		else
		{
			printf("Case #%d: NO\n",k);
		}
		k++;
	}
	return 0;
}
