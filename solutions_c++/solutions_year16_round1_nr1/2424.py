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
typedef long long LL;
#define mod 1000000007
#define N 1010
#define DEBUG 0

int T,n,l,r;
char s[N],f[N*5];

int main() {
	if(!DEBUG){
		freopen("in.in","r",stdin);
		freopen("out.out","w",stdout);
	}
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
    	scanf("%s",s);
    	n=strlen(s);
    	l=r=n;
    	f[n]=s[0];
    	for(int i=1;i<n;i++){
	    	if(s[i]>=f[l]){
	    		l--;
	    		f[l]=s[i];
	    	}else{
	    		r++;
	    		f[r]=s[i];
	    	}
	    }
	    printf("Case #%d: ",t);
	    for(int i=l;i<=r;i++) printf("%c",f[i]);
	    printf("\n");
    }
    return 0;
}
