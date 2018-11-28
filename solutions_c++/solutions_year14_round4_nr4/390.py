#include <cstdio>
#include <cstring>

char s[11][11];
int pos[11];

struct TrieNode{
	TrieNode* children[26];
	TrieNode(){
		memset(children,0,sizeof(children));
	}
	~TrieNode(){
		for(int i=0;i<26;i++){
			if(children[i])
				delete children[i];
		}
	}
	void insert(const char* key){
		if(*key==0)
			return ;
		int next = *key-'A';
		if(children[next]==NULL){
			children[next] = new TrieNode();
		}
		children[next]->insert(key+1);
	}
	int count(){
		int ret=0;
		for(int i=0;i<26;i++){
			if(children[i])
				ret += children[i]->count();
		}
		return ret+1;
	}
};

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,ti,m,n,i,cnt,ans,anscnt=0;
	scanf("%d",&t);
	for(ti=1;ti<=t;ti++){
		scanf("%d%d",&m,&n);
		for(i=0;i<m;i++){
			scanf("%s",s[i]);
			pos[i]=0;
		}
		pos[i]=0;

		ans=anscnt=0;
		while(true){
			TrieNode head[4];
			for(i=0;i<m;i++){
				head[pos[i]].insert(s[i]);
			}
			cnt=0;
			for(i=0;i<n;i++){
				int tmp = head[i].count();
				if(tmp!=1)
					cnt+=tmp;
			}
			if(ans<cnt){
				ans=cnt;
				anscnt=1;
			}else if(ans==cnt){
				anscnt++;
			}



			pos[0]++;
			for(i=0;i<m;i++){
				if(pos[i]==n){
					pos[i]=0;
					pos[i+1]++;
				}
			}
			if(pos[m]!=0)
				break;
		}
		printf("Case #%d: %d %d\n",ti,ans,anscnt);
	}
}