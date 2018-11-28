#include<bits/stdc++.h>
using namespace std;
int main()
{
     freopen("B-small-attempt0.in","r",stdin);
    freopen("out2.o","w",stdout);
    int i,j,k,l,m,n,s=1,t;

    scanf("%d",&t);
    while(t--){
    char str[110];
    scanf("%s",str);
    int cou=0;
    for(i=strlen(str)-1;i>=0;i--){
        if(str[i]=='-'){
                str[i]='+';
                cou++;
            for(j=i-1;j>=0;j--){
                if(str[j]=='-')str[j]='+';
                else str[j]='-';
            }
        }
    }
    printf("Case #%d: %d\n",s++,cou);
    }
}
