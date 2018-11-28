// Headers
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cassert>
#include<vector>
#include<map>
#include<fstream>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
#include<bitset>
#include<set>
using namespace std;
// Global declarations
typedef long long int ll;
typedef vector<int> vi;
typedef vector<char> vc;
typedef pair<int,int> pi;
const double eps = 1e-6;
int const mod  = 1e9+7;
int const INF = 1<<29;
// Macros
#define mp make_pair
#define el putchar('\n')
#define sp putchar(' ')
#define Fill(a,val) memset(a,val,sizeof a)
#define pb push_back
#define ppb pop_back
#define gcd __gcd
#define all(a) a.begin(),a.end()
#define ff first
#define ss second

char keyboard[100];
vector<string> v;

void f(string &S,int s){
    if(s == 0){
        v.pb(S);
    }
    else {
        int ln = strlen(keyboard);
        for(int i=0;i<ln;++i){
            char c = keyboard[i];
            S += c;
            f(S,s-1);
            S.erase(S.begin()+S.length()-1,S.begin()+S.length());
        }
    }
}

int main(){
    freopen("ip.in","r",stdin);
    freopen("op.out","w",stdout);
    int t,x=1;
    cin>>t;
    while(t--){
        int k,l,s;
        cin>>k>>l>>s;
        cin>>keyboard;
        char target[l];
        cin>>target;
        v.clear();
        string S;
        f(S,s);
        int sz = v.size();
        int mx = 0;
        int sum = 0;
        for(int i=0;i<sz;++i){
            string buf = v[i];
            int cnt = 0;
            int n = buf.length();
            int m = strlen(target);
            for(int j=0;j+m-1<n;++j){
                bool match = true;
                for(int jj=0;jj<m;++jj){
                    if(buf[j+jj] != target[jj]) {
                        match = false;break;
                    }
                }
                if(match) ++cnt;
            }
            sum += cnt;
            mx = max(mx , cnt);
        }
        double ans = (double)mx - (double)sum/(double)sz;
        printf("Case #%d: %.12lf\n",x++,ans);
    }
    return 0;
}
