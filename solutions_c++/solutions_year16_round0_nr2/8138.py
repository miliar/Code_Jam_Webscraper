#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <algorithm>
using namespace std;

int T,iCase;
char s[110];
int len;
int l,r;
int ans;

bool is(){
    int i,j;
    for(i=0;i<len;i++){
        if(s[i]=='-')
            return false;
    }
    return true;
}

void sw(int x,int y){
    int i,j;
    char sl[110];
    for(i=x;i<=y;i++)
        sl[i]=s[i];
    for(i=x;i<=y;i++){
        if(sl[x+y-i]=='-')
            s[i]='+';
        else s[i]='-';
    }
    ans++;
    return ;
}

int main()
{
    int i,j;
    FILE *fp;
    fp=fopen("H:\\out2-1-da.txt","w");
    freopen("H:B-large.in","r",stdin);
    scanf("%d",&T);
    for(iCase=1;iCase<=T;iCase++){
        scanf("%s",s);
        ans=0;
        len=strlen(s);
        r=len-1;
        while(r>=0&&s[r]=='+')r--;
        if(r==-1){
            fprintf(fp,"Case #%d: 0\n",iCase);
            //printf("Case #%d: 0\n",iCase);
            continue;
        }
        while(!is()){
            r=len-1;
            while(r>=0&&s[r]=='+')r--;
            if(s[0]=='+'){
                l=0;
                while(l<len&&s[l]=='+')l++;
                sw(0,l-1);
            }
            sw(0,r);
        }
        fprintf(fp,"Case #%d: %d\n",iCase,ans);
        //printf("Case #%d: %d\n",iCase,ans);
    }
    return 0;
}
