#include <bits/stdc++.h>
using namespace std;
#define AA first
#define BB second
#define PB push_back
#define MP make_pair
int main()
{
    int T, __case = 0, d, x, r , c;
    freopen("out4.txt", "w", stdout);
    scanf("%d", &T);
    while(T--) {
        cin >> x >> r >> c;
        int ans = 0;
        if(x == 1)
            ans = 1;
        else if(x == 2) {
            if((r % 2 == 0) || (c % 2 == 0))
                ans = 1;
            else
                ans = 0;
        } else if(x == 3) {
            if(r < c) swap(r,c);
            if(r == 3 && c == 2)
                ans = 1;
            else if(r == 4 and c == 3)
                ans = 1;
            else if(r == 3 && c == 3)
                ans = 1;
            else
                ans = 0;
        } else if(x == 4){
            if(r < c) swap(r,c);
            if(r == 4 && c >= 3)
                ans = 1;
            else
                ans = 0;
        }
        printf("Case #%d: %s\n", ++__case, ans ? "GABRIEL" : "RICHARD");
    }
    return 0;
}
