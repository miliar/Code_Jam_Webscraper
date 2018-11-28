#include <bits/stdc++.h>

using namespace std;
int n , k ;
double p[203];
double dp[66000][16][16];
double solve(int a ,int yes , int no ){
    if(yes==-1) return 0 ;
    if(no==-1) return 0;
    if(a==0) return 1 ;
    if(dp[a][yes][no]!= -1.0) return dp[a][yes][no];
    for(int i =0 ; i< n ; i++){
        if((1<<i)&a) dp[a][yes][no] = p[i]*solve(a-(1<<i) , yes-1 , no) + (1-p[i]) * solve(a-(1<<i) , yes , no - 1) ;
    }
    //cout << dp[a][yes][no] <<endl;;
    return dp[a][yes][no] ;
}



int main()
{
    ifstream cin("B-small-attempt0 (2).in") ;
    ofstream cout("out.txt");
    int t ;
    cin >> t ;
    int cp=1;
    while(t--){

            cout << "Case #" << cp++ << ": " ;
        cin >> n >> k ;
        for(int i= 0 ; i < 66000  ; i ++)for(int j = 0 ; j < 16 ; j ++) for(int k = 0 ; k < 16 ; k++) dp[i][j][k] = -1.0;
        for(int i = 0 ; i < n ; i++){
            cin >> p[i] ;
        }
        double ans = 00.0;
        for(int i = 0 ; i < (1<<n) ; i ++){
            int a = i  , nbr=0;
            while(a){
                nbr++ ;
                a-=a&(-a);
            }
            if(nbr==k)  ans = max(ans , solve(i,k/2,k/2));
        }
        cout << fixed << setprecision(8) << ans;
        cout <<endl;
    }
    return 0;
}
