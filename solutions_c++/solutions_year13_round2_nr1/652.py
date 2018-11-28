#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
#include<math.h>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<deque>
#include<sstream>
#include<iostream>
#include<stack>
#include<list>
using namespace std;

typedef vector<vector<int> > vii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long LL;

#define sz size()
#define all(n) n.begin(),n.end()
#define clr(a,n) memset(a,n,sizeof(a))
#define pb push_back
#define fo(i,j) for(int i=0;i<j;i++)

int A,N,arr[102],best[102][1000002];

int solve(int ind,int last)
{
	if(ind==N)return 0;
	
	if(best[ind][last]!=-1)return best[ind][last];
	
	int ret=N-ind;
	
	if(last>arr[ind])ret=min(ret,solve(ind+1,min(1000001,last+arr[ind])));
	else
	{
		if(last==1)return best[ind][last]=N;
		ret=min(ret,1+solve(ind,min(1000001,last+(last-1))));
	}
	
	return best[ind][last]=ret;
}

int main()
{
    freopen ("A-large.in","r",stdin);
    freopen ("output.out","w",stdout);
    
    int T,k=0;
    
    scanf("%d",&T);
    
    while(T--)
	{
		k++;
		clr(best,-1);
		
		scanf("%d %d",&A,&N);
		fo(i,N)scanf("%d",&arr[i]);
		
		sort(arr,arr+N);
		
		printf("Case #%d: %d\n",k,solve(0,A));
	}
    
    
}


































