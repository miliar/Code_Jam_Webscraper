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
	freopen("B-large.in","r",stdin);
	freopen("out.in","w",stdout);
	int t;
	cin>>t;
	int u=1;
	while(t--)
	{
		vector<double>a;
		double b;
		double c,f,x;
		cin>>c>>f>>x;
		double rate=2.0;
		int i=0;
        a.push_back(x/rate);
		b=c/rate;
		rate+=f;
		while(1)
		{
			a.push_back(x/rate+b);
			b=c/rate+b;
			rate+=f;
			if(a[i]<a[i+1])
				break;
			i++;
		}
        cout<<"Case #"<<u++<<": "; 
		printf("%.7f\n",a[i]);
		a.clear();
	
	}
	return 0;
}
