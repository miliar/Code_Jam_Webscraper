//Love Sucks!!!

#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define Sl(x) scanf("%lld",&x)
#define Su(x) scanf("%llu",&x)
#define all(v) v.begin(),v.end()
#define Sc(x) scanf("%d",&x)
#define P(x) printf("%d", x)
#define nl() printf("\n");
#define F first
#define S second
#define pii pair<int, int>
#define MOD 1000000007
#define pb push_back
#define mp make_pair
#define mem(x,i) memset(x,i,sizeof(x))
#define fori(i,s,n) for(int i=(s);i<(n);++i)
#define ford(i,s,n) for(int i=(n)-1;i>=(s);--i)
#define INF 8944674407370955161LL
#define debug(i,st,arr) fori(i,0,st){cout<<arr[i]<<" ";}cout<<endl;
#define forci(i,sw) for((i)=(sw).begin();(i)!=(sw).end();(i)++)
#define forcd(i,sw) for((i)=(sw).rbegin();(i)!=(sw).rend();(i)++)
#define sync() ios_base::sync_with_stdio(0)

ll abs(ll x) {if(x < 0) return -x; return x;}

int addmod(int v1, int v2) {
    int v3 = v1+v2;
    if(v3 >= MOD) v3 -= MOD;
    return v3;
}

#define MAX 100005//maximum value of n goes here!!
map< int, string> dig;

int main()
{
    freopen("in.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    dig[0] = "ZERO";
    dig[1] = "ONE";
    dig[2] = "TWO";
    dig[3] = "THREE";
    dig[4] = "FOUR";
    dig[5] = "FIVE";
    dig[6] = "SIX";
    dig[7] = "SEVEN";
    dig[8] = "EIGHT";
    dig[9] = "NINE";
    int t;
    cin>>t;
    for(int tc = 1; tc <= t; ++tc){
        cout<<"Case #"<<tc<<": ";
        string s;
        int hs[26];
        mem(hs, 0);
        cin>>s;
        fori(i, 0, s.size()){
            hs[s[i]-'A']++;
        }
        string ans = "";
        while(hs['Z'-'A']){
            ans += '0';
            string tp = dig[0];
            for(int i = 0; i < tp.size(); ++i){
                hs[tp[i]-'A']--;
            }
        }
        while(hs['G'-'A']){
            ans += '8';
            string tp = dig[8];
            for(int i = 0; i < tp.size(); ++i){
                hs[tp[i]-'A']--;
            }
        }
        while(hs['W'-'A']){
            ans += '2';
            string tp = dig[2];
            for(int i = 0; i < tp.size(); ++i){
                hs[tp[i]-'A']--;
            }
        }
        while(hs['S'-'A']){
            if(hs['X'-'A']){
                ans += '6';
                string tp = dig[6];
                for(int i = 0; i < tp.size(); ++i){
                    hs[tp[i]-'A']--;
                }
            }
            else if(hs['V'-'A']){
                ans += '7';
                string tp = dig[7];
                for(int i = 0; i < tp.size(); ++i){
                    hs[tp[i]-'A']--;
                }
            }
        }
        while(hs['F'-'A']){
            if(hs['U'-'A']){
                ans += '4';
                string tp = dig[4];
                for(int i = 0; i < tp.size(); ++i){
                    hs[tp[i]-'A']--;
                }
            }
            else if(hs['V'-'A']){
                ans += '5';
                string tp = dig[5];
                for(int i = 0; i < tp.size(); ++i){
                    hs[tp[i]-'A']--;
                }
            }
        }
        while(hs['N'-'A']){
            if(hs['O'-'A']){
                ans += '1';
                string tp = dig[1];
                for(int i = 0; i < tp.size(); ++i){
                    hs[tp[i]-'A']--;
                }
            }
            else if(hs['I'-'A']){
                ans += '9';
                string tp = dig[9];
                for(int i = 0; i < tp.size(); ++i){
                    hs[tp[i]-'A']--;
                }
            }
        }
        while(hs['R'-'A']){
            ans += '3';
            string tp = dig[3];
            for(int i = 0; i < tp.size(); ++i){
                hs[tp[i]-'A']--;
            }
        }
        sort(ans.begin(), ans.end());
        cout<<ans<<endl;
    }
    return 0;
}
