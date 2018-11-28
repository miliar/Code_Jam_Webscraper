#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define int long long

int find_div(ll num){
    for(ll i = 2 ; i*i <= num ; i++){
        if(num %i == 0){
            return i;
        }
    }
    return 1;
}

ll get(string num, int base){
    ll ret = 0;
    ll now = 1;
    reverse(num.begin(), num.end());
    for(auto it : num){
        ret += (it - '0')*now;
        now *= base;
    }
    return ret;
}

vector<int> check(ll num){
    vector<int> ret;
    string numStr = "";
    for(int i = 32; i >=  0; i--){
        if(((num >> i)&1ll) == 0){
            if(!numStr.empty()){
                numStr += "0";
            }
        }else{
            numStr += "1";
        }
    }
    for(int i = 2 ;i <= 10; i++){
        int div = find_div(get(numStr, i));
        if(div == 1)
            return {-1};
        ret.push_back(div);
    }
    return ret;
}
#undef int
int main(){
#define int long long
    srand(time(0));
    int test;
    cin >> test;
    for(int t = 1 ; t <= test;t ++){
        cout << "Case #1:" << endl; 
        int len, num;
        cin >> len >> num;
        set<pair<int, vector<int> > > ans;
        for(long long i= 0 ;i < (1ll << (len-2)) ; i++){
            long long j = i;
            j <<= 1;
            j |= 1ll;
            j |= 1ll << (len-1);
            if((int)ans.size() == num){
                break;
            }
            vector<int> vec = check(j);
            if(vec[0] != -1){
                ans.insert(make_pair(j, vec));
            }
        }
        for(auto it : ans){
            for(int i = len -1 ; i >= 0 ; i --){
                cout << ((it.first >> i)&1ll);
            }
            for(auto itt : it.second){
                cout << " " << itt ;
            }
            cout << endl;
        }
    }
    
    return 0;
}
