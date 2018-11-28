#include <cstdio>

const int NMAX=1111;

int a[NMAX];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,ti,n,i,start,end,m,mi,ans;
	scanf("%d",&t);
	for(ti=1;ti<=t;ti++){
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%d",&a[i]);
		}

		ans=0;
		start=0; end=n-1;
		while(start<end){
			m=2000000000;
			for(i=start;i<=end;i++){
				if(m>a[i]){
					m=a[i];
					mi=i;
				}
			}
			if(end-mi > mi-start){
				ans += mi-start;
				for(i=mi;i>start;i--){
					a[i]=a[i-1];
				}
				start++;
			}else{
				ans += end-mi;
				for(i=mi;i<end;i++){
					a[i]=a[i+1];
				}
				end--;
			}
		}
		printf("Case #%d: %d\n",ti,ans);
	}
}