#include<bits/stdc++.h>

using namespace std;

int count_bit(int k){
    int ret=0;
    while(k){
        ret++;
        k-=k&(-k);
    }
    return ret;
}


void solve(){
    int r,c,n;
    cin >> r >> c >> n;

    int N=r*c;
    int unhappy=r*c*10;
    for(int i = 0  ; i < (1<<N) ; ++ i ){
        if(count_bit(i)!=n)continue;
        int un=0;
        for(int j = 0 ; j < r ; ++ j ){
            for(int k = 0 ; k < c ; ++ k ){
                if(j+1<r){
                    if( ( i&(1<<(j*c+k)) ) && (i&( 1<<( (j+1)*c+k))))un++;
                }
                if(k+1<c){
                    if( ( i&(1<<(j*c+k)) ) && (i&( 1<<( (j)*c+k+1))))un++;

                }
            }
        }
        unhappy=min(unhappy,un);
    }
    cout <<unhappy<<endl;
}

int main(){
    freopen("B-small-attempt0"".in","r",stdin);
    freopen("B-small-attempt0"".out","w",stdout);
    int T;
    cin >> T;
    for(int i = 1 ; i <= T ; ++ i ){
        printf("Case #%d: ",i);
    solve();
    }
}
