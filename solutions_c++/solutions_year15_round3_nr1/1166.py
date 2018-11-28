# include <cstdio>
# include <iostream>
using namespace std;

int main(){
    //freopen ("A-large.in", "r", stdin);
    //freopen ("Alout.txt", "w", stdout);
    int cases, caseno=0, c, r, w, sum;
    scanf ("%d", &cases);
    while (cases--){
        scanf ("%d %d %d", &r, &c, &w);
        sum = c/w;
        sum *= r;
        sum += (w-1);
        if (c%w) sum++;
        printf("Case #%d: %d\n", ++caseno, sum);
    }
    return 0;
}
