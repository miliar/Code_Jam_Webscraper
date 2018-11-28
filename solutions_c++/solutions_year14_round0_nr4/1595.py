#include<iostream>
#include<cstdio>
using namespace std;

int main(){
    int t,temp;
    scanf("%d", &t);
    temp = t;
    int n,k,answerD,answer,len;
    while(t>0){
        answerD=0;
        answer=0;
        n=0;
        k=0;
        scanf("%d", &len);
        double naomi[len],ken[len];
        for(int a=0;a<len;a++)      scanf("%lf", &naomi[a]);
        for(int a=0;a<len;a++)      scanf("%lf", &ken[a]);
        //Main code
        sort(naomi,naomi+len);
        sort(ken,ken+len);
        while(n<len && k<len){
            if(naomi[n]>ken[k]){
                answerD++;
                n++;
                k++;
            } else {
                n++;
            }   
        }
        n=0;
        k=0;
        while(n<len && k<len){
            if(naomi[n]>ken[k]){
                answer++;
                k++;
            } else {
                n++;
                k++;
            }
        }
        printf("Case #%d: ", temp-t+1);
        printf("%d %d\n", answerD, answer);
        t--;
    }
    return 0;
}
