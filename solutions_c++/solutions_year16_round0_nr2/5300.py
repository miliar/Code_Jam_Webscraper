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
int64 a[10];
int64 fn(int64 n){
	int64 k;
	while(n>0){
		k = n%10;
		a[k]=1;
		n/=10;
	}
}
int64 chk() {
	for(int i=0;i<10;i++){
		if(a[i]!=1)return 0;
	}
	return 1;
}
int main()
{
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
int64 i,j,k,n,t,x,y,fl,cnt=1,ans;
cin>>t;
char s[10000],pr;
while(t--){
 	scanf("%s",s);
 	n = strlen(s);pr='+';ans=0;
 	for(i=n-1;i>=0;i--){
 		if(s[i]!=pr){
 			ans++;
 			if(pr=='+')pr='-';
 			else pr='+';
 		}
 	}
 	printf("Case #%lld: %lld\n",cnt,ans);
	cnt++;
}
return 0;
}

