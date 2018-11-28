#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<cstring>
#define FOR(a,b,c) for(a=b;a<c;++a)
#define sd(a) scanf("%d",&a)
using namespace std;

int main() {
  freopen("A-small-attempt0.in", "r", stdin);
  freopen("out", "w", stdout);
  int t,n,i,j,h;
	sd(t);
	FOR(h,1,t+1)
	{
		char str[105]="\0";
		int sum=0,flag=0,cmin[105]={0},cmax[105]={0};
		sd(n);
		string s;
		cin>>s;
		i=0;
		j=0;
		while(i<s.size()-1)
		{
			int c=0;
			while(s[i]==s[i+1]&&i<s.size()-1)
			{
				c++;
				i++;
			}
			cmin[j]=c+1;
			cmax[j]=c+1;
			if(s[i]!=NULL)
			{
				str[j]=s[i];
				j++;
				i++;
			}
		}
		if(s[i]!=s[i-1]&&s[i]!=NULL)
		{
			str[j]=s[i];
			cmin[j]=1;
			cmax[j]=1;
			j++;
		}
		n--;
		while(n--)
		{
			char abc[105]="\0";
			cin>>s;
			i=0;
			j=0;
			while(i<s.size()-1)
			{
				int c=0;
				while(s[i]==s[i+1]&&i<s.size()-1)
				{
					c++;
					i++;
				}
				if(c+1>cmax[j])
				{
					cmax[j]=c+1;
				}
				else
				if(c+1<cmin[j])
				{
					cmin[j]=c+1;
				}
				if(s[i]!=NULL)
				{
					abc[j]=s[i];
					j++;
					i++;
				}
			}
			if(s[i]!=s[i-1]&&s[i]!=NULL)
			{
				abc[j]=s[i];
				if(cmax[j]<1)
				{
					cmax[j]=1;
				}
				else
				if(cmin[j]>1)
				{
					cmin[j]=1;
				}
				j++;
			}
			if(strcmp(abc,str))
			{
				flag=1;
			}
		}
	//	FOR(i,0,j)
	//	cout<<cmin[i]<<" "<<cmax[i]<<endl;
		cout<<"Case #"<<h<<": ";
		if(flag)
		{
			cout<<"Fegla Won\n";
		}
		else
		{
			FOR(i,0,j)
			sum+=cmax[i]-cmin[i];
			cout<<sum<<endl;
		}
		
	}
	return 0;
}
