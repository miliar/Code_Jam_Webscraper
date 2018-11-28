#include<vector>
#include<string>
#include<algorithm>
#include<iostream>
#include <iomanip>
#include<cmath>
#include<cstdlib>
#include<cstdio>
#include<stack>
#include<cstring>
#include<map>
#include<set>
using namespace std;
#define MOD 1000000007
int main()
{
	int t,T;
	double C,F,X;
	double re;
	double ttime,ttime2;
	double per;
	freopen("B-large.in","rt",stdin);
	freopen("B.out","wt",stdout);
	cin>>T;
	for(t=1;t<=T;t++)
	{
		cin>>C>>F>>X;
		re=X/2;
		per=2;
		ttime=0;
		while(1)
		{
			ttime+=C/per;
			per+=F;
			ttime2=ttime+X/per;
			if(ttime2>re)
				break;
			else
				re=ttime2;
		}
		cout<<"Case #"<<t<<": "<<setiosflags(ios::fixed)<<setprecision(7)<<re<<endl;
	}
    return 0;
}