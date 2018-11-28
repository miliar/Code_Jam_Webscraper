
#include <cstdio>
#include <algorithm>
#include <utility>
#include <vector>
using std::max;
using std::sort;
using std::vector;
using std::pair;
using std::make_pair;

typedef pair<int,int> PII;

int n,m;
int d[110][110];
int s[110][110];
int row[110],col[110];
vector<PII> ans;


int main()
{
	int t,cs=0;
	scanf("%d",&t);
	while(cs++<t){
	
		ans.clear();
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;++i)for(int j=0;j<m;++j){
			scanf("%d",d[i]+j);
		}

		//collect answers for each row
		for(int i=0;i<n;++i){
			int t=0;
			for(int j=0;j<m;++j) t = max(t,d[i][j]);
			row[i]=t;	
			ans.push_back(make_pair(t,i*2));
		}

		//collect answers for each column 
		for(int i=0;i<m;++i){
			int t=0;
			for(int j=0;j<n;++j) t = max(t,d[j][i]);
			col[i]=t;	
			ans.push_back(make_pair(t, i*2+1));
		}

		sort(ans.begin(), ans.end());
		//for(int i=0;i<ans.size();++i)	
		//	printf("%s %d:%d\n", ans[i].second%2 ? "col":"row",
		//	ans[i].second>>1, ans[i].first);

		for(vector<PII>::reverse_iterator rit=ans.rbegin();
			rit!=ans.rend(); ++rit){
			// is column?
			if(rit->second%2){
				for(int i=0;i<n;++i) s[i][ rit->second >> 1]=rit->first;
			}
			else{// is row?
				for(int i=0;i<m;++i) s[ rit->second >> 1][i]=rit->first;
			}
		}

		//for(int i=0;i<n;++i)for(int j=0;j<m;++j){
		//	printf("%d ", s[i][j]);
		//	if(j==m-1)puts("");
		//}

		bool ok=true;
		for(int i=0;i<n;++i)for(int j=0;j<m;++j){
			if(s[i][j] != d[i][j]){ok=false;break;}
		}

		printf("Case #%d: %s\n", cs, ok?"YES":"NO");
	
	}


	return 0;
}
