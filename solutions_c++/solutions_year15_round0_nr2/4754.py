#include<iostream>
#include<queue>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> v;
int solve(){
    int ans = 10005,tmp=1;
    for(int i=1;i<=1000;i++){
        tmp = i;
        for(int j=0;j<v.size();j++){
            tmp += (v[j]-1) / i ;
        }
        //cout << "i: " << i << " " << tmp << "\n";
        ans = min(ans,tmp);
    }
    return ans;
}
int main (){
    int Z,D;
    cin >> Z;
    for(int ca = 1; ca <= Z;ca ++){
        cin >> D;
        v.clear();
        for(int i=0;i<D;i++){
            int p;
            cin >> p;
            v.push_back(p);
        }
        cout << "Case #" << ca << ": " << solve() << "\n";
    }
    return 0;
}
