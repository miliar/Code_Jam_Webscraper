#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
using namespace std;

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	for(int c = 1; c <= t; ++c)
	{
		int a,b,re = 0;
		cin>>a>>b;
		for(int j = a; j <= b; ++j)
		{
            char s[10],t[10],ss[10],tt[10];
            itoa(j,s,10);
            strcpy(ss,s);
            reverse(s,s + strlen(s));
			int m = sqrt((double)j);
			if(strcmp(s,ss) == 0 && m * m == j)
			{
				itoa(m,t,10);
				strcpy(tt,t);
				reverse(t,t + strlen(t));
				if(strcmp(t,tt) == 0)
				    re++;
			}
		}
		cout<<"Case #"<<c<<": "<<re<<endl;
	}
	//system("pause");
	return 0;
}
