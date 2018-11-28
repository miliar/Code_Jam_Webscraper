#include<stdio.h>
#include <algorithm>
#include <string.h>

int first;
int second;
int firstLine[4];
int secondLine[4];
int pass;
int indexNumbber;

void scanFirst(){
    for(int i=0; i<4; i++){
        if(i == first-1){
           for(int j=0; j<4; j++){
                scanf("%d",&firstLine[j]);
            }
            continue;
        }
        for(int j=0; j<4; j++){
            scanf("%d",&pass);
        }
    }
}

void scanSecond(){
    for(int i=0; i<4; i++){
        if(i == second-1){
           for(int j=0; j<4; j++){
                scanf("%d",&secondLine[j]);
            }
            continue;
        }
        for(int j=0; j<4; j++){
            scanf("%d",&pass);
        }
    }
}

int sameCount(){
    int sCount = 0;
    int index;
    for(int i=0; i<4; i++){
        for(int j=0; j<4; j++){
            if(firstLine[i] == secondLine[j]){
                sCount++;
                indexNumbber = firstLine[i];
            }
        }
    }
    return sCount;
}

int main(){
    int T;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for(int t=1; t<=T; t++){
        scanf("%d",&first);
        scanFirst();
        scanf("%d",&second);
        scanSecond();
/*
    printf("\n the first choice  ");
    for(int i=0; i<4; i++){
        printf("\t %d",firstLine[i]);
    }
    printf("\n the second choice ");
    for(int i=0; i<4; i++){
        printf("\t %d",secondLine[i]);
    }
*/
        int sCount = sameCount();
        if(sCount > 1){
            printf("Case #%d: Bad magician!\n",t);
        }
        else if(sCount == 1){
            printf("Case #%d: %d\n",t,indexNumbber);
        }
        else{
            printf("Case #%d: Volunteer cheated!\n",t);
        }

    }


return 0;
}
