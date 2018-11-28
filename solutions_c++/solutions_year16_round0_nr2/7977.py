#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int num = t;
    while(t--)
    {
        char str[105];
        scanf("%s",str);
        int c = 0;
        for(int i=0;i<strlen(str);)
        {
            if(str[i]=='-'){
            while(str[i]=='-')
            i++;
            c++;
            }
            else {
            while(str[i]=='+')
            i++;
            if(i!=strlen(str))
            c++;
            }
        }
        printf("Case #%d: %d\n",num-t,c);
    }
    return 0;
}
