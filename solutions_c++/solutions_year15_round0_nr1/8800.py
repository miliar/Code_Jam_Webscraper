/*  Bismillah hir rahmanir raheem. Thanks to Allah for everything.
    Coder: Abdullah Al Imran
    Email: abdalimran@gmail.com   */

#include <bits/stdc++.h>
#define endl '\n'

typedef long long ll;
const double pi = acos(-1.0);

using namespace std;

int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    int T;
    cin>>T;

    for(int i=1; i<=T; i++)
    {
        int n;
        string s;
        cin>>n>>s;

        if(n==0)
        {
            cout<<"Case #"<<i<<": 0"<<endl;
            continue;
        }

        int cnt=s[0]-'0';
        int frnd=0;

        for(int j=1; j<=n; j++)
        {
            if(j>cnt)
            {
                frnd++;
                cnt++;
            }
            cnt+=s[j]-'0';
        }
        cout<<"Case #"<<i<<": "<<frnd<<endl;
      }

    return 0;
}
