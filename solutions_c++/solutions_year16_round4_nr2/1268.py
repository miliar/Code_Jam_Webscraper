//problem name 
//url

#include  <bits/stdc++.h>//include all stl
#define LL long long
#define ULL unsigned LL
#define FOR(i,n) for(int i=0;i<n;i++)
#define ALL(v) begin(v),end(v)
#define UNIQUE(c) (c).resize(unique(ALL(c)) - (c).begin())
#define PRINT(v,sep) {copy(begin(v), end(v)-1, ostream_iterator<int>(cout, sep)); cout << *(end(v)-1)<<endl;}
#define MAX(v) accumulate(ALL(v),INT_MIN,[](int a,int b){return max(a,b);})
#define MIN(v) accumulate(ALL(v),INT_MAX,[](int a,int b){return min(a,b);})
using namespace std;
template<typename T>
inline T SUM(const vector<T>& v){
    return accumulate(ALL(v),T(0),[](T a,T b){return a+b;});
}

typedef vector<int>   VI;       typedef vector<bool> VB;
typedef vector<VI>   VVI;       typedef vector<double> VD;
typedef vector<VVI> VVVI;       typedef vector<VD> VDD;

typedef pair<int,int> PI;       typedef pair<double,double> PD;
typedef pair<PI,int> PII;

int n,K;
VD probs;
double score(const VI& chosen){
    double res = 0;
    int k = K/2;
    int set = (1 << k) - 1;
    assert(chosen.size()==K);
    while (set < (1<<K)) {
        double cur = 1;
        FOR(j,K) if((set>>j)&1){
            cur*=probs[chosen[j]];
        }else{
            cur*=(1-probs[chosen[j]]);
        }
        res += cur;
        int c = set & -set;// Gosper's hack
        int r = set + c;
        set = (((r^set) >> 2) / c) | r;
    }
    return res;

}
int main(){
    ios::sync_with_stdio(false);
    int T;
    cin>>T;
    FOR(t,T){
        cin>>n>>K;
        probs.assign(n,0);
        FOR(i,n) cin>>probs[i];
        double best = 0;
        int set = (1 << K) - 1;
        while (set < (1<<n)) {
            VI chosen;
            FOR(j,n) if((set>>j)&1)
                chosen.push_back(j);
            best = max(best,score(chosen));
            int c = set & -set;// Gosper's hack
            int r = set + c;
            set = (((r^set) >> 2) / c) | r;
        }
        cout<<"Case #"<<t+1<<": "<<best<<endl;

    }

    return 0;
}
