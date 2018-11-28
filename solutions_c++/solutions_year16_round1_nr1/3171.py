#include<bits/stdc++.h>
using namespace std;
#define ll long long int


int main()
{
    #ifndef ONLINE_JUDGE
        freopen("A-large.in", "r", stdin);
        freopen("ans1.txt", "w", stdout);
    #endif // ONLINE_JUDGE

    int test;
    scanf("%d", &test);
    for(int i=1; i<=test; ++i)
    {
        ll l, s=1000, e=1000;
        char ch[1009], ans[2008];
        cin>>ch;
        l = strlen(ch);
        ans[s]=ch[0];
        cout<<"Case #"<<i<<": ";
        for(ll j=1; j<l; ++j)
        {
            if(int(ans[s])>int(ch[j]))
               ans[++e]=ch[j];
            else
                ans[--s]=ch[j];
        }
        for(ll q=s; q<=e; ++q)
            cout<<ans[q];
        cout<<endl;
    }
    return 0;
}
