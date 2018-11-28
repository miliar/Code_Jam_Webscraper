#include <cstdio>
#include <cstring>
#include <map>
#include <stack>
#include <vector>
#include <algorithm>
using namespace std;

const int MAXN = 1e9+10;
const int MAXM = 1005;

typedef pair<int,int> ii;

vector<ii> run;
vector<int> arr_dist;
long long ans,ans_true,tmp;

long long sum(int n,int k){
	long long ans = n + (n-k+1);
	return ans*k/2;
}

int o[MAXM],e[MAXM],p[MAXM];
int T,N,M;

int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-output0.out","w",stdout);
	
	scanf("%d",&T);
	for(int _i=1;_i<=T;_i++){
		arr_dist.clear();
		run.clear();
		printf("Case #%d: ",_i);
		
		ans = ans_true = 0;
		
		
		scanf("%d %d",&N,&M);
		for(int i=1;i<=M;i++){
			scanf("%d %d %d",&o[i],&e[i],&p[i]);
			tmp = p[i];
			tmp *= sum(N,e[i]-o[i]);
			ans_true += tmp;
			
			run.push_back(ii(o[i],-p[i]));	// -  =  start
			run.push_back(ii(e[i],+p[i]));
		}
		sort(run.begin(),run.end());
		//arr_dist.erase(unique(arr_dist.begin(),arr_dist.end()),arr_dist.end());
		
		stack <ii> S;
		ans = 0;
		for(int i=0;i<run.size();i++){
			//printf("[%d,%d]\n",run[i].first,-run[i].second);
			if(run[i].second < 0){ // plus
				S.push(ii(run[i].first,-run[i].second));
			}else{	// minus
				int valnow = run[i].second;
				while(!S.empty() && S.top().second < valnow){
					tmp = S.top().second;
					tmp *= sum(N,run[i].first-S.top().first);
					
					valnow -= S.top().second;
					S.pop();
					ans += tmp;
				}
				ii tmp_stack = S.top();
				tmp_stack.second -= valnow;
				
				tmp = valnow;
				tmp *= sum(N,run[i].first-S.top().first);
				//printf("sum += (%d,%d) 	[%lld] \n",S.top().first,run[i].first,sum(N,run[i].first-S.top().first));
				ans += tmp;
				
				S.pop();
				S.push(tmp_stack);
				valnow = 0;
			}
		}
		
		printf("%lld\n",ans_true-ans);
	}
	return 0;
}