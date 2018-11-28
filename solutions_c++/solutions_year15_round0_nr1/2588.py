#include <iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<queue>
using namespace std;
int T,tt;
int n;
char s[10000];
int a[10000];
int max(int a,int b){
	return a<b?b:a;
}
int main(){	
	//freopen("t.txt","r",stdin);
	//freopen("x.out","w",stdout);
	tt=1;
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		scanf("%s",s);
		int len=strlen(s);
		for(int i=0;i<len;i++){
			a[i]=s[i]-'0';
		}
		int ans=0,sum=0;
		for(int i=0;i<len;i++){
			if(ans+sum>=i){
				sum+=a[i];
				continue;
			}
			ans=i-sum;
			sum+=a[i];
		}
		printf("Case #%d: %d\n",tt++,ans);
	}
    return 0;
}