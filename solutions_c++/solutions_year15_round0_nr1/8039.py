#include<iostream>
#include<cstring>
#include<cstdio>
#include<vector>
#include<ctype.h>
#include<queue>
#include<map>
#include<algorithm>
#define ll long long
using namespace std;

char s[1005];

int main(){
    int T,n;
    scanf("%d",&T);
    for (int t=1;t<=T;t++){
        scanf("%d",&n);
        scanf("%s",s);
        int sum=0,need=0;
        for (int i=0;i<=n;i++){
            if (sum>=i)
                sum+=s[i]-'0';
            else{
                need+=i-sum;
                sum=i+s[i]-'0';
            }
        }
        printf("Case #%d: %d\n",t,need);
    }
	return 0;
}
