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

int arr[10005];
bool taken[10005];

int main()
{
    freopen ("A-large.in","r",stdin);
    freopen ("output.out","w",stdout);
    
    int T,k=0;
    
    scanf("%d",&T);
    
    while(T--)
    {
		k++;
		clr(taken, 0);
		int N,X,ret=0;
		scanf("%d %d",&N,&X);
		
		fo(i,N)
			scanf("%d",&arr[i]);
		
		sort(arr,arr+N);
		
		for(int i=N-1;i>=0;i--)
		{
			if(taken[i])continue;
			taken[i] = 1;
			
			int ind = upper_bound(arr, arr+N, X-arr[i]) - arr - 1;
			
			while(ind>=0 && taken[ind])ind--;
			if(ind>=0)taken[ind]=1;
			
			ret++;
		}
		
		printf("Case #%d: %d\n",k,ret);
	}
    
}


































