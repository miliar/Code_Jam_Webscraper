#include<iostream>
#include<cstdlib>
#include<algorithm>
#include<sstream>
using namespace std;

bool isPalin(int N)
{
	stringstream ss;
	ss << N;
	string s = ss.str();
	string rev = s;
	reverse(s.begin(),s.end());
	if(rev == s)
		return 1;
	return 0;
}
int main()
{
	int cas =1;
	int n;
	freopen("in.in","r",stdin);
	cin >> n;
	int dp[1001];
	dp[0]=0;
	for(int i=0;i<=1000;i++) dp[i]=0;
	for(int i=1;i<=1000;i++)
	{
		if(isPalin(i))
		{
			int temp = i*i;
			if(temp<=1000)
			{
			if(isPalin(temp))
			{
				dp[temp]+=1;
				
			}
			
			}
		}
		dp[i]=dp[i-1]+dp[i];
	}
	while(n--)
	{
		int a,b;
		cin >> a >> b;
		int ans = dp[b] - dp[a-1];
		cout<< "Case #"<<cas <<": "<< ans<<"\n";
		cas ++;
	}

}