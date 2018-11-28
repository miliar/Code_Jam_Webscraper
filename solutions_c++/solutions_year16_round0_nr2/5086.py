#include <bits/stdc++.h>
using namespace std;
char s[1000];
#define pb push_back
#define mp make_pair
vector<char>V;
int main()
{
    int t,i,count,ans;
    freopen("1.in","r",stdin);
    freopen("2.out","w",stdout);
    char prev;
  cin>>t;
    int j=1;
    while(t>0)
    {
        t--;
        V.clear();
     cin>>s;
        prev=s[0];
        count=0;
        V.pb(s[0]);
        if(strlen(s)==1){
            if(s[0]=='+')
            {
                printf("Case #%d: 0\n",j);
            }
            else
                printf("Case #%d: 1\n",j);
                j++;
            continue;
        }
        for(i=1;s[i]!='\0';i++)
        {
            if(s[i]!=prev)
            {
                V.pb(prev);
                count=i;
            }
            prev=s[i];
        }
        ans=0;
        prev=V[0];
        for(i=1;i<V.size();i++)
        {
            if(prev=='-')
            {
                prev='+';
                ans++;
            }
            else
            {
                prev='-';
                ans++;
            }
        }
        if(prev=='-')
            ans++;
        printf("Case #%d: %d\n",j,ans);
            j++;
    }
}
