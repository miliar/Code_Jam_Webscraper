#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<stdlib.h>
using namespace std;
int chk[30],ans[30];
char s[2005];
char b[10][6]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int main(){
    int n,t,i,j,k;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(i=0;i<t;i++){
        scanf("%s",s);
        n=strlen(s);
        for(j=0;j<26;j++)    chk[j]=ans[j]=0;
        for(j=0;j<n;j++)    chk[s[j]-'A']++;
        //0
        ans[0]=chk['Z'-'A'];
        for(j=0;j<strlen(b[0]);j++) chk[b[0][j]-'A']-=ans[0];
        //8
        ans[8]=chk['G'-'A'];
        for(j=0;j<strlen(b[8]);j++) chk[b[8][j]-'A']-=ans[8];
        //2
        ans[2]=chk['W'-'A'];
        for(j=0;j<strlen(b[2]);j++) chk[b[2][j]-'A']-=ans[2];
        //3
        ans[3]=chk['H'-'A'];
        for(j=0;j<strlen(b[3]);j++) chk[b[3][j]-'A']-=ans[3];
        //4
        ans[4]=chk['U'-'A'];
        for(j=0;j<strlen(b[4]);j++) chk[b[4][j]-'A']-=ans[4];
        //6
        ans[6]=chk['X'-'A'];
        for(j=0;j<strlen(b[6]);j++) chk[b[6][j]-'A']-=ans[6];
        //5
        ans[5]=chk['F'-'A'];
        for(j=0;j<strlen(b[5]);j++) chk[b[5][j]-'A']-=ans[5];
        //9
        ans[9]=chk['I'-'A'];
        for(j=0;j<strlen(b[9]);j++) chk[b[9][j]-'A']-=ans[9];
        //1
        ans[1]=chk['O'-'A'];
        for(j=0;j<strlen(b[1]);j++) chk[b[1][j]-'A']-=ans[1];
        //7
        ans[7]=chk['V'-'A'];
        for(j=0;j<strlen(b[7]);j++) chk[b[7][j]-'A']-=ans[7];
        printf("Case #%d: ",i+1);
        for(j=0;j<10;j++){
            for(k=0;k<ans[j];k++)   printf("%d",j);
        }
        printf("\n");
    }
    return 0;
}


