#include <bits/stdc++.h>
using namespace std;
#define REP(a, b, c) for(int a = b; a < c; a++)
#define asd(x)              cout<<__LINE__<<" :: "<<#x<< ": "<<x<<endl;
#define asdf(x, y)          cout<<__LINE__<<" :: "<<#x<< ": "<<x<<" | "<<#y<< ": "<<y<<endl;
typedef pair<int,int> ii;
typedef long long LL;
int main(){

    int n;
    cin >> n;
    REP(t, 0, n){
        int x;
        string str;
        cin >> x >> str;

        int total = 0, ans = 0;
        REP(i, 0, x+1){
            if(str[i] == '0') continue;
            
            int here = max(0, i - total);
            total += (str[i] - '0') + here;
            ans += here;
        }

        printf("Case #%d: %d\n", t + 1, ans);

    }

    return 0;
}
