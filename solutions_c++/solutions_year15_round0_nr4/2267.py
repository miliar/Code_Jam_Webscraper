# include <cstdio>
using namespace std;

int main(){
    //freopen("D-small-attempt1.in", "r", stdin);
    //freopen("Dout.txt", "r", stdout);
    int x, r, c, cases, caseno=0;
    scanf ("%d", &cases);
    while (cases--){
        scanf ("%d %d %d", &x, &r, &c);
        if (x==1) printf ("Case #%d: GABRIEL\n", ++caseno);
        else if (x==4 && (r==2)||(c==2)) printf ("Case #%d: RICHARD\n", ++caseno);  /// special case
        else if (c<x/2+x%2 || r<x/2+x%2 || r*c%x) printf("Case #%d: RICHARD\n", ++caseno);
        else printf("Case #%d: GABRIEL\n", ++caseno);
    }
    return 0;
}
