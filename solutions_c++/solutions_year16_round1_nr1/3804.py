//Coded by: speeDemon/thunderclash
#include<bits/stdc++.h>
#define dbg(x)
using namespace std;
typedef long long ll;

deque<char> ans;

int main()
{
    freopen("Abig.in","r",stdin);
    freopen("Aout.txt","w",stdout);
    ll t,tinit;
    char s[1001];
    cin>>t;
    tinit=t;
    while(t--)
    {
        ans.clear();
        getchar();
        scanf("%s",s);
        ans.push_back(s[0]);
        for(int i=1;s[i]!='\0';++i)
        {
            if(s[i]>=ans[0])
                ans.push_front(s[i]);
            else
                ans.push_back(s[i]);
        }
        printf("Case #%d: ",tinit-t);
        for(int i=0;i<ans.size();++i)
            printf("%c",ans[i]);
        printf("\n");
    }
    return 0;
}
