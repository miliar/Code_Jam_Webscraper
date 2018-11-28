using namespace std;
#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i = (a),_b = (b); i <= _b; ++i)
#define FORD(i,a,b) for(int i = (a),_b = (b); i >= _b; --i)


int ntest, n;
vector<int> v;

int main(){
	
	freopen("A-large.in","r",stdin);
	freopen("out","w",stdout);

	scanf("%d", &ntest);
	FOR(test,1,ntest){
		scanf("%d", &n);
		
		if(n <= 1) printf("Case #%d: %d %d\n",test,0,0);
			else
		{
		v.clear();
		FOR(i,1,n){
			int x;
			scanf("%d", &x);
			v.push_back(x);
		}
		int ans1 = 0, ans2 = 0, mm = v[0] - v[1];

		FOR(i,1,n-1){
			int dist = v[i] - v[i-1];
			mm = max(mm,-dist);
			if(dist < 0){
				ans1 += -dist;
			}
		}
		if(mm <= 0) ans2 = 0;else{
			int perten = mm;
			
			FOR(i,1,n-1){
				if(v[i-1] >= perten){
					ans2 += perten;
				}	else ans2 += v[i-1];
			}
		}
		printf("Case #%d: %d %d\n",test,ans1,ans2);
		}
	}

	return 0;
}

