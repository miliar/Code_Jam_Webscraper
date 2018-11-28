#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

typedef long long ll;

int main()
{
    freopen("in.txt", "r", stdin);
    int t,s=0,x,r,c;
    scanf("%d", &t);
    while(t--){
        scanf("%d %d %d", &x, &r, &c);
        printf("Case #%d: ", ++s);
        if(x == 1) puts("GABRIEL");
        else if(x == 2){
            if(r%2 && c%2) puts("RICHARD");
            else puts("GABRIEL");
        }
        else if(x == 3){
            if(min(r,c) == 1) puts("RICHARD");
            else if(r == c && c == 2) puts("RICHARD");
            else if(r == 2 && c == 3 || r == 3 && c == 2) puts("GABRIEL");
            else if(r == c && c == 3) puts("GABRIEL");
            else if(r == 2 && c == 4 || r == 4 && c == 2) puts("RICHARD");
            else if(r == 3 && c == 4 || r == 4 && c == 3) puts("GABRIEL");
            else if(r == 4 && c == 4) puts("RICHARD"); ///not sure
        }
        else if(x == 4){
            if(max(r,c) < 4) puts("RICHARD");
            else{
                if(r<c) swap(r,c); ///c was 4, now r 4, c unknown
                if(c == 1) puts("RICHARD");
                else if(c == 2) puts("RICHARD");
                else if(c == 3) puts("GABRIEL");
                else if(c == 4) puts("GABRIEL");
            }
        }
    }
    return 0;
}
