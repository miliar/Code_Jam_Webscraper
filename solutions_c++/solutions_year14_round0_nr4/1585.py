#include<algorithm>
#include<set>
#include<deque>
using namespace std;

int n;
double ken[1111], naomi[1111];

int main(){
	freopen("D-large.in","r",stdin);
	freopen("D-large-output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int tc=1; tc<=t; tc++){
		scanf("%d",&n);
		for(int i=0; i<n; i++)
			scanf("%lf",naomi+i);
		for(int i=0; i<n; i++)
			scanf("%lf",ken+i);

		sort(ken,ken+n); sort(naomi,naomi+n);

		// DW
		int dw=0;
		deque<double> dq;
		for(int i=0; i<n; i++)
			dq.push_back(ken[i]);

		for(int i=0; i<n; i++){
			if(naomi[i] > dq.front()){
				dw++;
				dq.pop_front();
			}
			else{
				dq.pop_back();
			}
		}

		// W
		int w=0;
		set<double> kenSet;
		kenSet.insert(ken,ken+n);

		for(int i=0; i<n; i++){
			auto lb = kenSet.lower_bound(naomi[i]);
			if(lb == kenSet.end()){
				w++;
				kenSet.erase(kenSet.begin());
			}
			else{
				kenSet.erase(lb);
			}
		}

		printf("Case #%d: %d %d\n", tc, dw, w);
	}
}