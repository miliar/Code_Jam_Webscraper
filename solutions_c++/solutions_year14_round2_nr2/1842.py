#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<utility>
#include<vector>
#include<queue>
#include<stack>

#define ll long long int

using namespace std;

template<class T> void findMax(T &m, T x){m=m>x?m:x;}
template<class T> void findMin(T &m, T x){m=m<x?m:x;}
const double pi=acos(-1);
int main()
{
	//ios::sync_with_stdio(false);
	int t,z;
	ll a,b,k,i,j,c;
	scanf("%d", &t);
	for(z=1;z<=t;z++)
	{
		cin>>a>>b>>k;
		c=0;
		for(i=0;i<a;i++)
			{
				for(j=0;j<b;j++)
				{
					if((i&j)<k)
						c++;
				}
			}
		cout<<"Case #"<<z<<": "<<c<<endl;
	}
	return 0;
}
