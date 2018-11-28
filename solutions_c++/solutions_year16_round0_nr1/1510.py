#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <vector>
using namespace std;

const int MAXN=2147483647;

int i,j,k,n,m,t,x,y,bit,tcase,xcase;
string s;
ostringstream oss;


int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	cin>>tcase;
	xcase=0;
	while (xcase<tcase)
	{
		xcase++;
		cout<<"Case #"<<xcase<<": ";
		cin>>n;
		if (n==0)
		{
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		x=0;
		bit=0;
		while (bit!=1023)
		{
			x+=n;
			oss.clear();
			oss.str("");
			oss<<x;
			s=oss.str();
			for (i=0;i<s.length();i++)
			{
				bit|=(1<<(s[i]-'0'));
			}
			// cout<<x<<"\t-\t"<<bit<<endl;
		}
		cout<<x<<endl;
	}
	return 0;
}

