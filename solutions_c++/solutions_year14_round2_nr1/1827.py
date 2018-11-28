#include<cstdio>
#include<cstring>
#include<string>
#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;
const int N = 105;
int n;
int dp[N][N];
	
int main()
{
	//fstream cin("C:\\Users\\swcandy\\Desktop\\A-small-attempt0 (3).in", ios::in);
	//fstream cout("C:\\Users\\swcandy\\Desktop\\A-small-attempt0.out", ios::out);
	
	int t,times=0;
	cin >> t;
	while (t--) {
		cin >> n;
		string a,b;
		cin >> a >> b;
		memset(dp,-1,sizeof(dp));
		dp[0][0] = 0;
		for (int i = 1; i <= a.length(); i++)
			for (int j = 1; j <= b.length(); j++)
				if (a[i-1] == b[j-1]) {
					if (dp[i-1][j-1]>=0) dp[i][j] = (dp[i][j]>=0)?min(dp[i][j],dp[i-1][j-1]):dp[i-1][j-1];
					if (dp[i][j-1]>=0) dp[i][j] = (dp[i][j]>=0)?min(dp[i][j],dp[i][j-1]+1):dp[i][j-1]+1;
					if (dp[i-1][j]>=0) dp[i][j] = (dp[i][j]>=0)?min(dp[i][j],dp[i-1][j]+1):dp[i-1][j]+1;
				}
		if (dp[a.length()][b.length()]>=0)
			cout << "Case #" << ++times << ": " << dp[a.length()][b.length()] << endl;
		else cout << "Case #" << ++times << ": Fegla Won" << endl;
	}
	return 0;
}
			
		