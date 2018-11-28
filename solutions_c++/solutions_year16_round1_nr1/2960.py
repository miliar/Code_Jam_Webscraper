#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("output.txt","w",stdout);
    freopen("input.txt","r",stdin);
    int t;
    char s[1010],an[2200];
    int p=1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%s",s);
        char mx='a'-1;
        int k=1100,j=1100;
        an[k]=s[0];
        mx=an[k];
        for(int i=1;s[i]!='\0';i++)
        {
            if(s[i]<mx)
                an[++j]=s[i];
            else
            {
                an[--k]=s[i];
                mx=s[i];
            }
        }
        printf("Case #%d: ",p);
        for(int i=k;i<=j;i++)
            printf("%c",an[i]);
        printf("\n");
        p++;
    }
}

