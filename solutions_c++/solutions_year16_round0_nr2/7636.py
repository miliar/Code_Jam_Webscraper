#include<stdio.h>
#include<algorithm>
using namespace std;
int main(){

    char in[1005];
    int n,m,i,j,k,t;
    int ans,sum;

    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    scanf("%d",&t);
    for(k=1;k<=t;k++)
       {
        ans = 0;
        scanf("%s",in);
        char cur;
        int ff=0;
        cur = in[0];
        for(i=1;in[i]!='\0';i++) {
            if(in[i]!=cur) {
                ff++;
                if(cur == '-') cur = '+';
                else cur = '-';
            }
        }
        if(in[i-1]=='-') ff++;
        ans = ff;
        printf("Case #%d: %d\n",k,ans);
       }
 return 0;
}
