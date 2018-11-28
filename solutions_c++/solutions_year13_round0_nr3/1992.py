#include<cstdio>
#define LL long long
int T,num=0;
LL z[15],A,B, list[50];

bool pal(LL i){
     int num;
     for (int j = 1; j < 15; j++)
         if ((i / z[j]) == 0){
            num = j;
            break;
         }
     int half = (int)(((double)num)/2);
     bool s = 1;
     for (int j = 0; j < half; j++){
         if ((LL)(i/z[num-j-1])%10 != ((LL)i/z[j])%10)  s = 0;
     }    
     return s;
}

int main(){;
//    freopen("GCJ13_QR_Clarge1.in","r",stdin);
//    freopen("GCJ13_QR_Clarge1.out","w",stdout);

    z[0] = 1;
    for (int i = 0; i < 15; i++)
        z[i+1] = z[i]*10;
    
    for (int i = 1; i <= 10000000; i++)
        if (pal((LL)i))
           if (pal((LL)(i)*(LL)(i))) list[num++] = (LL)i*i;
           
//    printf("%d\n",num);
//    for (int i = 0; i < num; i++)printf("%I64d\n",list[i]);
    scanf("%d",&T);
    for (int i = 0; i < T; i++){
        scanf("%I64d%I64d",&A,&B);
        int st = -1, et = num;
        for (int j =0; j < num; j++){
            if (list[j] < A)st = j;
            if (list[j] > B){et = j; break;}
        }
        printf("Case #%d: %d\n",i+1,et-st-1);
    }
    return 0;               
}
