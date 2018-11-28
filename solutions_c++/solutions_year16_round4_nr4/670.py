#include <iostream>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <sstream>
#include <limits>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <cctype>
#include <queue>
#include <deque>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <map>
#include <set>
#define PI (acos(-1.0))
#define Abs(a) (((a)<0) ? (-(a)) :(a) )
#define rep(i,n) for((i)=0;(i)<(n);(i)++)
#define Rep(i,n) for(int i=0;i<(n);i++)
#define Rrep(i,n) for(int i=((n)-1);i>=0;i--)
#define rrep(i,n) for((i)=(n)-1;(i)>=0;(i)--)
#define Pii pair<int,int>
#define PB push_back
#define Size(x) ((int)(x.size()))
using namespace std;
typedef long long mint;
typedef unsigned long long umint;
string know[5];
bool check(const int *workers,const string *tmp,bool *taken,int n,int ccur)
{
	if(ccur==n)
		return true;
	int cur=workers[ccur];
	bool ok=true;
	int i;
	bool nf=true;
	for(i=0;i<n;i++)
	{
		if(tmp[cur][i]=='1'&&!taken[i])
		{
			nf=false;
			taken[i]=true;
			ok=check(workers,tmp,taken,n,ccur+1);
			if(!ok)
				return false;
			taken[i]=false;
		}
	}
	if(nf)
	{
		return false;
	}
	return true;
}
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("Dout.txt","w",stdout);
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
    	int n;
    	int mnc=1000;
    	cin>>n;
    	for(int i=0;i<n;i++)
    		cin>>know[i];
    	int val=n*n;
    	for(int i=0;i<(1<<val);i++)
    	{
    		string tmp[4];
    		bool ok=true;
    		int cost=0;
    		for(int j=0;j<n;j++)
    		{
    			tmp[j]=know[j];
    			for(int jj=0;jj<n;jj++)
    			{
    				int cur=(1<<(j*n+jj));
    				if((i&cur)&&know[j][jj]=='1')
    				{
    					ok=false;
    					break;
    				}
    				if((i&cur))
    				{
    					cost++;
    					tmp[j][jj]='1';
    				}
    			}
    			if(!ok)
    				break;
    		}
    		if(!ok)
    			continue;
    		int workers[4]={0};
    		for(int j=0;j<n;j++)
    			workers[j]=j;
    		do
    		{
    			bool taken[4]={false};
    			ok=check(workers,tmp,taken,n,0);
    			if(!ok)
    				break;
    		}while(next_permutation(workers,workers+n));
    		if(!ok)
    			continue;
    		mnc=min(mnc,cost);
    	}
    	printf("Case #%d: %d\n",t,mnc);
    }
    return 0;
}