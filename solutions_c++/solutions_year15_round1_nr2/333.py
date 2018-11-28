#include<cstdio>
int tm[1002];
int main(){
    int t,i,turn,b,n;
    long long int ss,ee,mid,can,cansu,zero;
    long long int cnt,cal1,cal2,zerocnt;
    int ccnt;
    //freopen("B-large.in.txt","r",stdin);
    scanf("%d",&turn);
    //freopen("dap.txt","w",stdout);
    for(t=1;t<=turn;t++){
        scanf("%d %d",&b,&n);
        printf("Case #%d: ",t);
        for(i=0;i<b;i++) scanf("%d",&tm[i]);
        ss=1;ee=n;ee=ee*100005;
        if(b>=n){
            printf("%d\n",n);
        }else{
            while(ss<=ee){
                mid=(ss+ee)/2;
                cnt=b;zerocnt=0;
                for(i=0;i<b;i++){
                    cal1=mid;cal2=mid;
                    cal1/=tm[i];
                    cal2=cal2%tm[i];
                    cnt+=cal1;
                    if(cal2==0) zerocnt++;
                }
                if(cnt>=n){
                    can=mid;
                    cansu=cnt;
                    zero=zerocnt;
                    ee=mid-1;
                }else{
                    ss=mid+1;
                }
            }
            zerocnt=0;
            for(i=0;i<b;i++){
                cal2=can;
                cal2=cal2%tm[i];
                if(cal2==0){
                    zerocnt++;
                    if(zerocnt==zero-(cansu-n)){
                        printf("%d\n",i+1);
                        break;
                    }
                }
            }
        }
    }
}
