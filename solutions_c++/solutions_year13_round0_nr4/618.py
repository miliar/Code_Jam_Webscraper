#include <cstdio> //PROG: GCp4
#include <cstring>
#include <algorithm>
using std::sort;
int key[100]={};
struct Box{
	int need,got[100],M;
	void input(){
		memset(got,0,sizeof(got));
		M=0;
		int i,n;
		scanf("%d%d",&need,&n);
		while (n--){
			scanf("%d",&i);
			if (M<i)M=i;
			got[i]++;
		}
	}
	void print(){
		printf("Box need %3d, got : ",need);
		int i;
		for (i=1;i<=M;i++) if (got[i]){
			printf("%3d",i);
			if (got[i]>1)
				printf("*%d",got[i]);
		}
		putchar('\n');
	}
	bool open(){
		if (key[need]==0){
			return false;
		}
		int i;
		key[need]--;
		for (i=1;i<=M;i++)
			if (got[i])
				key[i]+=got[i];
		return true;
	}
	void close(){
		int i;
		key[need]++;
		for (i=1;i<=M;i++)
			if (got[i])
				key[i]-=got[i];
	}
}box[500];
bool used[100],found;
int solve[100];
void dfs(int x,int n,int m){
	//printf("trybox%d\n",x);
	if (!box[x].open())return;
	used[x]=true;
	solve[n]=x;
	//printf("open box[%d] as solve[%d]/%d\n",x,n,m);
	if (n+1==m){
		found=true;
		return;
	}
	int i,j;
	
	
	//cut
	
	int g=box[x].need,p=0,h;
	if (key[g]==0){
		for (i=1;i<=m;i++)
			if (!used[i] && box[i].need==g)
				p++;
		///*
		if (p>0){
			h=0;
			for (i=1;i<=m;i++)
				if (!used[i] && box[i].need!=g)
					h+=box[i].got[g];
			if (h==0)
				goto CUTED;
		}
		//*/
	}
	
	
	//dfs
	for (i=1;i<=m;i++)
		if (!used[i]){
			dfs(i,n+1,m);
			if (found)return;
		}
	
	CUTED:
	box[x].close();
	used[x]=false;
}
int main(){
	#ifdef JACK1_NOTEBOOK
	freopen("GCp4_in.txt","r",stdin);
	freopen("GCp4_out.h","w",stdout);
	#endif
	int TN,N,K,TI,i,j,k;
	scanf("%d",&TN);
	for (TI=1;TI<=TN;TI++){
		scanf("%d%d",&K,&N);
		memset(key,0,sizeof(key));
		memset(used,0,sizeof(used));
		int nned[100]={};
		for (i=0;i<K;i++){
			scanf("%d",&j);
			key[j]++;
		}
		for (i=1;i<=N;i++)
			box[i].input();
		
		//tester
		found=false;
		for (i=1;i<=N;i++){
			nned[box[i].need]--;
			for (j=1;j<=box[i].M;j++)
				nned[j]+=box[i].got[j];
		}
		for (i=0;i<100;i++)
			if (key[i]+nned[i]<0)
				goto OUTPUT;
		
		for (i=1;i<=N;i++){
			dfs(i,0,N);
			if (found)
				break;
			//puts("===");
		}
		
		OUTPUT:
		fprintf(stderr,"testdata#%3d done.\n",TI);
		if (found){
			printf("Case #%d:",TI);
			for (i=0;i<N;i++)
				printf(" %d",solve[i]);
			putchar('\n');
		}else printf("Case #%d: IMPOSSIBLE\n",TI);
	}
}
