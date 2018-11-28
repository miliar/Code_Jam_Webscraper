#include <bits/stdc++.h>

using namespace std;

#define FOR(i,a,b)				for (i=a;i<b;i++)
#define s(n)					cin>>n
#define p(n)					cout<<n<<'\n'
#define sd(n)					int n;cin>>n;
#define pb(n)                                   push_back(n)
#define clr(a)                                  memset(a,0,sizeof(a))
#define all(c)                                  (c).begin(),(c).end()
#define tr(container,it)                        for (typeof(container.begin()) it=container.begin();it!=container.end();it++ )
#define sz(a)                                   int((a).size())
#define mp(a,b)                                 make_pair(a,b)
#define ps(str)                                 cout<<str<<'\n'
#define pans(t,ans)                             do{cout<<"Case #"<<t<<": "<<ans<<endl;} while(0)

#define INF                                     INT_MAX
#define UINF                                    UINT_MAX
#define INF_LL                                  LLONG_MAX
#define UINF_LL                                 ULLONG_MAX
#define PI 3.14159265358979323846

typedef vector <int> vi;
typedef vector <vi> vvi;
typedef vector <string> vstr;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<vector<pair<int,int> > > TG;


int main()
{
    //File IO
//    freopen("input.txt","r",stdin);
//    freopen("output.txt","w",stdout);
    ios_base::sync_with_stdio(false);
    sd(T);
    int i,j,t;
    FOR(t,0,T)
    {
        sd(r1);r1--;
        vvi mat1(4,vi(4));
        FOR(i,0,4) FOR(j,0,4) s(mat1[i][j]),mat1[i][j]--;
        sd(r2);r2--;
        vvi mat2(4,vi(4));
        FOR(i,0,4) FOR(j,0,4) s(mat2[i][j]),mat2[i][j]--;
        vi arr(16,0);
        FOR(j,0,4) arr[mat1[r1][j]]++;
        FOR(j,0,4) arr[mat2[r2][j]]++;
        int n1=0,n2=0;
        int ans;
        FOR(i,0,16)
        {
            if (arr[i]==1) n1++;
            else if (arr[i]==2)
            {
                n2++;
                ans=i+1;
            }
        }
        if (n2==0) pans(t+1,"Volunteer cheated!");
        else if (n2>1) pans(t+1,"Bad magician!");
        else pans(t+1,ans);
    }
}
