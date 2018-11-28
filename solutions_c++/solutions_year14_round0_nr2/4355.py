#include <iostream>
#include <vector>
#include <algorithm> 
#include <set>
#include <fstream>
#include <iomanip> 

typedef long double lld;
typedef long long ll;

using namespace std;

double R=2.0;

ifstream in("B-large.in"); ofstream out("b.out");
ll T, l=1;

ll optimalN(lld C, lld F, lld X)
{
	ll result = (ll)((X*F-C*R)/(F*C));
	return (result<0) ? 0 : result;
}

lld CC(lld C, lld F, ll n)
{
	if(n==0) return 0.0;
	else return (C/(R+(n-1)*F));
}


lld totalTime(lld C, lld F, lld X, ll n)
{
	lld result=0.0;
	for(ll i=0;i<=n;i++) result+=CC(C,F,i);
	result+=X/(R+n*F);
	return result;
}

int main()
{
	in>>T;
	while(T--)
	{
		lld C,F,X;
		in>>C>>F>>X;
		lld result = totalTime(C,F,X,optimalN(C,F,X));
		out<<fixed<<setprecision(7)<<"Case #"<<l<<": "<<result<<endl;
		l++;
		
	}
}

