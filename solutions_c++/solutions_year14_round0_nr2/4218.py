#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <iomanip>

using namespace std;

int tt,t;
long double c,f,x,ans,cur,tim;

int main()
{
	//ios_base::sync_with_stdio(false);
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	cin>>t;
	for (tt=1; tt<=t; tt++)
	{
		cin>>c>>f>>x;
		ans=0.;
		cur=2.;
		ans=x/cur;
		tim=0.;
		while (1)
		{
			tim=tim+c/cur;
			cur=cur+f;
			if (tim+x/cur>=ans) break;
			ans=tim+x/cur;
		}
		cout<<"Case #"<<tt<<": ";
		cout.precision(30);
		cout<<ans<<endl;
	}
	return 0;
}


