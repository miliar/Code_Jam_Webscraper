#include <bits/stdc++.h>
#define MAX 1000001
using namespace std;

long long int flip(long long int num){
    int new_num = 0LL;
    while(num > 0LL)
    {
            new_num = new_num*10LL + (num % 10LL);
            num = num/10LL;
    }

    return new_num;
}
long long int dp[MAX];
for(int i=0; i<MAX; i++) dp[i] = -1;

long long int solve( long long int n ){
    if( dp[n] != -1 ) return dp[n];
    if( n == 1LL ) return 1LL;
    long long int fp = flip(n);
    if( fp < n )
        return dp[n] = 1LL+min( solve( fp ), solve(n-1) );
    else return dp[n] = solve(n-1);
}

int main(){
    freopen("A-small-attempt3.in","r",stdin);
    freopen("A_small.out","w",stdout);
    int T;
    cin >> T;

    for(int c=1; c<=T; c++){
        long long int n;
        cin >> n;
        long long int ans = 0LL;
        queue< long long int > q;
        q.push(1LL);
        set< long long int > v;
        map< long long int, long long int > d;
        d[1LL] = 1LL;
        while( !q.empty() ){
            long long int c = q.front(); q.pop();
            if( c == n ) break;
            long long int fp = flip(c);
            long long int xd = d[c];

            if( v.count( fp ) == 0 ){
                v.insert( fp );
                q.push( fp );
                d[fp] = xd + 1LL;
            }
            if( v.count(c+1LL) == 0 ){
                v.insert( c+1LL );
                q.push( c+1LL );
                d[c+1LL] = xd + 1LL;
            }

        }

        cout << "Case #"<<c<<": "<< d[n] << endl;
    }
}
