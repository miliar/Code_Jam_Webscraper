#include<bits/stdc++.h>
using namespace std;

int main()
{
    //Place the Input File in the same directory as that of the cpp file.
    //Write the code normally as you take input from keyboard using scanf..
    //Just Place freopen() as the first statement in main();
    freopen("B-large.in","r",stdin);
    freopen("Output.txt","w",stdout);
    int t,i,j,l,c;
    scanf("%d",&t);
    for(i=1;i<=t;++i)
    {
        char s[101];
        scanf("%s",s);
        l=strlen(s);c=0;
        for(j=0;j<l-1;++j)
        {
            if(s[j]!=s[j+1])
            {
                c++;
            }
        }
        if(s[l-1]=='-')
            c++;
        printf("Case #%d: %d\n",i,c);
    }
    return 0;
}
