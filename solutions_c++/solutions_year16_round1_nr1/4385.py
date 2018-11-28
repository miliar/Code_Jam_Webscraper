#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> ii;
ii x[1005];
vector <int> v;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int cas,c=1;
    scanf("%d",&cas);
    while(cas--)
    {
        char s[1005];
        scanf(" %s",s);
        int l=strlen(s);
        for(int i=0;s[i];i++)
        {
            x[i]=make_pair(s[i],i);
        }
        sort(x,x+l);
        int last=l+5;
        v.clear();
        for(int i=l-1;i>=0;i--)
        {
            if(x[i].second<last)
            {
                last=x[i].second;
                v.push_back(x[i].second);
            }
        }
        printf("Case #%d: ",c++);
        for(int i=0;i<v.size();i++)
        {
            printf("%c",s[v[i]]);
        }
        for(int i=v.size()-1;i>=1;i--)
            for(int j=v[i]+1;j<v[i-1];j++)
                printf("%c",s[j]);
        for(int j=v[0]+1;j<l;j++)
            printf("%c",s[j]);
        puts("");
    }
}
