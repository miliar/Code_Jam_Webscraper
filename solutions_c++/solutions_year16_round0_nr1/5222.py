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
int64 i,j,k,n,t,x,y,fl,cnt=1;
cin>>t;
while(t--){
 	scanf("%lld",&n);
 	if(n==0){
 		printf("Case #%lld: INSOMNIA\n",cnt);
 		cnt++;
 		continue;
 	}
 	for(j=0;j<10;j++)a[j]=0;
	for(j=1;j<=1000;j++){
		fn(n*j);
		if(chk()==1){
			break;
		}
	}
	printf("Case #%lld: %lld\n",cnt,n*j);
	cnt++;
}
return 0;
}

