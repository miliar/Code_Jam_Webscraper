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
    freopen("D-small-attempt1.in","r",stdin);
    freopen("D-small-attempt1.out","w",stdout);

    long  i,t,x,r,c,p;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>x>>r>>c;
        p=1;
        if(x==1)
        p=0;
        else if(x==2)
        {
            if(r%2==0||c%2==0)
            p=0;
        }
        else if(x==3)
        {
            if(r==2&&c==3||r==3&&c==2||r==4&&c==3||r==3&&c==4||r==3&&c==3)
            p=0;
        }
        else if(x==4)
        {
            if(r==4&&c==4||r==4&&c==3||r==3&&c==4)
            p=0;
        }
        if(p==0)
        cout<<"Case #"<<i<<": GABRIEL"<<endl;
        else
        cout<<"Case #"<<i<<": RICHARD"<<endl;
    }

    return 0;
}


