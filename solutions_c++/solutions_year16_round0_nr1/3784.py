#include<bits/stdc++.h>
using namespace std;
int ans(int x)
{
    int mrk[10];
    int cnt=0;
    memset(mrk,0,sizeof(mrk));
    int ret=1;
    for(;;ret++){
        int tmp=x*ret;
        while(tmp>0){
            int b=tmp%10;
            if(!mrk[b]){
                mrk[b]=1;
                cnt++;
                if(cnt==10) return x*ret;
            }
            tmp=tmp/10;
        }
    }
}
main()
{
    freopen("Q1in.txt","r",stdin);
    freopen("Q1out.txt","w",stdout);



    int t;
    scanf("%d",&t);
    for(int kase=1;kase<=t;kase++){
        int x;
        scanf("%d",&x);
        if(x==0) printf("Case #%d: INSOMNIA\n",kase);
        else printf("Case #%d: %d\n",kase,ans(x));
    }
}
