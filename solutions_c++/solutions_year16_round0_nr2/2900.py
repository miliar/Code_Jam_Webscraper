#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include<cstdlib>
#include<ctime>
#include<cmath>
using namespace std;
typedef __int64 LL;
#define mod 1000000007
#define N 120
#define DEBUG 1

int T,n,ans;
char s[N];

int main() {
	if(DEBUG){
		freopen("in.in","r",stdin);
		freopen("out.out","w",stdout);
	}
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
    	scanf("%s",&s);
    	n=strlen(s);
    	ans=0;
    	for(int i=1;i<n;i++){
	    	if(s[i]!=s[i-1]) ans++;
	    }
	    if(s[n-1]=='-') ans++;
	    printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
