#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll INF=1e18+7;
const int MX=1e3+3;
char bb[MX];
int main()
{
   freopen("A-large.in", "r", stdin);
  freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int jj=1;jj<=t;jj++){
   string h;
   scanf("%s",bb);
   h=bb;

   int k;
   scanf("%d",&k);
   int ans=0;
   for(int i=0;i<=(int)h.size()-k;++i)
        if(h[i]=='-')
        {
            ans++;
            for(int j=i;j<i+k;j++)
            {
                if(h[j]=='-')h[j]='+';
                else h[j]='-';
            }
        }
    bool sex=0;
    for(int i=0;i<h.size();i++)
    {
        if(h[i]=='-')sex=1;
    }
    if(sex)printf("Case #%d: IMPOSSIBLE\n",jj);
    else printf("Case #%d: %d\n",jj,ans);
    }
    return 0;
}


