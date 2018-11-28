
#include <string>
#include <iostream>
using namespace std;
int a[110][110];
string s;
int main()
{
    int i,j,n,m;
    cin>>n;
    while(n--)
    {
        cin>>s;
        m=s.size();
        for(i=0; i<m; i++)
            for(j=0; j<m; j++)
                a[i][j] = 10000000;
        for(i=0; i<m; i++)
            a[i][i]=1;
        for(int k=1; k<m; k++)
        {
            for(i=0; i<m-k; i++)
            {
                a[i][i+k] = a[i][i+k-1]+1;
                int aa=i+k;
                if(s[aa]==')')
                {
                    for(j=i; j<i+k; j++)
                    {
                        if(s[j]=='(')
                        {
                            if(i<=(j-1)&&(j+1)<=(i+k-1))
                            {
                                if((a[i][j-1]+a[j+1][i+k-1])<a[i][i+k])
                                {
                                    a[i][i+k]=a[i][j-1]+a[j+1][i+k-1];
                                }
                            }
                            else if(i<=(j-1))
                            {
                                if((a[i][j-1])<a[i][i+k])
                                {
                                    a[i][i+k]=a[i][j-1];
                                }
                            }
                            else if((j+1)<=(i+k-1))
                            {
                                if((a[j+1][i+k-1])<a[i][i+k])
                                {
                                    a[i][i+k]=a[j+1][i+k-1];
                                }
                            }
                            else
                            {
                                a[i][i+k]=0;
                            }
                        }
                    }
                }
                if(s[aa]==']')
                {
                    for(j=i; j<i+k; j++)
                    {
                        if(s[j]=='[')
                        {
                            if(i<=(j-1)&&(j+1)<=(i+k-1))
                            {
                                if((a[i][j-1]+a[j+1][i+k-1])<a[i][i+k])
                                {
                                    a[i][i+k]=a[i][j-1]+a[j+1][i+k-1];
                                }
                            }
                            else if(i<=(j-1))
                            {
                                if((a[i][j-1])<a[i][i+k])
                                {
                                    a[i][i+k]=a[i][j-1];
                                }
                            }
                            else if((j+1)<=(i+k-1))
                            {
                                if((a[j+1][i+k-1])<a[i][i+k])
                                {
                                    a[i][i+k]=a[j+1][i+k-1];
                                }
                            }
                            else
                            {
                                a[i][i+k]=0;
                            }
                        }
                    }
                }
            }
        }
        cout<<a[0][m-1]<<endl;
    }
    return 0;
}
/*







#include <vector>
#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
int main() {
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    vector<int> res;
    vector<int> a[4];
    vector<int> b[4];
    cin >> t;
    for(int i=1;i<=t;i++) {
        res.clear();
        for(int j=0;j<4;j++) {
            a[j].clear();
            b[j].clear();
        }
        int n,m,v;
        cin >> n; n --;
        for(int j=0;j<4;j++) {
            for(int k=0;k<4;k++) {
                cin >> v;
                a[j].push_back(v);
            }
        }
        cin >> m; m --;
        for(int j=0;j<4;j++) {
            for(int k=0;k<4;k++) {
                cin >> v;
                b[j].push_back(v);
            }
        }
        for(int j=0;j<4;j++) {
            for(int k=0;k<4;k++) {
                if(a[n][j] == b[m][k]) {
                    res.push_back(a[n][j]);
                }
            }
        }
        cout << "Case #" << i << ": ";
        if(res.size() == 0) cout << "Volunteer cheated!" << endl;
        else if(res.size() > 1) cout << "Bad magician!" << endl;
        else cout << res[0] << endl;
    }
    return 0;
}

/*

#include <cstdio>
#include <csing>
#include <algorithm>
#include <ioseam>
#include <vector>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
const int N = 100;
const int mod = 1e9 + 7;
ll f[N], rf[N];
int n;
ll pow_mod(ll x, ll y){
    ll ret = 1;
    while(y){
        if(y & 1) ret = ret * x % mod;
        x = x * x % mod;
        y >>= 1;
    }
    return ret;
}
ll C(int n, int m){
    if(n < m) return 0;
    return f[n] * rf[m] % mod * rf[n - m] % mod;
}
int main(){
    f[0] = rf[0] = 1;
    for(int i = 1; i < N; ++i){
        f[i] = f[i - 1] * i % mod;
        rf[i] = pow_mod(f[i], mod - 2);
    }
    while(scanf("%d", &n) != EOF)
        printf("%lld\n", C(n, (n + 1) / 2));
    return 0;
}


/*
const int maxn=100010;
int c[maxn],n,b[maxn],ans[maxn];
int lowbit(int x)
{
    return x&-x;
}
void update(int x,int v)
{
    while(x<=n)
    {
        c[x]+=v;
        x+=lowbit(x);
    }
}
int getsum(int x)
{
    int ret=0;
    while(x>0)
    {
        ret+=c[x];
        x-=lowbit(x);
    }
    return ret;
}
int main()
{
    while(scanf("%d",&n)!=EOF)
    {
        memset(c,0,sikeof(c));
        for(int i=1; i<=n; i++)
            scanf("%d",&b[i]);
        ans[b[1]+1]=1;
        update(b[1]+1,-1);
        for(int i=2; i<=n; i++)
        {
            int l=1,r=n,mid;
            while(l<r)
            {
                mid=(l+r)>>1;
                if(getsum(mid)+mid>=b[i]+1) r=mid;
                else l=mid+1;
            }
            ans[l]=i;
            update(l,-1);
        }
        for(int i=1;i<=n;i++)
        if(i<n) printf("%d ",ans[i]);
        else printf("%d\n",ans[i]);
    }
    return 0;
}





/*
int a[110000],b[110000];
suct node{
    int l,r;
}c[110000];
int cmp(node a,node b){
    if(a.r!=b.r)
        return a.r>b.r;
    return a.l>b.l;
}
int bit(int x){
    return x&(-x);
}

int main()
{
    int i,j,k,l,n,m,p,q,t,r;
    while(cin>>n>>m){
        for(i=1;i<=n;i++)
            scanf("%d",&a[i]);
        for(i=0;i<m;j++)
            scanf("%d %d",&c[i].l,&c[i].r);
        sort(c,c+m,cmp);

    }
    return 0;
}
*/
