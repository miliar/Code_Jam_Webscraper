
#pragma comment(linker,"/STACK:16777216")
#pragma  warning ( disable: 4786)
#include <bits/stdc++.h>
using namespace std;

#define max(x,y) ((x)>(y)?(x):(y))
#define min(x,y) ((x)<(y)?(x):(y))

#define forl(i,a,b) for ( i = a; i < b; i++)
#define fore(i,a,b) for ( i = a; i <= b; i++)
#define forrev(i,a,b) for ( i = a; i >= b; i--)
#define MID(a, b) (a + ((b - a) >> 1))
#define pb push_back
typedef long long  LL;
#define in(a,b,c) ((a) <= (b) && (b) <= (c))
#define ms(a,b) memset((a),(b),sizeof(a))

#define all(v) (v).begin(),(v).end()
#define pb push_back
#define ull unsigned long long int
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

string to_string(long long x) { stringstream ss; ss << x; return ss.str(); }
long long to_int(const string &s) { stringstream ss; ss << s; long long x; ss >> x; return x; }

#define MAX 11
#define INF 9999999

bool vis[MAX];
unsigned long long int n;
bool isAllTaken(){
    int i;
    forl(i,0,10){
        if(vis[i]==false)
            return false;
    }
    return true;
}
void makeItvisited(ull n){
    while(n){
        vis[n%10]=true;
        n /=10;
    }
}
int main(void)
{
    freopen("A-large.txt", "r", stdin);
    freopen("2_large.txt", "w", stdout);
    int t;
    int ca=1;
    cin >> t;
    ull i;
    while(t--){
        cin >> n;
        
        ms(vis,false);
        
        cout << "Case #" << ca++ << ": ";
        if(n==0){
            cout << "INSOMNIA\n";
            continue;
        }
        forl(i,1,73){
            makeItvisited(n*i);
            if(isAllTaken()){
                break;
            }
        }
        if(i==73){
            cout << "INSOMNIA\n";
            //cout << n << endl;
        }else{
            cout << n*i << endl;
        }
    }
    return 0;
}
