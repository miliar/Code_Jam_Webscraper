#include <bits/stdc++.h>
using namespace std;
#define mp make_pair
#define pb push_back
#define f first
#define s second
typedef long long ll;
const int MAX = 10000008;
int n,r,p,s;

string build(int s,int e,char c){
    if(s==e){
        string r ="";
    r += c;
        return r;
    }
    if(c=='R'){
        return min( build(s,(s+e)/2,'R')+build((s+e)/2+1,e,'S') , build(s,(s+e)/2,'S')+build((s+e)/2+1,e,'R') );
    }
    if(c=='P'){
        return min( build(s,(s+e)/2,'P')+build((s+e)/2+1,e,'R') , build(s,(s+e)/2,'R')+build((s+e)/2+1,e,'P') );
    }else{
        return min( build(s,(s+e)/2,'P')+build((s+e)/2+1,e,'S') , build(s,(s+e)/2,'S')+build((s+e)/2+1,e,'P') );
    }
}

string fun(char c){
    string sol = build(0,(1<<n)-1,c);
    ///
//    cout << c << " " << sol << endl;
    int cnt[3] = {0};
    for(int i=0;i<(int)sol.size();i++){
        if(sol[i]=='R') cnt[0]++;
        if(sol[i]=='P') cnt[1]++;
        if(sol[i]=='S') cnt[2]++;
    }
    if(r<cnt[0] || p<cnt[1] || s<cnt[2]) return "IMPOSSIBLE";
    return sol;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,tc(1);
    cin >> T;
    while(T--){
        cin >> n >> r >> p >> s;
        string a = fun('R');
        string b = fun('S');
        string c = fun('P');
//        cout << n << " " << r << " " << p << " " << s << endl;
        string ans = a;
        if(b!="IMPOSSIBLE"){
            if(ans=="IMPOSSIBLE") ans = b;
            else ans = min(ans,b);
        }
        if(c!="IMPOSSIBLE"){
            if(ans=="IMPOSSIBLE") ans = c;
            else ans = min(ans,c);
        }
        cout << "Case #" << tc++ << ": " << ans << endl;
    }
    return 0;
}
