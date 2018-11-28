#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    char s[300];
    scanf("%d",&t);
    int case1=0;
    while(t--)
    {
        case1++;
        scanf("%s",&s);
        char last=s[0];
        int change=0;
        int i;
        for(i=1;s[i]!='\0';i++)
        {
            if(s[i]!=last)
            {
                change++;
                last=s[i];
            }
        }
        if(s[--i]=='-')
            change++;
        printf("Case #%d: %d\n",case1,change);
    }
}
