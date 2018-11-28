#include <bits/stdc++.h>
#define ll long long 
#define mp make_pair
#define pb(a) push_back(a) 
#define pii pair<int,int> 
#define mii map<int,int>
#define rep(i,a) for(int i = 0 ; i < a ; ++i)
using namespace std;
struct Quaternion{
    int w , x , y ,z ; 
};
Quaternion mult(Quaternion q1 , Quaternion q2){
    Quaternion ret ;
    ret.w = q1.w*q2.w - q1.x*q2.x - q1.y*q2.y - q1.z*q2.z;
    ret.x = q1.w*q2.x + q1.x*q2.w + q1.y*q2.z - q1.z*q2.y;
    ret.y = q1.w*q2.y + q1.y*q2.w + q1.z*q2.x - q1.x*q2.z;
    ret.z = q1.w*q2.z + q1.z*q2.w + q1.x*q2.y - q1.y*q2.x;
    return ret; 
}
const int MAXN = 10010 ; 
Quaternion pre_prod[MAXN] , suff_prod[MAXN] ; 
int main(){
    freopen("C-small-attempt0.in","r",stdin) ; 
    freopen("C-small-attempt0.out","w",stdout) ; 
    ios_base::sync_with_stdio(0) ; 
    int L , X ; 
    string inp , str;
    int tc;
    cin >> tc; 
    for(int t = 1 ; t <= tc ; ++t){
        cout << "Case #"<<t<<": ";
        cin >> L >> X ; 
        cin >> inp ;
        str = "" ; 
        for(int i = 0 ; i < X ; ++i){
            str += inp ; 
        }
        pre_prod[0].w = 1; 
        pre_prod[0].x = 0 ; 
        pre_prod[0].y = 0 ;
        pre_prod[0].z = 0 ; 
        for(int i = 1 ; i <= str.length() ; ++i){
            Quaternion next;
            next.w = 0 ; 
            next.x = 0 ;
            next.y = 0 ; 
            next.z = 0 ; 
            if(str[i-1] == 'i'){
                next.x = 1; 
            }
            if(str[i-1] == 'j'){
                next.y = 1 ;
            }
            if(str[i-1] == 'k'){
                next.z = 1 ; 
            }
            pre_prod[i] = mult(pre_prod[i-1],next) ; 
        }
        int len = (int)str.length() ; 
        suff_prod[len].w = 1; 
        suff_prod[len].x = 0 ;
        suff_prod[len].y = 0 ; 
        suff_prod[len].z = 0 ;
        for(int i = (int)str.length() - 1;  i >= 0 ; --i){
            Quaternion next;
            next.w = 0 ; 
            next.x = 0 ;
            next.y = 0 ; 
            next.z = 0 ; 
            if(str[i] == 'i'){
                next.x = 1; 
            }
            if(str[i] == 'j'){
                next.y = 1 ;
            }
            if(str[i] == 'k'){
                next.z = 1 ; 
            }
            suff_prod[i] = mult(next,suff_prod[i+1]) ;
        }
        bool ok = false ; 
        int prev_occ = -1 ; 
        for(int i = 1; i < str.length() ; ++i){
            if(pre_prod[i].x == 1 and pre_prod[i].w == 0 and pre_prod[i].y == 0 and pre_prod[i].z == 0){
                prev_occ = i ; 
            }
            if(pre_prod[i].x == 0 and pre_prod[i].w == 0 and pre_prod[i].y == 0 and pre_prod[i].z == 1 and prev_occ != -1){
                if(suff_prod[i].x == 0 and suff_prod[i].w == 0 and suff_prod[i].y == 0 and suff_prod[i].z == 1){
                    ok = true ; 
                    break ;
                }
            }
        }
        if(ok){
            cout << "YES\n" ; 
        }
        else{
            cout << "NO\n" ; 
        }
    }
    return 0 ;
}