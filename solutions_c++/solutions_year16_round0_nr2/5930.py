#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
char str[110];
char ch;
int main(){
    FILE *rf,*wf;
    rf=fopen("A.txt","r");
    wf=fopen("Aa.txt","w");
    int t,i,j,ctr;
    fscanf(rf,"%d",&t);
    for(i=0;i<t;i++){
        fscanf(rf,"%s",str);
        ctr=0;
        ch=str[0];
        for(j=0;j<strlen(str);j++){
            if(ch!=str[j]){
                ctr++;
                ch=str[j];
            }
        }
        if(str[strlen(str)-1]=='+')
            fprintf(wf,"Case #%d: %d\n",i+1,ctr);
        else
            fprintf(wf,"Case #%d: %d\n",i+1,ctr+1);
    }
    return 0;
}
