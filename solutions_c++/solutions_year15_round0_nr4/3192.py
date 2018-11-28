#include <bits/stdc++.h>
#define LL long long
#define x first
#define y second
#define pb push_back
#define mod 1000000007
using namespace std;

int main()
{
    freopen("D-small-attempt1.in", "r", stdin);
    freopen("op.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    int x, r, c;
    int tc = 1;
    while(t--){
        string str = "";
        scanf("%d%d%d", &x, &r, &c);
        if(x==1){
            str = "GABRIEL";
        }
        else if(x==2){
            if((r*c)%2 != 0){
                str = "RICHARD";
            }
            else {
                str = "GABRIEL";
            }
        }
        else if(x==3){
            if((r!=1 && c!=1) && (r==3 || c==3)){
                str = "GABRIEL";
            }
            else {
                str = "RICHARD";
            }
        }
        else if(x==4){
            if(r>c){
                int tmp = r;
                r = c;
                c = tmp;
            }
            if(c==4 &&(r==3||r==4)){
                str = "GABRIEL";
            }
            else {
                str = "RICHARD";
            }
        }
        cout << "Case #" << tc << ": " << str <<endl;
        tc++;
    }
    return 0;
}
