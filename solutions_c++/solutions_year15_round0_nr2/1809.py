#include<stdio.h>
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int in=1;in<=T;in++){        
        int n;
        scanf("%d",&n);
        int ary[1001],maxtime=0;
        for(int ii=0;ii<n;ii++) {scanf("%d",&ary[ii]); maxtime=max(ary[ii],maxtime);}
        int mintime=10000000;
        for(int etime=1;etime<=maxtime;etime++){
             int step=0;
             for(int i=0;i<n;i++){
                 step+=((ary[i]-1)/etime);
             }
         //    printf("etime=%d,step=%d\n",etime,step);
             mintime=min(mintime,etime+step);
        }
    printf("Case #%d: %d\n",in,mintime);
    }
}
