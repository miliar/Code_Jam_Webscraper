#include <bits/stdc++.h>
using namespace std;

#define FOR(p,star,end) for(int p = star ; p<end ; p++)
#define FORR(p,star,end) for(int p = star ; p>=end ; p--)
#define INF 1000000000
#define MOD 1000000007
#define MAX 101
#define LOGMAX 14
#define pi pair<int ,int >
#define vi vector<int>
#define vp vector< pair<int ,int> >
#define vii vector< vector<int> >
#define vip vector<vector<pair<int , int > > >
#define pb push_back
#define mp make_pair
#define ll long long
#define sz(v) ((int)v.size())
#define f first
#define s second
#define EPS 10-7

using namespace std;
int MAP[20][20];
int dx[]= {0,0,1,-1};
int dy[]= {1,-1,0,0};

int main()
{
    freopen("In.in","r",stdin);
    freopen("out.txt","w",stdout);

    int t;
    cin >> t;
    FOR(O,1,t+1)
    {
        int n , m , k;
        cin >> n >> m >> k;

        vp A;
        FOR(i,0,n)
        FOR(j,0,m)
        A.pb(mp(i,j));


        vi B(n*m,0);

        FORR(i,n*m - 1 ,n*m - k)
        B[i]=1;



        int ans = INF;
        do
        {
            int res=0;
            memset(MAP,0,sizeof MAP);
            FOR(i,0,B.size())
            if(B[i])
                MAP[A[i].f][A[i].s]=1;


            FOR(i,0,n)
            {
                FOR(j,0,m)
                {
                    if(MAP[i][j])
                    {
                        FOR(k,0,4)
                        {
                            int X = i+dx[k];
                            int Y = j+dy[k];
                            if(X>=0 && Y>=0 && X<n && Y<m)
                                if(MAP[X][Y])
                                    res++;
                        }
                    }
                }
            }

            ans = min ( ans , res/2);

          //  cout << res <<endl;


        }
        while(next_permutation(B.begin(),B.end()));

        printf("Case #%d: %d\n",O,ans);

    }


}


