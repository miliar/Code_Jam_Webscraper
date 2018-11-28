#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<sstream>
#include<cstring>
using namespace std;

#define rep(i,n) for(int i=0;i<(n);i++)
#define rept(i,m,n) for(int i=(m);i<(n);i++)

int rmax[101],cmax[101];

int heights[101][101];

int main()
{
	int n,m,t;
	cin>>t;
	rep(tt,t)
	{			
		cin>>n>>m;
		rep(i,n) 
			rep(j,m) 
				cin>>heights[i][j];
		memset(rmax,0,sizeof(rmax));
		memset(cmax,0,sizeof(cmax));
		rep(i,n) {
			int currmax = 0;
			rep(j,m)
				currmax = max(currmax,heights[i][j]);
			rmax[i] = currmax;
		}
		rep(j,m) {
			int currmax = 0;
			rep(i,n)
				currmax = max(currmax,heights[i][j]);
			cmax[j] = currmax;
		}
		bool flag=true;
		rep(i,n) {
			rep(j,m) {
				if(heights[i][j]<rmax[i] && heights[i][j]<cmax[j]){
					flag=false;
					break;
				}
			}
			if(!flag)
				break;
		}
		printf("Case #%d: %s\n",tt+1,flag?"YES":"NO");		
	}	
	return 0;
}





