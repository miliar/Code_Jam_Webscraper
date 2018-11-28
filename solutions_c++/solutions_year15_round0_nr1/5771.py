#include<bits/stdc++.h>
int main()
{
    int t;
    FILE *f,*g;
    f=fopen("InputFile1.txt","r");
    g=fopen("OutputFile1.txt","w");
    fscanf(f,"%d",&t);
    char ch=getchar();
    char s[1010];
    int u=t;
    while(t--)
    {
        int sum=0,ans=0,i;
        fscanf(f,"%s %s",s,s);
        for(i=0;s[i];i++)
        {
            if(s[i]-'0'!=0)
            {
                if(sum<i)
                {
                    ans=ans+i-sum;
                    sum=i;
                }
            }
            sum=sum+s[i]-'0';
        }
        fprintf(g,"Case #%d: %d\n",u-t,ans);
    }
    return(0);
}
