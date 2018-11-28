#include<bits/stdc++.h>

using namespace std;

#define s(n) scanf("%d", &n)

int main()
{

    int T, start, end;
    s(T);
    for(int i=1;i<=T;i++)
    {
        char s[4000], ans[4000];
        for(int j=0;j<4000;j++)
            ans[j]='\0';
        for(int j=0;j<4000;j++)
            s[j]='\0';
        scanf("%s", s);
        start=2000;
        end=2000;
        ans[start]=s[0];
        for(int j=1;s[j]!='\0';j++)
        {
            if(s[j]>=ans[start])
                ans[--start]=s[j];
            else
                ans[++end]=s[j];
        }
        cout<<"Case #"<<i<<": ";
        for(int j=start;j<=end;j++)
            cout<<ans[j];
        cout<<"\n";
    }
    return 0;
}
