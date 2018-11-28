#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
    int t,i,l,c,k;
    char s[105];
    scanf("%d",&t);
    getchar();
    k=1;
    while(t--)
    {
        scanf("%s",s);
        l=strlen(s);
        c=0;
        for(i=0;s[i+1]!='\0';i++)
            if(s[i]!=s[i+1])
                c++;
        if(s[l-1]=='-')
            c++;
        printf("Case #%d: %d\n",k++,c);
    }
    return 0;
}
