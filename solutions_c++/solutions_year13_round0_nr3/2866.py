#include <iostream>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cmath>
#include <vector>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <string>
#define SET(p) memset(p,-1,sizeof(p))
#define CLR(p) memset(p,0,sizeof(p))
#define LL long long int
#define ULL unsigned long long int
#define S(n)					scanf("%d",&n)
#define Sl(n)					scanf("%lld",&n)
#define Sf(n) 					scanf("%lf",&n)
#define Ss(n) 					scanf("%s",n)
using namespace std;
LL indices[1000010];
LL values[1000010]; 
int end;
bool ispalin(LL a)
{
	LL rev=0;
	LL t=a;
	while(t>0)
	{
		rev=rev*10+(t%10);
		t/=10;
	}
	return rev==a;
}
void prep()
{
	int i,j,k;
	indices[0]=0;
	values[0]=0;
	indices[1]=1;
	values[1]=1;
	j=2;
	for(i=2;i<=10000010;i++)
	{
		if(ispalin(i)&&ispalin(i*i))
		{
			indices[j]=i*i;
			values[j]=values[j-1]+1;
			j++;
		}
	}
	end=j;
}

int main()
{
	int i,j,k,l,m,n,t;
	#ifndef ONLINE_JUDGE
	freopen("test3.in","r",stdin);
	freopen("op3.txt","w",stdout);
	#endif
	prep();
	S(t);
	k=1;
	while(t--)
	{
		LL a, b;
		Sl(a),Sl(b);
		i=lower_bound(indices,indices+end,a)-indices;
		if(binary_search(indices,indices+end,b))
		{
			j=lower_bound(indices,indices+end,b)-indices;
		}
		else
		j=upper_bound(indices,indices+end,b)-1-indices;
		//cout<<i<<" "<<j<<endl;
		printf("Case #%d: %d\n",k++,max(j-i+1,0));
		
		
	}
	return 0;
}
