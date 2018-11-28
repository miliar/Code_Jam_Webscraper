#include<iostream>
#include<cstdio>
int main(){
    int t;
    scanf("%d",&t);
    for(int ti=1;ti<=t;ti++){
        int n,ar[26];
        scanf("%d",&n);
        for(int i=0;i<n;i++){
            scanf("%d",&ar[i]);
        }
        /*for(int i=0;i<n;i++){
            printf("%d\n",ar[i]);
        }*/
        printf("Case #%d: ",ti);
        while(1){
            int max1=0,max2=0,no1=0,no2=0;
            for(int i=0;i<n;i++){
                if(ar[max1]<ar[i]){
                    max1=i;
                    no1=1;
                }
                else if(ar[max1]==ar[i]){
                    no1++;
                }

            }
            if(ar[max1]==1 && no1==3){
                printf("%c ",max1+'A');
                ar[max1]--;
                continue;
            }
            if(ar[max1]==0){
                break;
            }
            max2=(max1+1)%n;
            for(int i=0;i<n;i++){
                if(ar[max2]<ar[i]&&max1!=i){
                    max2=i;
                    no2=1;
                }
                else if(ar[max2]==ar[i]){
                    no2++;
                }
            }
            printf("%c%c ",max1+'A',max2+'A');
            ar[max1]--;
            ar[max2]--;
        }
        printf("\n");
    }
}
