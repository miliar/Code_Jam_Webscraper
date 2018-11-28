#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
using namespace std;
typedef long long int64;
const int maxn=1000100, oo=1000100000;
struct Node;
Node *null;
struct Node {
	Node *left, *right;
	int pri, key,size;
	Node(){
		left=right=null;
		pri=rand()%oo;
	}
};
void Node_init() {
	null = new Node;
	null->pri = oo;
	null->size = 0;
}
void update(Node *x) {
	x->size = 1 + x->left->size + x->right->size;
}
Node *lrotate(Node *x) {
	Node *y=x->left; x->left=y->right; y->right=x;
	update(x); update(y);
	return y;
}
Node *rrotate(Node *x) {
	Node *y=x->right; x->right=y->left; y->left=x;
	update(x); update(y);
	return y;
}
Node *insert(Node *x, int key) {
	if(x==null) {
		x=new Node;
		x->key = key;
		x->size = 1;
		return x;
	}
	if(key<x->key) {
		x->left=insert(x->left, key);
		if(x->left->pri < x->pri)
			x=lrotate(x);
	} else {
		x->right=insert(x->right, key);
		if(x->right->pri < x->pri)
			x=rrotate(x);
	}
	update(x);
	return x;
}
int count_geq(Node *x, int key) {
	if(x==null)
		return 0;
	if(key<=x->key)
		return count_geq(x->left, key)+1+x->right->size;
	else
		return count_geq(x->right, key);
}
void free(Node *x) {
	if(x==null)
		return;
	free(x->left), free(x->right);
	delete x;
}

int n,diff;
int val[maxn], ch[maxn], sib[maxn];
int lval[maxn], hval[maxn];
void testin() {
	scanf("%d%d",&n,&diff);
	int S,A,C,R;
	scanf("%d%d%d%d",&S,&A,&C,&R);
	for(int i=0;i<n;i++) {
		val[i+1]=S;
		S=(int64(S)*A+C)%R;
	}
	scanf("%d%d%d%d",&S,&A,&C,&R);
	fill(ch+1, ch+n+1, 0);
	fill(sib+1, sib+n+1, 0);
	for(int i=0;i<n;i++) {
		if(i) {
			int x=i+1, p=S%i+1;
			sib[x]=ch[p], ch[p]=x;
		}
		S=(int64(S)*A+C)%R;
	}
	
	/*for(int i=1;i<=n;i++)
		printf("%d ",val[i]);
	puts("");
	for(int i=1;i<=n;i++)
		printf("%d ",par[i]);
	puts("");*/
}
void dfs(int x, int mi, int ma) {
	lval[x] = mi = min(mi, val[x]);
	hval[x] = ma = max(ma, val[x]);
	for(int y=ch[x];y;y=sib[y])
		dfs(y,mi,ma);
}
bool cmp(int x, int y) {
	return hval[x]<hval[y];
}
int lst[maxn];
void testcase() {
	testin();  dfs(1, oo, -oo);
	//printf("n=%d\n",n);
	//for(int i=1;i<=n;i++)
	//	printf("%d %d\n",lval[i],hval[i]);

	for(int i=1;i<=n;i++)
		lst[i] = i;
	sort(lst+1, lst+n+1, cmp);
	
	Node *root = null;
	int ans=0;
	for(int i=1;i<=n;i++) {
		int x=lst[i];
		root = insert(root, lval[x]);
		int cnt=count_geq(root, hval[x]-diff);
		//add lval[x]
		//count >=hval[x]-diff
		ans=max(ans,cnt);
		//printf("%d~%d: %d\n",hval[x]-diff,hval[x],cnt);
	}
	printf("%d\n",ans);
	free(root);
}
int main() {
	Node_init();

	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++) {
		printf("Case #%d: ",i);
		testcase();
	}
	scanf("%*s");
	return 0;
}
