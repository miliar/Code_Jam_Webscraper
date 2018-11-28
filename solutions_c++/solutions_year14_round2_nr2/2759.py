
#include<iostream>
#include<vector>
#include<stack>
#include<cstring>
#include<map>
#include<set>
#include<string>
#include<queue>
#include<algorithm>
#include<stdio.h>
#include<sstream>
#include<cmath>
#include<cctype>
#include<fstream>
#include<set>
#define mp(x,y) make_pair(x,y)
using namespace std;
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.in","w",stdout);
	int t;
	cin>>t;
	int u=1;
	while(t--)
	{
		int a,b,k;
		int x;
		int count=0;
		cin>>a>>b>>k;
		for(int i=0;i<a;++i)
		{
			for(int j=0;j<b;++j)
			{
				x=i&j;
				if(x<k)
					count++;
			}
		}
		cout<<"Case #"<<u++<<": "<<count<<endl;
	}
    return 0;
}


