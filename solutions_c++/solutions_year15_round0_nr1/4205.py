#include <cmath> 
#include <cctype>
#include <cstdio>
#include <string>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define Max(a,b) ((a)>(b)?(a):(b))
#define Min(a,b) ((a)<(b)?(a):(b))

bool cmp(const int a, const int b)
{
	return a > b;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int cases=0;	cin>>cases;
	int n;	string s;
	for(int _case=1;_case<=cases;_case++)
	{
		int now=0,ans=0;
		cin>>n>>s;
		for(int i=0;i<=n;i++)
		{
			while(s[i]=='0' && i<=n) i++;
			int num=s[i]-'0';
			if(i>now) ans+=i-now,now+=i-now;
			now+=num;
			//cout<<i<<":"<<now<<endl;
		} 
		printf("Case #%d: %d\n",_case,ans);
	}
	return 0;
}

