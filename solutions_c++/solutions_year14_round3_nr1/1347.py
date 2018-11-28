#include <iostream>
#include <iomanip>
#include <cmath>
#include <list>
#include <stack>
#include <queue>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
long long Gcd(long long n1,long long n2)
{
	if(n2==0)return n1;
	return Gcd(n2,n1%n2);
}

int main()
{
	//freopen("a.in","r",stdin);
	//freopen("a.out","w",stdout);
	char ch;
	int cases;
	long long p,q,gcd,po2,po3,po[50];
	po[0]=1;
	for(int i=1;i<=40;i++)
	{
		po[i]=po[i-1]*2;
	}
	cin>>cases;
	for(int kase=1;kase<=cases;kase++)
	{
		cin>>p>>ch>>q;
		gcd=Gcd(q,p);
		p/=gcd;
		q/=gcd;
		po2=log10l(q)/log10l(2);
		cout<<"Case #"<<kase<<": ";
		if(q!=po[po2])
		{
			cout<<"impossible\n";
			continue;
		}
		po3=log10l(p)/log10l(2);
		po2-=po3;
		if(po2==0)po2++;
		cout<<po2<<"\n";
	}
	return 0;
}