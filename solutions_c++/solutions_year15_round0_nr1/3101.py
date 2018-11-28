#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <iostream>
#include <cstdlib>
#include <sstream>
using namespace std;

void solve()
{
	int n;
	string s;
	cin>>n>>s;
	int ans=0;
	int sum=0;
	for(int i=0;i<s.size();i++)
	{
		ans=max(ans,i-sum);
		sum+=s[i]-'0';
	}
	cout<<ans<<endl;
}
int main()
{
	freopen("/Users/francis/Documents/in.txt","r",stdin);
	freopen("/Users/francis/Documents/out.txt","w",stdout);
	int T;
	cin>>T;
	for(int cas=1;cas<=T;cas++)
	{
		printf("Case #%d: ",cas);
		solve();
	}
}
