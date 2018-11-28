#include <stdio.h>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <string>
using namespace std;

#define PB push_back
typedef long double LD;
vector<int> sizes;
int s,n;
int main() {
	int id=1;int t;scanf("%d",&t);
	while(t--) {
		scanf("%d%d",&n,&s);
		sizes.clear();
		for(int i=0;i<n;i++) {
		int a;scanf("%d",&a);
		sizes.PB(a);
		}
		sort(sizes.begin(),sizes.end(),greater<int>());
		
		int ost = n-1;
		int res = 0;
		for(int i=0;i<n;i++) {
			if(i<ost) {
				// probuj dwa
				if(s >= sizes[i] + sizes[ost]) {
					ost--;
				}
				res++;
			}
			else if(i<=ost) {
				res++;
				break;
			}
		}
		
		printf("Case #%d: %d\n",id++,res);
		
	}
	return 0;
}
