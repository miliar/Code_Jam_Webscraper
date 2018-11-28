#include <cstdio>

int T,N;
int vertex[1080];
int slen[308];
char sentences[308][1008][18];
int wlen=0;
char words[2008][18];
int esum[6008];
int to[6008][2008];
int rev[6008][2008];
int cap[6008][2008];
int visited[6008];
int fromv[6008];
int que[9999];
void init(void) {
	for(int i=0;i<6008;i++) {
		esum[i]=0;
		visited[i]=-1;
	}
}
void add_edge(int fr_v,int to_v,int cap_v) {
	to[fr_v][esum[fr_v]]=to_v;
	rev[fr_v][esum[fr_v]]=esum[to_v];
	cap[fr_v][esum[fr_v]]=cap_v;
	esum[fr_v]++;
	to[to_v][esum[to_v]]=fr_v;
	rev[to_v][esum[to_v]]=esum[fr_v]-1;
	cap[to_v][esum[to_v]]=0;
	esum[to_v]++;
}
int max_f(int s,int t) {
	int sol=0;
	while(1) {
		//printf("%d\n",sol);
		int qst=0;
		int qls=1;
		que[0]=s;
		visited[s]=sol;
		while(qst<qls) {
			int now=que[qst];
			for(int i=0;i<esum[now];i++) {
				if(cap[now][i]>0&&visited[to[now][i]]!=sol) {
					visited[to[now][i]]=sol;
					fromv[to[now][i]]=rev[now][i];
					que[qls++]=to[now][i];
				}
			}
			qst++;
		}
		if(visited[t]!=sol) return sol;
		sol++;
		int now=t;
		while(1) {
			//printf("now:%d\n",now);
			int fromvertex=to[now][fromv[now]];
			cap[now][fromv[now]]++;
			cap[fromvertex][rev[now][fromv[now]]]--;
			now=fromvertex;
			if(now==s) break;
		}
	}
}
int main() {
	scanf("%d",&T);
	for(int ts=1;ts<=T;ts++) {
		scanf("%d",&N);
		char rds='\0';
		while(rds!='\n') scanf("%c",&rds);
		for(int i=0;i<N;i++) {
			slen[i]=0;
			while(1) {
				int cn=0;
				int sentend=0;
				while(1) {
					scanf("%c",&rds);
					if(rds>='a'&&rds<='z') {
						sentences[i][slen[i]][cn++]=rds;
					}
					if(rds==' '||rds=='\n') {
						sentences[i][slen[i]][cn]='\0';
						if(rds=='\n') sentend=1;
						break;
					}
				}
				slen[i]++;
				if(sentend) break;
			}
		}
		wlen=0;
		for(int i=0;i<N;i++) {
			//printf("%d\n",slen[i]);
			for(int j=0;j<slen[i];j++) {
				//printf("%s\n",sentences[i][j]);
				int found=0;
				for(int k=0;k<wlen;k++) {
					int iseq=1;
					int x=0;
					while(sentences[i][j][x]!='\0'&&words[k][x]!='\0') {
						if(sentences[i][j][x]!=words[k][x]) iseq=0;
						x++;
					}
					if(sentences[i][j][x]!='\0'||words[k][x]!='\0') iseq=0;
					if(iseq) found=1;
				}
				if(found==0) {
					int x=0;
					while(1) {
						words[wlen][x]=sentences[i][j][x];
						if((int)sentences[i][j][x]==0) break;
						x++;
					}
					wlen++;
				}
			}
		}
		init();
		//start=4001 end=4002
		int INF=2015;
		add_edge(4001,4500,INF);
		add_edge(5001,4002,INF);
		for(int i=0;i<wlen;i++) {
			add_edge(i,2000+i,1);
			add_edge(2000+i,i,INF);
		}
		for(int i=0;i<N;i++) {
			add_edge(4500+i,5000+i,INF);
			add_edge(5000+i,4500+i,INF);
			for(int j=0;j<slen[i];j++) {
				for(int k=0;k<wlen;k++) {
					int iseq=1;
					int x=0;
					while(sentences[i][j][x]!='\0'&&words[k][x]!='\0') {
						if(sentences[i][j][x]!=words[k][x]) iseq=0;
						x++;
					}
					if(sentences[i][j][x]!='\0'||words[k][x]!='\0') iseq=0;
					if(iseq) {
						add_edge(4500+i,k,INF);
						add_edge(2000+k,5000+i,INF);
					}
				}
			}
		}
		printf("Case #%d: %d\n",ts,max_f(4001,4002));
	}
	return 0;
}
