#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("output.txt","w",stdout);
    freopen("input.txt","r",stdin);
    int t;
    char s[110];
    int p=1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%s",s);
        int c=0,i;
        char prev='#';
        for(i=0;s[i]!='\0';i++)
        {
            if(s[i]!=prev)
            {
                c++;
                prev=s[i];
            }
        }
        if(s[i-1]=='+')
            c--;
        printf("Case #%d: %d\n",p,c);
        p++;
    }
}
