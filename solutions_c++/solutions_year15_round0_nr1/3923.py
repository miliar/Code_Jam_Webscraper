#include <bits/stdc++.h>
#define ll long long 
#define mp make_pair
#define pb(a) push_back(a) 
#define pii pair<int,int> 
#define mii map<int,int>
#define rep(i,a) for(int i = 0 ; i < a ; ++i)
using namespace std; 
 
int main(){
    freopen("A-large.in","r",stdin) ; 
    freopen("A-large.out","w",stdout) ; 
    string str ; 
    int tc;
    cin >> tc;
    for(int t = 1 ; t <= tc ; ++t){
        int len ; 
        cin >> len  ; 
        cin >> str; 
        int got = 0 , ans = 0 ;
        for(int i = 0 ; i <= len ; ++i){
            int need = i  ;
            if(got < need){
                ans += (need - got) ; 
                got += (need - got) ; 
                got += ((str[i] - '0')) ; 
            }
            else{
                got += (str[i] - '0') ; 
            }
        }
        cout << "Case #"<<t<<": "<<ans<<"\n" ; 
    }
    return 0 ;
}