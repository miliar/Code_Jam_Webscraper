#include <bits/stdc++.h>
using namespace std;
const int limit = 1000 + 5;
double naomi[limit], ken[limit];
int f[limit][limit];
int n;

int War(){
	int result = 0;
	set<double> Ken(ken, ken+n);
	//cout << Ken.size() << endl;
	//for(auto x: Ken) cout << x << " "; cout << endl;
	for(int i = 0; i < n; ++i){
		auto p = Ken.upper_bound(naomi[i]);
		if (p == Ken.end()) {
			result++;
			Ken.erase( Ken.begin() );
		} else Ken.erase(p);
	}
	return result;
}

int DeceifulWar(){
	int first_naomi = 0, last_naomi = n-1;
	int first_ken = 0, last_ken = n-1;
	int result = 0;
	while (first_ken <= last_ken){
		if (ken[last_ken] < naomi[last_naomi]) {
			result++;
			last_naomi--;
		} else first_naomi++;
		last_ken--;
	}
			
	return result;
}

int deceifulWar(int dau=0, int cuoi=n-1, int front=0, int rear=n-1){
	if (dau > cuoi) return 0;
	if (f[dau][cuoi] != -1) return f[dau][cuoi];
	
		
	int k = (naomi[dau] < ken[rear]) ? 
			deceifulWar(dau+1,cuoi,front,rear-1) : deceifulWar(dau+1,cuoi,front+1,rear)+1;
	int t = (naomi[cuoi] > ken[rear]) ? 
			deceifulWar(dau,cuoi-1,front+1,rear)+1 : deceifulWar(dau,cuoi-1,front,rear-1);
	f[dau][cuoi] = max(k,t);
	
	//printf("%d %d %d\n",dau,cuoi,f[dau][cuoi]);
	return f[dau][cuoi];
	
}

int main(){
	freopen("file.inp","r",stdin);
	freopen("sol.txt","w",stdout);
	int test; scanf("%d",&test);
	for(int num = 1; num <= test; ++num){
		scanf("%d",&n);
		for(int i = 0; i < n; ++i) scanf("%lf",naomi + i);
		for(int i = 0; i < n; ++i) scanf("%lf",ken + i);
		
		sort(naomi, naomi+n);
		sort(ken, ken+n);
		//for(int i = 0; i < n; ++i) printf("%.3f ", naomi[i]); printf("\n");
		//for(int i = 0; i < n; ++i) printf("%.3f ", ken[i]); printf("\n");
		
		memset(f,-1,sizeof f);
		printf("Case #%d: %d %d\n",num,DeceifulWar(), War());
	}

}

