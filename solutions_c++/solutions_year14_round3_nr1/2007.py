#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <set>
#include <cstdio>
#define LL long long
using namespace std;
LL  gcd(LL a,LL b)
{
    while(a!=b)
    {
		if(a>b)a-=b;
        else b-=a;
	}
	return a;
}
int main()
{
	freopen("C:\\Users\\Balasubramanian\\Downloads\\A-small-attempt0.in", "r", stdin);
    freopen("C:\\Users\\Balasubramanian\\Desktop\\C++progs\\outputa1.out", "w", stdout);
	LL t;char c;
	cin>>t;
	for (LL c=1;c<=t;++c)
	{
	
		LL p,q;char c1;
		cin>>p;cin>>c1;cin>>q;
			cout<<"Case #"<<c<<": ";
		LL hcf=gcd(p, q);
		p/=hcf;
		q/=hcf;
		
		if(q&(q-1))
		{
		cout<<"impossible"<<endl;
			continue;
		}
		else
		{
	cout<<ceil(log2((double)q/p))<<endl;
		}
	}
 
	return 0;
}
