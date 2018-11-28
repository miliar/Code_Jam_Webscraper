#include <map>
#include <set>
#include <cmath>
#include <stack>
#include <queue>
#include <cstdio>
#include <vector>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

#define rep(i,n) for(int i=0; i<n; i++)
#define fr(i,a,b) for(int i=a; i<=b; i++)
#define debug(a) cout<< #a << " = " <<a<<endl;

#define ff first
#define ss second
#define mp make_pair
#define pb push_back

#define MaxInt 2147483647
#define INF 12512523232344LL
#define pi 3.1415926535897932

#define read(a) scanf("%d",&a);
#define read2(a,b) scanf("d",&a,&b);
#define read3(a,b,c) scanf("d%d",&a,&b,&c);

int T,n;
double a[2000],b[2000];
vector<double> va,vb;

int main(){

    #ifndef ONLINE_JUDGE
    freopen("INPUT.INP", "r", stdin);
    freopen("OUTPUT.OUT", "w", stdout);
    #endif // ONLINE_JUDGE

    cin>>T;

    fr(Tc,1,T)
    {

        int f=0,s=0;
        va.clear();
        vb.clear();

        cin>>n;

        rep(i,n) cin>>a[i];
        rep(i,n) cin>>b[i];

        sort(a,a+n);
        sort(b,b+n);

        rep(i,n)
        {
            va.pb(a[i]);
            vb.pb(b[i]);
        }

        int i =0,j=0;

        while(i<n && j<n)
        {
            if(a[i] > b[j])
            {
                i++;
                j++;
                f++;
            }
            else
            {
                i++;
            }
        }


        bool cha[2000],chb[2000];

        memset(cha,true,sizeof(cha));
        memset(chb,true,sizeof(chb));

        for( i = 0; i < n; i++)
        {
            for(j = 0 ; j<n; j++)
            {
                if(chb[j] && a[i] < b[j])
                {
                   cha[i] = false;
                   chb[j] = false;
                   break;
                }
            }
        }

        int cnta = 0,cntb=0;

        rep(i,n)
        {
            if(cha[i]) cnta++;
            if(chb[i]) cntb++;
        }

        s = min(cnta,cntb);

        printf("Case #%d: %d %d\n",Tc,f,s);
    }


return 0;
}
