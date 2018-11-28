#include <cstdio> //PROG: GCp2
#include <cstring>
#include <algorithm>
using std::sort;
#include <set>
typedef std::set<int> SET;
int main(){
	#ifdef JACK1_NOTEBOOK
	freopen("GCp2_in.txt","r",stdin);
	freopen("GCp2_out.h","w",stdout);
	#endif
	int N,M,TN,TI,i,j,k,ary[100][100];
	scanf("%d",&TN);
	for (TI=1;TI<=TN;TI++){
		SET S;
		scanf("%d%d",&N,&M);
		for (i=0;i<N;i++)
			for (j=0;j<M;j++){
				scanf("%d",ary[i]+j);
				S.insert(ary[i][j]);
			}
		bool okrow[100],okcol[100];
		memset(okrow,true,sizeof(okrow));
		memset(okcol,true,sizeof(okcol));
		while (!S.empty()){
			SET::iterator itr=S.end();
			int h=*(--itr);
			for (i=0;i<N;i++)
				for (j=0;j<M;j++)
					if (ary[i][j]==h)
						if (!okrow[i] && !okcol[j])
							goto OUTPUT;
			for (i=0;i<N;i++)
				for (j=0;j<M;j++)
					if (ary[i][j]==h){
						okrow[i]=false;
						okcol[j]=false;
					}
			S.erase(h);
		}
		OUTPUT:
		printf("Case #%d: %s\n",TI,S.empty()?"YES":"NO");
	}
}
