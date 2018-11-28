/* ***********************************************
Author        :axp
Created Time  :2016/6/11 23:23:57
TASK		  :D.cpp
LANG          :C++
************************************************ */

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

string gen(int x)
{
	string re;
	while(x--)
		re+='1';
	return re;
}

int main()
{
    freopen("D-small-attempt2.in","r",stdin);
    freopen("out.txt","w",stdout);
    int n,l;
	int T;
	string out;

	for(int i=0;i<30;i++)out+="10";
	out+='?';
	for(int i=0;i<30;i++)out+="10";

	cin>>T;
	for(int kase=1;kase<=T;kase++)
	{
		cin>>n>>l;
		string s;
		string k=gen(l);
		bool flag=1;
		for(int i=0;i<n;i++)
		{
			cin>>s;
			if(s==k)
			{
				flag=0;
			}
		}
		cin>>s;
		cout<<"Case #"<<kase<<": ";
		if(flag==0)
		{
			puts("IMPOSSIBLE");
			continue;
		}
		s="";
		if(l==1)
		{
			puts("? 0");
		}
		else
		{
			for(int i=1;i<l;i++)
				s+='?';
			cout<<s<<' '<<out<<endl;
		}
	}
    return 0;
}
