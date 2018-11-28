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
double dp[205][408];
const int off=201;
double prob[205];
/*void make_false(int N,int K)
{
	for(int i=0;i<=N;i++)
		for(int j=0;j<=K;j++)
		{
			for(int k=0;k<40;k++)
			{
				dp[i][j][k]=-1.0;
			}
		}
}*/
void make_false(int N)
{
	for(int i=0;i<=N;i++)
	{
			for(int k=0;k<408;k++)
			{
				dp[i][k]=-1.0;
			}
	}
}
double getans(int N,int need)
{
	if(N==0)
	{
		if(need==0)
			return 1.0;
		else
			return 0.0;
	}
	if(dp[N][off+need]>-.5)
	{
		return dp[N][off+need];
	}
	dp[N][need+off]=prob[N]*getans(N-1,need-1)+(1-prob[N])*getans(N-1,need+1);
	return dp[N][need+off];
}
/*
double getans(int N,int K,int need)
{
	if()
	{

	}
	if(dp[N][K][off+need]>-.5)
	{
		return dp[N][K][off+need];
	}
	double a1=getans(N-1,K-1,need-1);
	double a2=prob[N]*getans(N-1,K)
}*/
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("Bout.txt","w",stdout);
    int T;
    cin>>T;
    double p[205];
    for(int t=1;t<=T;t++)
    {
    	int N,K;
    	cin>>N>>K;
    	for(int i=0;i<N;i++)
    		cin>>p[i];
    	int arr[20]={0};
    	for(int i=0;i<K;i++)
    		arr[i]=1;
    	reverse(arr,arr+N);
    	double mx=0.0;
    	//cout<<N<<endl;
    	do
    	{
    		make_false(N);
    		int cnt=0;
    		for(int i=0;i<N;i++)
    		{
    			if(arr[i])
    			{
    				prob[cnt+1]=p[i];
    				cnt++;
    			}
    			//cout<<arr[i]<<" ";
    		}
    		//cout<<endl;
    		double val=getans(K,0);
    		//cout<<val<<endl;
    		mx=max(mx,val);
    	}while(next_permutation(arr,arr+N));
    	printf("Case #%d: %.10lf\n",t,mx);
    }
    return 0;
}