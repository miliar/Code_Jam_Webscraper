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
set<int> di;

string foo(string s){
    string ret = "";
    int n = s.size();
    int st = n-1;
    for(int i = n-1; i >= 0; --i){
        if(s[i] == '-'){
            st = i;
            break;
        }
    }
    for(int i = 0; i <= st; ++i){
        if(s[i] == '+'){
            ret += '-';
        }
        else{
            ret += '+';
        }
    }
    return ret;
}

bool check(string s){
    fori(i, 0, s.size()){
        if(s[i] == '-')
            return false;
    }
    return true;
}

int main()
{
   freopen("in.in", "r", stdin);
   freopen("out.txt", "w", stdout);
    int t;
    Sc(t);
    for(int tc = 1; tc <= t; ++tc){
        printf("Case #%d: ", tc);
        string s;
        cin>>s;
        int ans = 0;
        while(true){
            if(check(s)){
                break;
            }
            ans++;
            s = foo(s);
        }
        cout<<ans<<endl;
    }
    return 0;
}
