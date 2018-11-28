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
const char HAPPY='+';
const char BLANK='-';

int i,j,k,n,m,t,x,y,tcase,xcase;
string s;

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	cin>>tcase;
	xcase=0;
	while (xcase<tcase)
	{
		xcase++;
		cout<<"Case #"<<xcase<<": ";
		cin>>s;
		n=s.length();
		while (n>0 && s[n-1]==HAPPY)
		{
			n--;
		}
		x=0;
		if (n>0)
		{
			x=1;
			for (i=n-1;i>0;i--)
			{
				if (s[i]!=s[i-1])
				{
					x++;
				}
			}
		}
		cout<<x<<endl;
	}
	return 0;
}

