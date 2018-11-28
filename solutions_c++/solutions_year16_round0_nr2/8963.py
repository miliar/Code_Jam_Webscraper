#include<bits/stdc++.h>
#define pb push_back
#define mk make_pair
#define lol long long
#define ld long double
#define fc cin.tie(NULL);ios_base::sync_with_stdio(false);
using namespace std;
const int N=100005;
const int md=1000000007;

int t,c,ans,i;
string s;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    fc
    cin>>t;
    while (t--)
    {
        ++c;
        ans=0;
        cin>>s;
        if (s[0]=='-') ++ans;
        for (i=1;i<s.size();++i)
         if (s[i]=='-' && s[i-1]=='+') ans+=2;
        cout<<"Case #"<<c<<": ";
        cout<<ans;
        cout<<"\n";
    }
}
