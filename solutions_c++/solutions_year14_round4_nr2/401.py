#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <memory.h>

using namespace std;
const int INF=1000000000;
int ans,n;
int a[1005];
int ar[1005];
int b[1005];
int po[1005];

int tree_n,tree[300005];
void init(int n1){  // 초기화 : 아래에 깔리는 노드가 n1개
	tree_n=1;
	while(tree_n<n1){tree_n*=2;}
	for(int i=0;i<=2*tree_n;i++){tree[i]=0;}
}
void update(int po){  // po 번째값 업데이트
	po+=tree_n-1;
	tree[po]=1;
	while(po>1){
		po=po/2;
		tree[po]=tree[po*2]+tree[po*2+1];
	}
}
int query(int ql,int qr,int po,int l,int r){  // a~b구간, po노드가 ㅣ~r에 대응  => po=1  l=1  r=tree_n
	if(r<ql || l>qr) return 0;
	if(ql<=l && r<=qr) return tree[po];
	return query(ql,qr,2*po,l,(l+r)/2)+query(ql,qr,2*po+1,(l+r)/2+1,r);
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,ca=0;
	scanf("%d",&t);
	while(t--){
		ans=INF;
		scanf("%d",&n);
		vector<int> now;
		for(int i=1;i<=n;i++){
			scanf("%d",&a[i]);
			now.push_back(a[i]);
			b[i]=a[i];
		}
		sort(b+1,b+n+1);
		for(int i=1;i<=n;i++) for(int j=1;j<=n;j++) if(a[i]==b[j]) a[i]=j,ar[j]=i;
		init(n+1);
		ans=0;
		for(int i=1;i<=n;i++){
			int left=ar[i]-1-query(1,ar[i],1,1,tree_n);
			int right=n-ar[i]-query(ar[i],n,1,1,tree_n);
			ans+=min(left,right);
			update(ar[i]);
		}
		printf("Case #%d: %d\n",++ca,ans);
	}
	return 0;
}