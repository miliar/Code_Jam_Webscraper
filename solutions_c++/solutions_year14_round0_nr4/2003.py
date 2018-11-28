#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
static int t,tt=1,n;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	while(t--){
		double tmp;
		scanf("%d",&n);
		set<double> naomi1,naomi2;
		set<double> ken1,ken2;
		for(int i=0;i<n;++i) {
			scanf("%lf",&tmp);
			naomi1.insert(tmp);
			naomi2.insert(tmp);
		}
		for(int i=0;i<n;++i) {
			scanf("%lf",&tmp);
			ken1.insert(tmp);
			ken2.insert(tmp);
		}
		int point1=0,point2=0,size=n;
		set<double>::iterator it,it2;
		while(n--){
			it=naomi2.begin();
			tmp=*it;
			it2=ken2.lower_bound(tmp);
			if(it2==ken2.end()) {
				point2++;
				it2=ken2.begin();
			}
				naomi2.erase(it);
				ken2.erase(it2);
		}
		while(size--){
			it=naomi1.end();
			it--;
			tmp=*it;
			it2=ken1.end();
			it2--;
			if(tmp>*it2){
			point1++;
			naomi1.erase(it);
			ken1.erase(it2);
			}
			else{
			 it=naomi1.begin();
			 naomi1.erase(it);
			ken1.erase(it2);
			}
			
		}
		printf("Case #%d: %d %d\n",tt,point1,point2);
		++tt;
	}
	return 0;
}