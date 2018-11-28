#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int n,m,ans,n1,m1,a[11000],nn,i,j,T,TT;
int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&TT);
	for(T=1;T<=TT;T++){
		scanf("%d%d",&n,&m);
		ans=0;
		for(i=1;i<=n;i++){
			scanf("%d",&a[i]);
		}
		sort(a+1,a+n+1);
		n1=0;nn=n;
		while(n1<n){
			m1=m;
			for(i=nn;i>=1;i--)if(a[i]>0){
				m1-=a[i];a[i]=-1;
				n1++;break;
			}nn--;
			for(j=i;j>=1;j--)if(a[j]>0&&m1>=a[j]){
				m1-=a[j];a[j]=-1;
				n1++;break;
			}
			ans++;
		}
		printf("Case #%d: %d\n",T,ans);
	}
}