#include <stdio.h>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <string>
using namespace std;

int n;
vector<int>ile;
int main() {
	int id=1;int t;scanf("%d",&t);
	while(t--) {
		scanf("%d", &n);
		ile.clear();
		for(int i=0;i<n;i++) 
		{ int s;
			scanf("%d",&s);
			ile.push_back(s);
			}
			
		sort(ile.begin(),ile.end());
		int res = ile[n-1];
		
		for(int i=1;i<res;i++) {
			int najedzenie = i;
			
			int ruchy = 0;
			for(int k=0;k<n;k++) {
				ruchy += (ile[k] + najedzenie-1) / najedzenie - 1;
			}
			res = min(res,ruchy+najedzenie);
		}
		
		
		// for(int i=0;i<res;i++) {
			// int dopodzialu = ile[ile.size()-1];
			// ile[ile.size()-1] = dopodzialu/2;
			// ile.push_back(dopodzialu - ile[ile.size()-1]);
			// sort(ile.begin(),ile.end());
			// ruchy++;
			// res = min(res,ruchy+ile[ile.size()-1]);
		// }
		printf("Case #%d: %d\n",id++,res);
	}
	return 0;
}
