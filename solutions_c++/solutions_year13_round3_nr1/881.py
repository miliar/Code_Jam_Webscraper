#include<cstdio>
#include<cstdlib>
#include<vector>
#include<map>
#include<set>
#include<cstring>

#define pb(X) push_back(X)
#define mp(X,Y) make_pair(X,Y)
#define sz(X) (int)X.size()

char s[1000010];
int v[1000010];
int sum[1000010];

int main(){
	int T;
	scanf("%d", &T);
	for(int caso=1;caso<=T;caso++) {
		int n,m;
		scanf("%s %d",s,&m);
		n=strlen(s);
		for(int i=0;i<n;i++){
			if(s[i]=='a' || s[i]=='e' || s[i] =='i' || s[i]=='o' || s[i] =='u')
				v[i+1]=0;
			else v[i+1]=1;
		}
		v[0]=0;
		sum[0]=0;
		for(int i=1;i<=n;i++)
			sum[i]=sum[i-1]+v[i];
		long long resp=0;
		int j=1;
		for(int i=m;i<=n;i++){
			if(sum[i]-sum[i-m] == m){
				for(;j<=i-m+1;j++)
					resp+= n-i+1;
			}
		}
		printf("Case #%d: %lld\n",caso,resp);
	}
	return 0;
}
