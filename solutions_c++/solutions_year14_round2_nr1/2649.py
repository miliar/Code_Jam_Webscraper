#include<bits/stdc++.h>
using namespace std;

// #defines
#define FOR(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define sz(x) ((int)(x).size())
#define ms0(x) memset(x,0,sizeof(x))
#define ms1(x) memset(x,-1,sizeof(x))
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define f first
#define s second
#define mp make_pair
#define pb push_back
#ifdef ONLINE_JUDGE
#define FILEIO(x) freopen(#x ".in","r",stdin);freopen(#x ".out","w",stdout);
#define FILEIOS freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
#else
#define FILEIO(x) ;
#define FILEIOS ;
#endif
#define inf 1001001001
typedef pair<int,int> pii;
typedef long long ll;
typedef unsigned long long ull;
const double eps = 1e-9;
const double pi = acos(-1.0);
const int maxn = (int)1e5 + 10;
const int mod = (int)1e9;
int fastMax(int x, int y) { return (((y-x)>>(32-1))&(x^y))^y; }
int fastMin(int x, int y) { return (((y-x)>>(32-1))&(x^y))^x; }

#define FILEIO(x) freopen(#x ".in","r",stdin);freopen(#x ".out","w",stdout);
#define FILEIOS freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);

int main(){
    //FILEIO("B-small-practice");
    freopen("A-small-attempt2.in","r",stdin);
    freopen("A-small-attempt2.out","w",stdout);
    string a;
    int b[200][300],d[200],c[200],i,t,j,p,k,l,flg,r,n,lm,cnt;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>n;
        cin>>a;
        l=a.size();
        ms0(b);
        ms0(c);
        b[0][0]++;
        p=0;
        c[p]=a[0];
        for(k=1;k<l;k++)
        if(a[k]==a[k-1])
        b[0][p]++;
        else
        {p++;
        b[0][p]++;
        c[p]=a[k];
        }
        lm=p;
        flg=0;
        for(j=1;j<n;j++)
        {
            cin>>a;
        l=a.size();
        b[j][0]++;
        p=0;
        if(c[p]!=a[0])
        {
            flg=1;
        }
        for(k=1;k<l;k++)
        if(a[k]==a[k-1])
        b[j][p]++;
        else
        {p++;
        b[j][p]++;
        if(c[p]!=a[k])
        {
            flg=1;
        }
        }
        if(lm!=p)
        flg=1;

        }
        cnt=0;
        for(k=0;k<=lm;k++)
        {
            //cout<<k<<endl;
            for(j=0;j<n;j++)
            d[j]=b[j][k];
            sort(d,d+n);
            l=0;r=n-1;
            while(l<r)
            {
               cnt=cnt+abs(d[l]-d[l+1]);
               if(l+1<r)
               cnt=cnt+abs(d[r]-d[r-1]);

               d[l+1]=d[l+1]+d[l];
               d[r-1]=d[r-1]+d[r];
               r--;l++;
               //cout<<cnt<<endl;
            }
        }
        cout<<"Case #"<<i<<": ";
        if(flg==1)
        cout<<"Fegla Won"<<endl;
        else
        cout<<cnt<<endl;
    }

    return 0;
}


