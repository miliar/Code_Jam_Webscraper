#include <bits/stdc++.h>
#define ll long long 
#define mp make_pair
#define pb(a) push_back(a) 
#define pii pair<int,int> 
#define mii map<int,int>
#define rep(i,a) for(int i = 0 ; i < a ; ++i)
using namespace std; 
 
vector<int> vec ; 
long long dp[100][100] ; 
long long go(long long val , long long to){
  //  cout << val << " " << to << "\n" ; 
    if(dp[val][to] != -1){
        return dp[val][to] ; 
    }
    if(val <= to){
        return dp[val][to] = 0 ; 
    } 
    // if((val + 1)/2 <= to){
    //     dp[val][to] = 1 ;
    // }
    for(int part1 = 1; part1 < val ; ++part1){
        int part2 = val - part1 ; 
        if(dp[val][to] == -1){
            dp[val][to] =  1 + go(part1,to) + go(part2,to) ; 
        }
        else{
            dp[val][to] = min(dp[val][to] , 1 + go(part1 , to) + go(part2 , to)) ; 
        }
    }
    return dp[val][to] ; 
}
int main(){
    freopen("B-small-attempt1.in","r",stdin) ; 
    freopen("B-small-attempt1.out","w",stdout) ; 
    int tc; 
    cin >> tc;
    for(int i = 0 ; i < 100 ; ++i){
        for(int j = 0 ; j < 100 ; ++j){
            dp[i][j] = -1 ; 
        }
    }
    for(int t = 1 ; t <= tc;  ++t){
        cout << "Case #"<<t<<": " ; 
        long long N ; 
        cin >> N ;
        vec.clear() ; 
        vec.resize(N)  ;
        for(int i = 0; i < N ; ++i){
            cin >> vec[i] ;
        }
        long long ans = 10000000000LL , ops = 0  ; 
        for(int max_value = 1; max_value <= 9 ; ++max_value){
            ops = 0 ; 
            for(int i = 0 ; i < N ; ++i){
                if(vec[i] <= max_value){
                    continue; 
                }
                ops += go(vec[i] , max_value) ; 
                //cout << "FROM " << vec[i] << " TO " << max_value << " OPERATIONS = " << dp[vec[i]][max_value] << "\n" ; 
            }
          //  cout << max_value << " " << ops << "\n" ; 
            ans = min(ans , max_value + ops) ; 
        } 
        cout << ans << "\n" ; 
    } 
    return 0 ; 
}