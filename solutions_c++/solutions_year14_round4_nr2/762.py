#include <stdio.h>
#include <algorithm>
#include <memory.h>

using namespace std;

#define N 1005
#define INF 1e9

int n;
int a[N],b[N];
int idx[N*3],idx1[N*3],idx2[N*3],idx3[N*3],idx4[N*3];
int bi;

void input()
{
	scanf("%d",&n);
	for(int i=1; i<=n; i++) {
		scanf("%d",&a[i]);
		b[i]=a[i];
	}

	sort(b+1,b+n+1);	

	for(bi=1; bi<n; bi*=2);
}

int get_idx(int tree[], int l, int r)
{
	l+=bi-1;
	r+=bi-1;
	int cnt=0;
	while(l<=r)
	{
		if(l%2==1) cnt+=tree[l];
		if(r%2==0) cnt+=tree[r];
		l=(l+1)/2;
		r=(r-1)/2;
	}
	return cnt;
}

void update_idx(int tree[] ,int l, int t)
{
	l+=bi-1;
	while(l) {
		tree[l]+=t;
		l/=2;
	}
}

void process()
{
	int ans=INF;

	for(int i=0; i<=n; i++) {

		int tmp=0;		
		
		memset(idx1,0,sizeof(idx1));
		memset(idx2,0,sizeof(idx2));
		memset(idx3,0,sizeof(idx3));
		memset(idx4,0,sizeof(idx4));

		for(int j=i; j>=1; j--) {			
			int x=lower_bound(b+1,b+n+1,a[j])-(b);
			update_idx(idx1,x,1);
			update_idx(idx3,x,1);
		}
		
		for(int j=i+1; j<=n; j++) {			
			int x=lower_bound(b+1,b+n+1,a[j])-(b);
			update_idx(idx2,x,1);			
			update_idx(idx4,x,1);
		}

		memset(idx,0,sizeof(idx));

		for(int j=1; j<=i; j++) {
			int x=lower_bound(b+1,b+n+1,a[j])-(b);
			tmp+=min(get_idx(idx,x+1,n),get_idx(idx3,x+1,n) + get_idx(idx2,x+1,n));
			update_idx(idx,x,1);
			update_idx(idx3,x,-1);
		}

		memset(idx,0,sizeof(idx));
		for(int j=n; j>i; j--) {
			int x=lower_bound(b+1,b+n+1,a[j])-(b);
			tmp+=min(get_idx(idx,x+1,n),get_idx(idx4,x+1,n) + get_idx(idx1,x+1,n));
			update_idx(idx,x,1);
			update_idx(idx4,x,-1);
		}
		
		if(ans>tmp) ans=tmp;
	}
	printf("%d",ans);
}

int main()
{
	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
	int t,i;
	scanf("%d",&t);
	for(int i=1; i<=t; i++) {
		printf("Case #%d: ",i);
		input();
		process();
		printf("\n");
	}
	return 0;
}
