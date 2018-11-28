#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin>>T;
	for (int t=0;t<T;t++)
	{
		cout<<"Case #"<<t+1<<": ";
		int res=0;
		int smax;
		int s[20000];
		int total[20000];
		string str;
		cin>>smax>>str;
		for (int i=0;i<=smax;i++)
		{
			s[i]=str[i]-48;
		}
		total[0]=0;
		for (int i=1;i<=smax;i++)
		{
			total[i]=total[i-1]+s[i-1];
			while (total[i]<i)
			{
				total[i]++;
				res++;
			}
		}
		cout<<res<<endl;
	}
	return 0;
}
