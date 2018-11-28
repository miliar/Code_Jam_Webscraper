#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;

int main(){
    int t;
    scanf("%d",&t);
    int caseNumber=1;
    while(t--){
        int p;
        scanf("%d",&p);
        char a[1020];
        scanf("%s",a);
        int count1=0,answer=0;
        for(int i=0;i<p+1;i++){
            if(count1>=i){
                count1+=(a[i]-'0');
            }
            else if(a[i]=='0'){
                ;
            }
            else{
                answer+=(i-count1);
                count1+=(a[i]-'0')+(i-count1);
            }
        }
        printf("Case #%d: %d\n",caseNumber,answer);
        caseNumber++;
    }
    return 0;
}