#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<sstream>
using namespace std;
#define INF 2000000000
#define INFLL (1LL<<62)
#define SS ({int x;scanf("%d", &x);x;})
#define SSL ({lint x;scanf("%lld", &x);x;})
#define rep(i,n) for(int i=0;i<(n);i++)
#define rept(i,m,n) for(int i=(m);i<(n);i++)
#define ull unsigned long long
#define lint long long
#define MX 10000001

int height[128][128],rowMax[128],colMax[128];

int main()
{
	int i,j,n,m,t,testnum;
	t=SS;	
	for(testnum=1; testnum<=t; testnum++) {
		n=SS;
		m=SS;		
		for(i=0; i<n; ++i)
			for(j=0; j<m; ++j)
				height[i][j] = SS;
				
		//Calculate max height for each row	
		for(i=0; i<n; ++i) {
			int mx = 0;
			for(j=0; j<m; ++j)
				mx = max(mx,height[i][j]);
			rowMax[i] = mx;			
		}
		//Calculate max height for each column	
		for(j=0; j<m; ++j) {
			int mx = 0;
			for(i=0; i<n; ++i)
				mx = max(mx,height[i][j]);
			colMax[j] = mx;		
		}
		
		bool good = true;
		for(i=0; i<n; ++i) {
			for(j=0; j<m; ++j) {
				if(height[i][j]<rowMax[i] && height[i][j]<colMax[j]) {
					good = false;
					break;
				}				
			}
			if(!good)
				break;
		}
		printf("Case #%d: %s\n",testnum,good?"YES":"NO");
	}	
	return 0;
}





