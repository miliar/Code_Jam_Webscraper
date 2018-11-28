#include<bits/stdc++.h>
using namespace std;
main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,c;
    scanf("%d",&T);
    for(c=1;c<=T;c++){
        char str[2010];
        int ary[2010],n,i,j;
        scanf("%s %d",str,&n);
        int len=strlen(str),ans=0;
        for(i=0;i<len;i++)ary[i]=(str[i]=='+');
        for(i=0;i<len-n+1;i++){
            if(ary[i]==0){
                for(j=0;j<n;j++)ary[i+j]=!ary[i+j];
                ans++;
            }
        }
        int fail=0;
        for(i=0;i<len;i++)
            if(!ary[i])fail=1;
        if(!fail)printf("Case #%d: %d\n",c,ans);
        else printf("Case #%d: IMPOSSIBLE\n",c);
    }
}
