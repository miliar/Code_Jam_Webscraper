#include <bits/stdc++.h>
#define all(a) (a).begin(),(a).end()
#define ld long double
#define ll long long
#define sqr(a) (a)*(a)
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define inf (int)1e9
#define pi pair<int,int>
#define y1 fdfs
using namespace std;
inline void read(int &x){x = 0;while(1){char ch = getchar();if(ch==' '||ch=='\n') break;x = x*10 + ch - '0';}}
inline void write(int x){char wr[12];int k = 0;if(!x) ++k,wr[k] = '0';while(x){++k;wr[k] = char(x%10+'0');x/=10;}for(int i=k;i>=1;--i)putchar(wr[i]);}
int T,n,ans;
string s;
//++
void solve()
{
    ans = 0;
    while(1){
        bool p = 0;
        for(int i=0;i<s.size();++i)
            if(s[i]=='-') p = 1;
        if(!p) break;
        if(s[0]=='-')
        {
            int pos = -1;
            for(int j=(int)s.size()-1;j>=0;--j)
                if(s[j]=='-') {
                    pos = j;
                    break;
                }
            reverse(s.begin(),s.begin()+pos+1);
            for(int i=0;i<=pos;++i)
                if(s[i]=='+') s[i]='-';
            else s[i]='+';
        }else{
            int pos = 0;
            for(int j=0;j<s.size();++j)
                if(s[j]=='-') {
                    pos = j - 1;
                    break;
                }
            reverse(s.begin(),s.begin()+pos+1);
            for(int i=0;i<=pos;++i)
                if(s[i]=='+') s[i]='-';
            else s[i]='+';
        }
        ++ans;
    }

}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("1.out","w",stdout);
    ios_base::sync_with_stdio(0);
    cin>>T;
    for(int t=1;t<=T;++t)
    {
        cin>>s;
        cout<<"Case #"<<t<<": ";
        solve();
        cout << ans << "\n";
    }
}
