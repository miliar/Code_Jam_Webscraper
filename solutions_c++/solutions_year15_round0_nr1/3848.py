#include<map>
#include<string>
#include<cstring>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<queue>
#include<vector>
#include<iostream>
#include<algorithm>
#include<bitset>
#include<climits>
#include<list>
#include<iomanip>
#include<stack>
#include<set>
using namespace std;
int main()
{
	freopen("A-large(3).in","r",stdin);
	freopen("A-large(3).out","w",stdout);
	int T;
	cin>>T;
	for(int cs=1;cs<=T;cs++)
	{
		int mx;
		string s;
		cin>>mx>>s;
	//	cout<<mx<<" "<<s<<endl;
	//	continue;
		int sum=0,ans=0;
		for(int i=0;i<=mx;i++)
		{
			if(sum<i)
			{
				ans+=i-sum;
				sum=i;
			}
			sum+=s[i]-'0';
		}
		printf("Case #%d: %d\n",cs,ans);
	}
}
