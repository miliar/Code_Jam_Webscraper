#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string>
#define forn(a,b) for(int a = 0; a < int(b); ++a)
#define forr(a,c,b) for(int a = int(c); a < int(b); ++a)
using namespace std;
typedef long long ll;
const int maxn = 1024;
const char L[] = "PRS";

int T, N, R, P, S;
int A[3];

string dp(int n, int level){
    if( level == 0 ){
        A[n]++;
        return string(1, L[n]);
    }
    int opp = ( n + 1 ) % 3;
    string a = dp(n, level-1);
    string b = dp(opp, level-1);
    if( a < b ) return a + b;
    else        return b + a;
}

int main(){
    freopen("large.txt", "r", stdin);
    freopen("salida.txt", "w", stdout);

    scanf("%i", &T);
    forn(t, T){
        scanf("%i%i%i%i", &N, &R, &P, &S);
        string Ans = "";
        forn(i, 3){
            string seq = dp(i, N);
            if( A[0] == P and A[1] == R and A[2] == S )
                if( Ans == "" or seq < Ans )
                    Ans = seq;
            forn(j, 3) A[j] = 0;
        }
        if( Ans == "" ) Ans = "IMPOSSIBLE";
        printf("Case #%i: %s\n", t+1, Ans.c_str());
    }

    return 0;
}

