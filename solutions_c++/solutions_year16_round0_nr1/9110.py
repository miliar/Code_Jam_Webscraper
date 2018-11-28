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
int T,n;
bool used[10];
int kol;
void add(int x)
{
    if(!x&&!used[0]) used[0] = 1,++kol;
    while(x)
    {
        if(!used[x%10]) used[x%10] = 1,++kol;
        x/=10;
    }
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("1.out","w",stdout);
    ios_base::sync_with_stdio(0);
    cin>>T;
    for(int t=1;t<=T;++t)
    {
        cin>>n;
        cout<<"Case #"<<t<<": ";
        bool p = 0;
        kol = 0;
        memset(used,0,sizeof used);
        for(int i=1;i&&n;++i)
        {
            add(i*n);
            if(kol==10)
            {
                cout<<i*n;
                p = 1;
                break;
            }
        }
        if(!p) cout<<"INSOMNIA";
        cout<<"\n";
    }
}
