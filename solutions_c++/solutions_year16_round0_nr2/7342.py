#include <bits/stdc++.h>
#define MAXA 100005
#define MOD 1000000007
using namespace std;
char a[205];
int main()
{
    freopen("B-large.in","r+",stdin);
    freopen("output1.txt","w+",stdout);
    int t,i,x=1;
    cin>>t;
    while(t--)
    {
        int c=0;
        scanf("%s",&a);
        int l=strlen(a);
        for(i=0;i<l-1;i++)
        {
            if(a[i]=='+'&&a[i+1]=='-'||a[i]=='-'&&a[i+1]=='+')
                c++;
        }
        if(a[l-1]=='-')
            c++;
        printf("Case #%d: %d\n",x,c);
        x++;
    }
    return 0;
}
