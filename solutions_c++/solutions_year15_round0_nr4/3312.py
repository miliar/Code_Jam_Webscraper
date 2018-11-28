#include <bits/stdc++.h>
using namespace std;
#define REP(a, b, c) for(int a = b; a < c; a++)
#define asd(x)              cout<<__LINE__<<" :: "<<#x<< ": "<<x<<endl;
#define asdf(x, y)          cout<<__LINE__<<" :: "<<#x<< ": "<<x<<" | "<<#y<< ": "<<y<<endl;
typedef pair<int,int> ii;
typedef long long LL;
int main(){

    int test;
    cin >> test;
    REP(t, 0, test){
        string ans = "RICHARD";

        int X, R, C;
        cin >> X >> R >> C;
        if(R > C) swap(R, C);
        if(X == 1) ans = "GABRIEL";
        if(X == 2){
            if(R % 2  == 0 || C % 2 == 0) ans =  "GABRIEL";
        }
        if(X == 3){
            if(R == 2 and C == 3) ans = "GABRIEL";
            else if(R == 3 and C == 3) ans = "GABRIEL";
            else if(R == 3 and C == 4) ans = "GABRIEL";
        }

        else if(X == 4){
            if(R == 3 and C == 4) ans = "GABRIEL";
            if(R == 4 and C == 4) ans = "GABRIEL";

        }

        cout << "Case #" << t + 1 << ": "  << ans << endl;
    }

    return 0;
}
