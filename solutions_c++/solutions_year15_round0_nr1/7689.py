#include<stdio.h>

int main()
{

    freopen("A-large.in","r",stdin);
    freopen("A-larg.out","w",stdout);
    int t;

    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        int s,ans=0;
        scanf("%d", &s);
        char str[s+1];
        scanf("%s", &str);
        //int l=strlen(str);
        int l=s+1;
        int tmp=str[0]-48;
        //printf("tmp=%d\n", tmp);
        for(int j=1;j<l;j++)
        {
            if((str[j]-48)!=0){
                if(tmp<j){

                    ans+=j-tmp;
                    tmp=str[j]-48+j;
                }
                else
                    tmp+=str[j]-48;
            }
        }
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
