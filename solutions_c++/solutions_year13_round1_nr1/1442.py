#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
int main(){
    int t;
    scanf("%d",&t);
    for(int iiii=1;iiii<=t;iiii++){
        int r,t;
        scanf("%d %d",&r,&t);
        int sum=2*r+1;
        int count=0;
        while(sum<=t){
            count++;
            r+=2;
            sum+=2*r+1;
        }
        printf("Case #%d: %d\n",iiii,count);
    }
}