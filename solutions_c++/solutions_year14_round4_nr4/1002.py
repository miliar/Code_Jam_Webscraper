#include <bits/stdc++.h>
#define mpr std::make_pair
#define lg std::__lg
#define __count __builtin_popcount
#define X first
#define Y second
#define mst(x) memset(x,0,sizeof(x))
#define mst1(x) memset(x,-1,sizeof(x))
#define ALL(c) (c).begin(),(c).end()
#define pb push_back
using namespace std;
typedef long long LL;
typedef double LD;
typedef vector<int> VI;
typedef std::pair<int,int> PII;
template<class T>inline void maz(T &a,T b){if(a<b)a=b;}
template<class T>inline void miz(T &a,T b){if(a>b)a=b;}
template<class T>inline T abs(T a){return a>0?a:-a;}
void RI() {}
template<typename... T>
void RI( int& head, T&... tail ) {
    scanf("%d",&head);
    RI(tail...);
}
const int N=1010;
int n,m;
char s[1001][13];
int line[N];
int Max,cnt;
int ans;
struct Node{
	Node*next[26];
	Node(){
		for(int i=0;i<26;i++)next[i]=0;
	}
}*root[10];
void insert(Node *now,char s[]){
	for(int i=0;s[i];i++){
		if(now->next[s[i]-'A']==NULL){
			now->next[s[i]-'A']=new Node();
			ans++;
		}
		now=now->next[s[i]-'A'];
	}
	
}
int solve(){
	ans=0;
	for(int i=0;i<n;i++)
		root[i]=new Node();
	for(int i=0;i<m;i++)
		insert(root[line[i]],s[i]);
	for(int i=0;i<n;i++)
		for(int j=0;j<26;j++)
			if(root[i]->next[j]!=NULL){
				ans++;
				break;
			}
	return ans;
}
void release(Node *now){
	for(int i=0;i<26;i++)
		if(now->next[i]!=NULL)release(now->next[i]);
	delete now;
}
void release(){
	for(int i=0;i<n;i++)
		release(root[i]);
}
void DFS(int now) {
	if(now == m){
		int tmp=solve();
		if(tmp > Max){Max=tmp;cnt=1;}
		else if(tmp==Max)cnt++;
		release();
		return;
	}
	for(int i=0;i<n;i++){
		line[now]=i;
		DFS(now+1);
	}
}
int main(){
	int T;
	RI(T);
	int w=1;
	while(T--){
		Max=0;cnt=0;
		RI(m,n);
		for(int i=0;i<m;i++)
			scanf("%s",s[i]);
		DFS(0);
		printf("Case #%d: %d %d\n",w++,Max,cnt);
	}
	return 0;
}

