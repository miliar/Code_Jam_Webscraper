#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define si(x) scanf("%d",&x)
#define sc(ch) scanf(" %c",&ch);
#define sl(x) scanf("%I64d",&x)
#define pi(x) cout << x <<" "
#define nl cout << '\n'
#define mp make_pair
#define pb push_back
#define f first
#define se second
#define pii pair<int,int>
#define RESET(a) memset(a,-1,sizeof(a))
#define CLEAR(a) memset(a,0,sizeof(a))
#define all(v)   v.begin(),v.end()
#define trv(it,v) for(it=v.begin();it!=v.end();it++)
#define rep(i,a,b) for(int i=a;i<b;i++)
#define mod 1000000007
#define MIN INT_MIN
#define MAX INT_MAX
#define INF 10e8
//freopen("out", "w", stdout);

int main()
{
    std::ios::sync_with_stdio(false);
    #ifndef ONLINE_JUDGE
        freopen("input.in", "r", stdin);
        freopen("out2.txt", "w", stdout);
    #endif

    int T,t=1;
    cin >> T;
    while(t<=T){
        int k,c,s;
        cin >> k >> c >> s;
        cout << "Case #"<<t<<": ";
        if(c==1){
            if(s<k)
                cout <<"IMPOSSIBLE";
            else{
                for(int j=1; j<=k; j++)
                    cout <<j<<" ";
            }
        }
        else if(s < (k+1)/2)
           cout <<"IMPOSSIBLE";
        else{

        ll p = 1;
        for(int i=1; i<c; i++)
            p = p*k;

         for(int i=1; i<=(k+1)/2; i++){
            ll idx = i*p - (i-1)*(p/k) - ((c==2) ? 0 : (i-1));
            cout << idx<<" ";
         }
        }
        nl;
        t++;
    }

   return 0;
}
