#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <set> 
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int s;
	string str;
	int T,caseT=0;
	cin>>T;
	while (T--){
	cin>>s;
	int sum=0,ans=0;
	for (int i=0;i<=s;i++)
	{
		char t=getchar();
		if (!(t>='0'&&t<='9')) t=getchar();
		if (sum<i)
		{
			ans+=(i-sum);
			sum+=(i-sum);
		}	
		sum+=(t-'0');
	}
	cout<<"Case #"<<(++caseT)<<": "<<ans<<endl;
	}
	
	return 0;
}