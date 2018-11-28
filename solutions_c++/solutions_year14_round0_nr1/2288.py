#include<stdio.h>
#include<iostream>

using namespace std;

int num[17];

int main(){
    int t,row1,row2,temp,ans,cans,ccase=1;
    scanf("%d",&t);
    while(t--){
        scanf("%d",&row1);
        for(int i=0;i<17;i++) num[i]=0;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                scanf("%d",&temp);
                if(i==row1-1){
                    num[temp]++;
                }
            }
        }
        scanf("%d",&row2);
        cans=0;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                scanf("%d",&temp);
                if(i==row2-1){
                    if(num[temp]>0){
                        ans=temp;
                        cans++;
                    }
                }
            }
        }
        if(cans==1)
            printf("Case #%d: %d\n",ccase,ans);
        else if(cans>1)
            printf("Case #%d: Bad magician!\n",ccase);
        else
            printf("Case #%d: Volunteer cheated!\n",ccase);
        ++ccase;
    }
    return 0;
}
