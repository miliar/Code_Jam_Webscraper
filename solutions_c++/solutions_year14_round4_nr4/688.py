#include <iostream>
#include <string>
using namespace std;
const int maxn=1000;
struct Node{
		int son[26];
		void clear(){
			memset(son,0,sizeof(son));
		}
} tree[maxn],root[5];
string s[10];
int ans,second,n,m,a[10];
void calc(){
	int b[10],p,o,i,t;
	memset(b,0,sizeof(b));
	for(int i=0;i<m;i++) b[a[i]]++;
	for(int i=1;i<=n;i++) if(!b[i]) return;
	memset(root,0,sizeof(root));
	int sum=n;
	for(i=1;i<=n;i++) tree[i].clear();
	for(i=0;i<m;i++)
		for(t=a[i],p=0;s[i][p];p++){
			if(!tree[t].son[s[i][p]-'A']){
				sum++;
				tree[sum].clear();
				tree[t].son[s[i][p]-'A']=sum;
			}
			t=tree[t].son[s[i][p]-'A'];
		}
	if(sum>ans) ans=sum,second=1;
	else
	if(sum==ans) second++;
}
void dfs(int x){
	if(x==m){
		calc();
		return;
	}
	for(int i=1;i<=n;i++){
		a[x]=i;
		dfs(x+1);
	}
}
int main(){
	freopen("a.txt","r",stdin);
	freopen("b.txt","w",stdout);
	int T,i;
	cin>>T;
	for(int k=1;k<=T;k++){
		ans=0;
		cin>>m>>n;
		for(i=0;i<m;i++) cin>>s[i];
		dfs(0);
		cout<<"Case #"<<k<<": "<<ans<<' '<<second<<endl;
	}
}
