#include<cstdio>
using namespace std;
int main(){
int T,n,sum,ans;
	freopen("A-large.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	scanf("%d\n",&T);
char s[1005];

for  (int cas=1;cas<=T;cas++){

	scanf("%d %s",&n,s);
	sum=s[0]-'0';
	ans=0;	
	for (int i=1;i<=n;i++){
		if (sum<i&&s[i]!='0') {
			ans+=i-sum;
			sum=i;
		}
		sum+=s[i]-'0';
	}
	printf("Case #%d: %d\n",cas,ans);
}
}
