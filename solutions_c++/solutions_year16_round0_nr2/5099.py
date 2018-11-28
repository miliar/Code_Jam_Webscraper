#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
    int t,i,k,count,plus,minus;
    scanf("%d",&t);
    for(k=1;k<=t;++k)
    {
        char str[105];
        scanf("%s",str);
        for(i=strlen(str)-1;i>=0 && str[i]=='+';--i);
        count=0;
        while(i>=0)
        {
            minus=0;
            while(i>=0 && str[i]=='-')
            {
                minus=1;
                i--;
            }
            if(minus)
                count++;
            plus=0;
            while(i>=0 && str[i]=='+')
            {
                plus=1;
                i--;
            }
            if(plus)
                count++;
        }
        printf("Case #%d: %d\n",k,count);
    }
}