#include"stdio.h"
#include"vector"
using namespace std;
#define FOREACH(it,v) for(typeof(v.begin()) it = v.begin(); it != v.end(); it++)
int main(){
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++){
		int n,m;
		scanf("%d%d",&n,&m);
		int count[n+m];
		vector<int> inps[101];
		int a;
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				scanf("%d",&a),
				inps[a].push_back((i<<10)|j);
		for(int i=0;i<n+m;i++)count[i]=0;
		bool final=1;
		for(int x=1;x<101;x++){
			FOREACH(it,inps[x])
				count[(*it)&1023]++,
				count[m+((*it)>>10)]++;
			FOREACH(it,inps[x])
				final &= count[m+((*it)>>10)]==m||count[(*it)&1023]==n;
		}
		printf("Case #%d: %s\n",t+1,final?"YES":"NO");
	}
}
