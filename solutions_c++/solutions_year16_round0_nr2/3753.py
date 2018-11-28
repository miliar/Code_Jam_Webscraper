#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("TasnimIN.txt","r",stdin);
    freopen("TasnimOUT.txt","w",stdout);
    int n,k,i,varity,start;
    char str[105];
    scanf("%d",&n);
    for(k=1;k<=n;k++)
    {
        scanf("%s",str);
        varity=1;
        if(str[0]=='+')
            start=1;
        else start=0;
        for(i=0;i<strlen(str)-1;i++)
        {
            if(str[i]!=str[i+1]){
                varity++;
            }
        }
        if(varity%2==0 && start==0 ||varity%2==1 && start==1 )
            printf("Case #%d: %d\n",k,varity-1);
        else printf("Case #%d: %d\n",k,varity);
    }
    return 0;
}
