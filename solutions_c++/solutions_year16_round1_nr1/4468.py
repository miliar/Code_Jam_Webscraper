#include<bits/stdc++.h>
using namespace std;
char s[3000];
char ara[3000];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.o","w",stdout);
    int i,j,k,l,m,n,t;

    char mx;
    scanf("%d",&t);
    getchar();
    for(int p=1;p<=t;p++)
    {
        gets(s);
        l=strlen(s);
        ara[1500]=s[0];
        mx=s[0];
        int mxc=1500;
        i=1501;
        j=1500-1;
        for(k=1;k<l;k++)
        {
            if(s[k]>mx){
                ara[j]=s[k];
                mx=s[k];
                //mxc=j;
                j--;}
            else if(s[k]<mx){
                ara[i]=s[k];
                i++;}
            else if(s[k]==mx){
                ara[j]=s[k];
                j--;}
        }
        printf("Case #%d: ",p);
        for(k=j+1;k<i;k++)
            printf("%c",ara[k]);
        printf("\n");
    }
    return 0;
}
