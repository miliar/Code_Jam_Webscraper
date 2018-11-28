#include<cstdio>
#include<algorithm>

using namespace std;

int m[200],T;

void test(){
	T++;
	int a,n,ans=10000,lus=0;
	scanf("%d%d",&a,&n);
	for(int i=0;i<n;i++) scanf("%d",&m[i]);
	if(a==1) ans=n;
	else{
		sort(m,m+n);
		for(int i=0;i<n;i++){
			if(a>m[i]) a+=m[i];
			else{
				ans=min(lus+n-i,ans);
				while(a<=m[i]){
					lus++;
					a=a+a-1;
				}
				a+=m[i];
			}
		}
		ans=min(ans,lus);
	}
	printf("Case #%d: %d\n",T,ans);
}

int main(){
	int t;
	scanf("%d",&t);
	while(t--) test();
	return 0;
}
