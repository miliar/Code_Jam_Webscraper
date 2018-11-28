#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;

int count1[1020];

int main(){
    int t;
    scanf("%d",&t);
    int testCase=1;
    while(t--){
        int d;
        scanf("%d",&d);
        int num;
        for(int i=1;i<=1000;i++){
            count1[i]=0;
        }
        for(int i=0;i<d;i++){
            scanf("%d",&num);
            count1[num]++;
        }
        int ans=10000000;
        for(int i=1;i<=1000;i++){
            int tempAns=i,midAns=0;
            for(int j=i+1;j<=1000;j++){
                midAns=j/i;
                if(j%i==0)
                    midAns--;
                tempAns+=midAns*count1[j];
            }
            if(tempAns<ans){
                ans=tempAns;
            }
        }
        printf("Case #%d: %d\n",testCase,ans);
        testCase++;
    }
    return 0;
}