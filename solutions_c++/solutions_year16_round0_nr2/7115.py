#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

int main()
{
    string s;
    int t,i;
    cin>>t;
    for (int j=1;j<=t;j++)
    {
        cin>>s;
        int c=0,flag=0;
        int n=s.size();
        for (i=n-1;i>0 && n>1;i--)
        {
            if (s[i]!=s[i-1])
            {
                c++;
            }
        }
        if (s[n-1]=='-')
            c++;
        printf("Case #%d: %d\n",j,c);
    }
    return 0;
}
