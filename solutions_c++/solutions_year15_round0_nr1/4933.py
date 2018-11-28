#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>
#include <cstdlib>
#include <vector>


using namespace std;



void test()
{
	int i,smax,ans=0,sum;
	char s[100001];
	cin>>smax>>s;

	sum=s[0]-'0';
	for(i=1;i<=smax;i++)
	{
		ans=(sum<i)?(i-sum)+ans:ans;
		sum=(sum<i)?(i-sum)+sum+s[i]-'0':sum+s[i]-'0';
	}
	
	cout<<ans;
	
}




int main()
{
	long long T,i;
	cin>>T;
	for(i=1;i<=T;i++)
	{
		cout<<"Case #"<<i<<": ";
		test();
		cout<<"\n";
	}
	return 0;
}
