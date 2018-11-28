
 #include <bits/stdc++.h>

//#define NDEBUG ;
#ifdef NDEBUG
#define debug(x) ;
#define print(x) ;
#else
#define debug(x) cerr << #x << ": " << x << endl;
#define print(x) cerr<<x<<endl;
#endif

#define mp make_pair
#define pb push_back
#define all(x) (x).begin() , (x).end()
#define rall(x) (x).rbegin() , (x).rend()
#define REP(i,x,y) for(int i=x;i<y;i++)
//#define REPIT(it,A) for(typeof(A.begin()) it = (A.begin()); it!=A.end();it++)
#define fst first
#define snd second
#define sqr(x) ((x)*(x))

#define fast_io() ios_base::sync_with_stdio(0);cin.tie(0);
#define ones(x) __builtin_popcount(x)
using namespace std;

typedef pair<int,int> ii ;
typedef long long ll ;
typedef vector<int> vi;
typedef vector<ii> vii;

set<int> used;

void getDigits(ll cur){
    
    while(cur){
        int d = cur%10;
        cur /= 10;
        used.insert(d);
    }
}

int main(){
    fast_io(); 

    int T;
    cin >> T;
    ll n;
    for(int caso = 1; caso <= T; caso++){
        used.clear();
        cin >> n;
        cout<<"Case #"<<caso<<": ";
        if(n == 0){
            cout<<"INSOMNIA"<<endl;
        }else{
            ll cur = n;
            
            while(true){
                getDigits(cur);
                bool flg = true;
                for(int i = 0; i < 10; i++){
                    if(used.count(i) == 0){
                        flg = false;
                        break;
                    }
                }
                if(flg) break;
                cur += n;
            }
            cout<<cur<<endl;
        }
    }
    

    return 0;
}
