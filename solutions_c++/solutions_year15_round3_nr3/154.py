#include<bits/stdc++.h>

using namespace std;


bool okay(set<int>avail,int v){
    vector<bool> ok(v+1,false);
    ok[0]=true;
    for(auto x : avail){
        for(int k =v;k>=0;--k){
            if(ok[k]&&k+x<=v)ok[k+x]=true;
        }
    }
    for(int i = 0 ; i <= v ; ++ i ){
        if(!ok[i])return false;
    }
    return true;
}

void solve(){
    int c,d,v;
    cin >> c >> d >> v;
    vector<int> D;
    vector<bool> ok(v+1,false);
    for(int i = 0 ; i < d;  ++ i ){
        int k ;
        cin >> k;
        D.push_back(k);
    }
    int ans=v;
    for(int i = 0 ; i < (1<<15) ; ++ i ){
        set<int> avail(D.begin(),D.end());
        for(int j = 0 ; j < 15 ; ++ j ){
            if( (1<<j)&i){
                avail.insert(j+1);
            }
        }
        if(okay(avail,v)){
            ans=min(ans,(int)avail.size()-d);
        }
    }
    cout << ans << endl;
}
void solveLarge(){
    long long c,d,v;
    cin >> c >> d >> v;
    long long  mx=0;
    int toAdd=0;
    for(int i = 0 ; i < d ; ++ i ){
        long long k;
        cin >> k;
        while(mx+1<k){
            if(mx==0){
                mx=c;
                toAdd=1;
            }
            else{
                // need to insert mx
                mx+=(mx+1)*c;
                toAdd++;
            }
        }
        mx+=c*k;
    }
    while(mx<v){
        if(mx==0){
            mx=c;
            toAdd=1;
        }
        else{
            // need to insert mx
            mx+=(mx+1)*c;
            toAdd++;
        }
    }
    cout <<toAdd<<endl;
}
int main(){
    freopen("C-large"".in","r",stdin);
    freopen("C-large"".out","w",stdout);
    int T;
    cin >> T;
    for(int i = 1 ; i <= T ; ++ i ){
        cout <<"Case #" <<i <<": ";
        solveLarge();
    }
    return 0;
}
