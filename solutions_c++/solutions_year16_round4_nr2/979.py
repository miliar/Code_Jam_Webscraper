#include <bits/stdc++.h>
typedef long long LL;
using namespace std;
typedef __int128 INT;
struct INIT{INIT(){ios::sync_with_stdio(false);cin.tie(0);cout<<fixed<<setprecision(10);}}init;

template <typename ITR>
bool next_value(int base,ITR bg,ITR ed){
    int c=1;
    for(; bg != ed && c==1; ++bg){
        (*bg)+=c;
        if((c = ((*bg) == base)))(*bg)=0;
    }
    return !c;
}
template <typename T> class svector:private std::vector<T>{
    using V=std::vector<T>;
    using SV=svector;
private:
    int sz;
public:
    using V::begin;
    using V::end;
    svector(int n,T ini):V(n*2+1,ini),sz(n){}
    svector(int n):SV(n,T()){}
    svector():V(),sz(0){}
    int size(){return sz;}
    T& operator[](int id){
        //assert(abs(id)<=sz);
        return V::operator[](id+sz);
    }
    SV& copy(const SV &other){
        V::operator=(other);
        sz=other.sz;
        return (*this);
    }
    SV& operator=(const SV& other){
        return copy(other);
    }
};

void solve(){
    int N,K;
    cin>>N>>K;
    vector<int> use(N,0);
    vector<double> p(N);
    for(auto& it : p)cin>>it;
    double res=0;
    do{
        int cnt=0;
        svector<double> dp(1);
        dp[0]=1;
        for(int i = 0; i < N; i++)
            if(use[i]){
                svector<double> nxt(dp.size()+1);
                for(int j = -dp.size(); j <= dp.size(); j++){
                    nxt[j+1]+=dp[j]*p[i];
                    nxt[j-1]+=dp[j]*(1-p[i]);
                }
                swap(dp,nxt);
                cnt++;
            }
        if(cnt==K)res=max(res,dp[0]);
    }while(next_value(2,use.begin(),use.end()));
    cout << res;
}

int main() {
    int T; cin >> T;
    for(int i = 1; i <= T; i++){
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }
    return 0;
}
