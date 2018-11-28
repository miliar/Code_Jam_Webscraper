#include<stdio.h>
#include<iostream>

using namespace std;

int M[10010][10010];

int multiply(int ans,char x) {
    int abs=ans;
    if(abs<0)
        abs=-abs;
    if(abs==1)
        return abs==ans ? x-'i'+2 : -(x-'i'+2);
    else if(abs==2) {
        if(x=='i')
            return abs==ans ? -1 : 1;
        if(x=='j')
            return abs==ans ? 4 : -4;
        if(x=='k')
            return abs==ans ? -3 : 3;
    }
    else if(abs==3) {
        if(x=='i')
            return abs==ans ? -4 : 4;
        if(x=='j')
            return abs==ans ? -1 : 1;
        if(x=='k')
            return abs==ans ? 2 : -2;
    }
    else if(abs==4) {
        if(x=='i')
            return abs==ans ? 3 : -3;
        if(x=='j')
            return abs==ans ? -2 : 2;
        if(x=='k')
            return abs==ans ? -1 : 1;
    }
    return 0;
}

int main() {
    FILE* fin = fopen("C-small-attempt0.in","r");
    FILE* fout = fopen("out.txt","w");
    int c=1,t;
    fscanf(fin,"%d",&t);
    while(c<=t) {
        int l,x;
        char s[10010];
        fscanf(fin,"%d %d %s",&l,&x,s);
        string ss(s),str="";
        for(int i=0;i<x;i++)
            str+=ss;
        int n=x*l;
        int ans=0;

        for(int i=0;i<n;i++) {
            for(int j=i;j<n;j++) {
                if(j==i)
                    M[i][j]=multiply(1,str[j]);
                else {
                    M[i][j]=multiply(M[i][j-1],str[j]);
                    // printf("-> %d %c = %d \n",M[i][j-1],str[j],M[i][j]);
                }
            }
            // printf("\n");
        }

        /*

        for(int i=0;i<n;i++) {
            for(int j=0;j<n;j++)
                printf("%d ",M[i][j]);
            printf("\n");
        }
        printf("\n");

        */

        for(int i=1;i<n-1 && !ans;i++) {
            for(int j=i+1;j<n && !ans;j++)
                if(M[0][i-1]==2 && M[i][j-1]==3 && M[j][n-1]==4)
                    ans=1;
        }
        if(ans)
            fprintf(fout,"Case #%d: YES\n",c);
        else
            fprintf(fout,"Case #%d: NO\n",c);
        c++;
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
