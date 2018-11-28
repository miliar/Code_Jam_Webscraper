									/*	In the name of God	*/
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
#include <sstream>
#include <bitset>
#include <map>
#include <set>
#include <queue>
#include <stack>

#define rep(i,n) for((i)=0;(i)<(n);(i)++)
typedef long long ll;

using namespace std;

int n,m,a[1001][1001];

int findmin(){
	int i,j,r=100;
	rep(i,n)
		rep(j,m)
			if (a[i][j])
				r=min(r,a[i][j]);
	return r;
}

int main(){
	
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);	

	int ti,tc,i,j,x;
	scanf("%d",&tc);
	rep(ti,tc){
		scanf("%d %d",&n,&m);
		rep(i,n)
			rep(j,m)
				scanf("%d",&a[i][j]);
		bool f=1;
		while (f && (x=findmin())!=100){
			f=0;
			rep(i,n){
				int y=0;
				rep(j,m){
					y=max(y,a[i][j]);
					if (a[i][j] && a[i][j]!=x)
						break;
				}
				if (y && j==m){
					f=1;
					rep(j,m)
						a[i][j]=0;
				}
			}
			rep(j,m){
				int y=0;
				rep(i,n){
					y=max(y,a[i][j]);
					if (a[i][j] && a[i][j]!=x)
						break;
				}
				if (y && i==n){
					f=1;
					rep(i,n)
						a[i][j]=0;
				}
			}
		}
		if (f)
			printf("Case #%d: YES\n",ti+1);
		else
			printf("Case #%d: NO\n",ti+1);
	}

	return 0;
}