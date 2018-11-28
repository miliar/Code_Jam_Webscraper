#include <bits/stdc++.h>
using namespace std;

#define rep(i,x,y) for(int i=(x);i<(y);++i)
#define debug(x) #x << "=" << (x)

#ifdef DEBUG
#define _GLIBCXX_DEBUG
#define dump(x) std::cerr << debug(x) << " (L:" << __LINE__ << ")" << std::endl
#else
#define dump(x)
#endif

typedef long long int ll;
typedef pair<int,int> pii;
//template<typename T> using vec=std::vector<T>;

const int inf=1<<30;
const long long int infll=1LL<<58;
const double eps=1e-9;
const int dx[]={1,0,-1,0},dy[]={0,1,0,-1};

template <typename T> ostream &operator<<(ostream &os, const vector<T> &vec){
    os << "[";
    for (const auto &v : vec) {
    	os << v << ",";
    }
    os << "]";
    return os;
}

void solve(){
    int t;
    cin >> t;
    rep(iiiiiiiiiiiii,0,t){
        ll n;
        cin >> n;
        if(n==0){
            cout << "Case #" << iiiiiiiiiiiii+1 <<  ": INSOMNIA" << endl;
            continue;
        }

        bool done[10];
        ll cnt=0,i=1,ans;
        fill_n((bool*)done,10,false);
        while(true){
            stringstream ss;
            ss << n*i;
            string str=ss.str();
            rep(j,0,str.size()) if(!done[str[j]-'0']){
                done[str[j]-'0']=true;
                ++cnt;
            }
            if(cnt==10){
                dump(i);
                ans=n*i;
                break;
            }
            ++i;
        }
        cout << "Case #" << iiiiiiiiiiiii+1 << ": "  <<  ans << endl;
    }
}

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);
    cout << fixed << setprecision(8);
    solve();
    return 0;
}
