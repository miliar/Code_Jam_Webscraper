#include <bits/stdc++.h>

using namespace std;
int n , R , P , S ;
int tab[13][100000];
int get(int a, int b){
    if(a>b) return get(b , a) ;
   if( a==b ) return -1;
   if( a==1 && b == 2) return 1 ;
   if( a==1 && b == 3) return 3 ;
   if( a== 2 && b == 3) return 2 ;
}
bool verifier(){
    for(int i = n-1 ; i>=0 ; i--){
        for(int j = 0 ; j < (1<<i) ; j++)
        {
            tab[i][j]= get(tab[i+1][2*j] , tab[i+1][j*2+1]);
            if(tab[i][j]==-1) return false;
        }
    }
    return true;
}

bool cas(int p , int r , int s , int l){
    if(l==(1<<n)) if(verifier()) return true ;
    if(p) {
        tab[n][l]=1;
        if (cas(p-1 , r , s , l+1)) return true  ;
    }
    if(r) {
        tab[n][l]=2;
        if(cas(p , r-1 , s , l+1)) return true ;
    }
    if(s) {
        tab[n][l]=3;
        if(cas(p , r , s-1 , l+1) ) return true ;
    }
    return false ;
}
int main()
{
    ifstream cin("A-small-attempt0 (2).in") ;
    ofstream cout("out.txt");
    int t ;
    cin >> t ;
    int cp=1;
    while(t--){
            cout << "Case #" << cp++ << ": " ;
        cin >> n >> R >> P >> S ;
        if(cas(P,R,S,0)) {
            for(int i = 0  ; i<(1<<n) ; i++){
                if( tab[n][i]==1)
                    cout << 'P' ;
                else if(tab[n][i]==2) cout << 'R' ;
                else cout << 'S' ;
            }
        }
        else cout << "IMPOSSIBLE" ;
        cout <<endl;
    }
    return 0;
}
