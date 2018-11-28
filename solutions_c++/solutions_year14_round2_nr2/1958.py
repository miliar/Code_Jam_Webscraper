//shashwat001

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <utility>
#include <algorithm>
#include <cassert>

using namespace std;

#define INF 2147483647
#define LINF 9223372036854775807
#define mp make_pair
#define pb push_back

typedef long long int lli;
typedef pair<int,int> pi;

vector<int> getbitvector(int a)
{
	vector<int> v;
	int i = 0;
	while(a>0)
	{
		if(a&1)
		{
			v.pb(i);
		}
		i++;
		a = a>>1;
	}
	return v;
}

int main ()
{
	int t;
	scanf("%d",&t);
	for(int T = 1;T <= t;T++)
	{
		int a,b,k,i;
		scanf("%d %d %d",&a,&b,&k);
//	vector<int> va,vb,vk;
//	va = getbitvector(a);
//	vb = getbitvector(b);
//	vk = getbitvector(k);
//	reverse(va.begin(),va.end());
//	reverse(vb.begin(),vb.end());
//	reverse(vk.begin(),vk.end());
		int cnt = 0,j;
		for(i = 0;i < a;i++)
		{
			for(j = 0;j < b;j++)
			{
				if((i&j) < k)
				{
					//cout<<i<<" "<<j<<endl;
					cnt++;
				}
			}
		}
		printf("Case #%d: %d\n",T,cnt);
	}
	
	return 0;
}
