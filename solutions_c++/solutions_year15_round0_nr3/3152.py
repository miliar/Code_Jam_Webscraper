#include <bits/stdc++.h>
#define push_back pb
using namespace std;
typedef long long ll;

ll M[5][5] =  { {0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
ll n;

bool solve(string t, ll st, ll cr)
{
     //if ( cr == 4 && st == n)
       // return true;
     if (cr == 4){
         ll vv = t[st] - '0';
         ll ml = 1;
         ll i ;
         for ( i = st+1; i < n; i++) {
             if ( vv < 0)
                ml = -1;
             else
                 ml = 1;

             vv = M[abs(vv)][t[i] - '0'];
             vv *= ml;

             }
            if (vv == 4){
                    return true;
            } else {
                   return false;
            }

     }

     /*k.clear();
        for (ll i=0;i<n;i++){
            cin>>p[i];
            k.pb(p[i]);
        }
        sort (p, p+n);
        ll ans = 10000;
        for (ll i=1; i<=10;i++){
            ll mx = 0;
            vector<ll> g;
            g.clear();
            for (ll j=0;j<n;j++){
                if (p[j] > i){
                    g.pb(p[j]);
                } else {
                    mx = max (mx, p[j]);
                }
            }*/


     ll vv = t[st] - '0';
     ll ml = 1;
     ll i ;
     for ( i = st+1; i < n; i++) {
          if ( vv == cr)
            return solve(t, i,cr+1);
         if ( vv < 0)
            ml = -1;
         else
             ml = 1;

         vv = M[abs(vv)][t[i] - '0'];
         vv *= ml;

         }
         return false;
}

bool solve1(string t, int st, int cr)
{

     int val = t[st] - '0';
     int mult = 1;
     int i ;
     for ( i = st+1; i < n; i++) {
          if ( val == cr)
            return solve1(t, i,cr+1);
         if ( val < 0)
            mult = -1;
         else
             mult = 1;

         val = M[abs(val)][t[i] - '0'];
         val *= mult;

         }
         return false;
}

int main(){
   freopen("asd.txt", "r", stdin);
    freopen("qw.txt", "w", stdout);

    ll t;
    cin>>t;
    ll cc = 1;
    while (t--){
        ll a,b;
        string s;

        cin>>a>>b;
        cin>>s;
        ll temp;
        for ( ll i = 0 ; i < s.length(); i++) {
            if (s[i] == 'i')
               s[i] = '2';
            else if ( s[i] == 'j')
                 s[i] = '3';
            else
                s[i] = '4';
                }

                string t = "";
                while (b--){
                      t += s;
                }
                n = t.size();
                //cout<<t<<"\n";
                //cout<<"Case #"<<cc<<": ";
                cout << "Case #";
                cout << cc << ":";
                cc++;
                cout <<" " <<( solve(t,0,2) ? "YES" : "NO") << endl;
    }
    return 0;
}
