#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long long LL;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

#ifdef DEBUG
    #define cek(x) cout<<x
#else
    #define cek(x) if(false){}
#endif // DEBUG

#define fi first
#define se second
#define INF 1000000000
#define INFLL 1000000000000000000LL
#define EPS 1e-9
#define PI acos(-1.0)
#define pb push_back
#define TC() while(tc--)
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORN(i,n) for(int i=0;i<=n;i++)
#define REP(i,a,b) for(int i=a;i<b;i++)
#define REPN(i,a,b) for(int i=a;i<=b;i++)
#define reset(a,b) memset(a,b,sizeof(a))
#define sci(x) scanf("%d",&x)
#define scs(x) scanf("%s",&x)

bool ansExist;
int tci;

bool test(string ans){
    if(ans.length() == 1) return true;
    string newString = "";
    for(int i=0;i<ans.length();i++){
        if(i%2==0){
            if(ans.at(i)==ans.at(i+1)) return false;
            if(ans.at(i)=='R')
            {
                if(ans.at(i+1) == 'P') newString += "P";
                else newString += "R";
            } else if (ans.at(i)=='P'){
                if(ans.at(i+1) == 'S') newString += "S";
                else newString += "P";
            } else {
                if(ans.at(i+1) == 'R') newString += "R";
                else newString += "S";
            }
        }
    }
    return test(newString);
}

void brute(int R, int P, int S, string ans){
    if(R+P+S == 0)
    {
        if(test(ans))
        {
            ansExist = true;
            cout << "Case #" << tci+1 << ": " << ans << endl;
        }
    } else {
        if(P > 0 && !ansExist) {
            brute(R,P-1,S,ans+"P");
        }
        if(R > 0 && !ansExist) {
            brute(R-1,P,S,ans+"R");
        }
        if(S > 0 && !ansExist) {
            brute(R,P,S-1,ans+"S");
        }
    }
}

int main(void){
    freopen("D:/Code/A-small-attempt1.in","r",stdin);
    freopen("D:/Code/out.txt","w",stdout);

    int tc;
    sci(tc);

    for(tci=0;tci<tc;tci++)
    {
        ansExist = false;
        int N;
        int R,P,S;
        sci(N);
        sci(R);
        sci(P);
        sci(S);
        brute(R,P,S,"");

        if(!ansExist){
            cout << "Case #" << tci+1 << ": IMPOSSIBLE" << endl;
        }
    }


    return 0;
}
