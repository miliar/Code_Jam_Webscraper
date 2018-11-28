#include<cstdio>
int pnt[3002][2];
int mn;
int main(){
    int t,turn,n,i,j,k;
    long long int aa,bb,cc,cal1,cal2,cal3,cal4;
    int cnt1,cnt2;
    //freopen("A-large.in-1.txt","r",stdin);
    //freopen("dap.txt","w",stdout);
    scanf("%d",&turn);
    for(t=1;t<=turn;t++){
        scanf("%d",&n);
        for(i=0;i<n;i++){
            scanf("%d %d",&pnt[i][0],&pnt[i][1]);
        }
        printf("Case #%d:\n",t);
        for(i=0;i<n;i++){
            mn=n+100;
            for(j=0;j<n;j++){
                if(i==j) continue;
                aa=pnt[j][1]-pnt[i][1];
                bb=pnt[i][0]-pnt[j][0];
                cal1=pnt[j][0];
                cal2=pnt[i][1];
                cal3=pnt[i][0];
                cal4=pnt[j][1];
                cal1=cal1*cal2;cal3=cal3*cal4;
                cc=cal1-cal3;
                cnt1=0;cnt2=0;
                for(k=0;k<n;k++){
                    cal1=aa*pnt[k][0];
                    cal2=bb*pnt[k][1];
                    cal3=cc;
                    cal1=cal1+cal2+cal3;
                    if(cal1>0){
                        cnt1++;
                    }else if(cal1<0){
                        cnt2++;
                    }
                }
                if(cnt1>cnt2){
                    if(mn>cnt2){
                        mn=cnt2;
                    }
                }else{
                    if(mn>cnt1){
                        mn=cnt1;
                    }
                }
            }
            if(mn==n+100){
                printf("0\n");
            }else{
                printf("%d\n",mn);
            }
        }
    }
}
