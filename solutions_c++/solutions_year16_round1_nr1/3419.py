#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

#define sspeed ios_base::sync_with_stdio(0);cin.tie(0)
#define dbg(a) cout<<a<<endl
#define clr(a) memset(a,0,sizeof(a))
#define maxn 10001
#define mod 1000000007
#define eps 1e-9
#define inf 0x7fffffff

int main()
{
    freopen("D.in","r",stdin);
freopen("D.out","w",stdout);
    int T;
    char a[1010];
    char b[1010];
    int top1;
    int top2;
    int caseno = 0;
    cin>>T;
    while (T--)
    {
        string s;
        cin>>s;
        cout<<"Case #"<<++caseno<<": ";
        top1=0;
        top2=1;
        int i;
        b[0]=s[0];
        for (i=1;i<s.length();i++)
        {
            if (s[i]<b[top2-1]) a[top1++]=s[i];
            else b[top2++]=s[i];
        }
        for (i=top2-1;i>=0;i--)
            cout<<b[i];
        for (i=0;i<top1;i++)
            cout<<a[i];
        cout<<endl;
    }
    return 0;
}
