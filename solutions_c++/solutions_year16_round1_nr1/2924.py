#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<string>
#include<cmath>
#include<queue>
#include<map>
#include<set>
#include<sstream>
#include<stack>
#include<vector>
#include<stack>
#define gc getchar_unlocked
using namespace std;
typedef long long int int64;

int main()
{
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
int64 i,j,k,n,m,t,cnt=1;
cin>>t;
char a[1002];
while(t--){
 	scanf("%s",a);
 	n = strlen(a);
 	string ans;
 	ans = a[0];
 	for(i=1;i<n;i++){
 		if(a[i]>=ans[0])ans=a[i]+ans;
 		else ans=ans+a[i];
 	}
 	printf("Case #%lld: ",cnt);
 	for(i=0;i<n;i++)printf("%c",ans[i]);
 	printf("\n");
	cnt++;
}
return 0;
}

