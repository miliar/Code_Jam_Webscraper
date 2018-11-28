#include <stdio.h>
#include <stdlib.h>
#include <sstream>
#include <iostream>

using namespace std;

int main()
{
	string st;
	getline(std::cin,st);
	int t=atoi(st.c_str());
	for (int j = 0; j < t; ++j)
	{
		getline(std::cin,st);
		stringstream ss(st);
		ss>>st;
		int smax=atoi(st.c_str());
		ss>>st;
		int cnt=(int)st[0]-48;
		int ans=0;
		for (int i = 1; i <= smax; ++i)
		{
			if(cnt<i)
			{
				ans+=i-cnt;
				cnt+=i-cnt+(int)st[i]-48;
			}
			else
			{
				cnt+=(int)st[i]-48;
			}
		}
		printf("Case #%d: %d\n",(j+1),ans);
	}
}
