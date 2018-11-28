#include <stdio.h>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <string>
using namespace std;

#define PB push_back

#define INF 1000000000
typedef long double LD;
vector<int> sizes;
int s,n;

int kosztPorzadku(int a, int b, int mno, int maks) {
	int res = 0;
	for(int i=a;i<b;i++) {
		for(int i2=i+1;i2<b;i2++) if(i2!=i && sizes[i] != maks && sizes[i2] != maks ){
			res += mno ^ (sizes[i]>sizes[i2]);
		}
	}
	return res;
}
int zyje[2000];
int main() {
	int id=1;int t;scanf("%d",&t);
	while(t--) {
		scanf("%d",&n);
		sizes.clear();
		
		for(int i=0;i<n;i++) {
		int a;scanf("%d",&a);
		sizes.PB(a);
		zyje[i] = 1;
		}
		
		int res = 0;
		for(int i=0;i<n;i++) {
			int index = min_element(sizes.begin(),sizes.end())-sizes.begin();
			int best = INF;
			int lewy = 0;
			for(int i2=0;i2<index;i2++) if(sizes[i2] != INF) {
				lewy++;
			}	
			int prawy = 0;
			for(int i2=index+1;i2<n;i2++) if(sizes[i2] != INF) {
				prawy++;
			}	
			best = min (lewy,prawy);
			sizes[index] = INF;
			res += best;
		}
		/*
		int index = max_element(sizes.begin(),sizes.end())-sizes.begin();
		
		int res = INF;
		for(int i=0;i<=n;i++) {
			int newres = abs(i - index) + (i>index ? -1 : 0);
			//printf("res = %d\n",newres);
			newres += kosztPorzadku(0,i,0,sizes[index]);
			//printf("res = %d\n",newres);
			newres += kosztPorzadku(i,n,1,sizes[index]);
			//printf("res = %d\n\n",newres);
			res = min(res,newres);
		}*/
		printf("Case #%d: %d\n",id++,res);
		
	}
	return 0;
}
