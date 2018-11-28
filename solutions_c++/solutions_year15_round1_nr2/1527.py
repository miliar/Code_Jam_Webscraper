# include <cstdio>
# include <iostream>
# include <cmath>
# include <cstring>
# include <algorithm>
using namespace std;

struct barber{
    int id;
    int time;
    bool operator < (const barber &b) const{
        if (time<b.time) return true;
        if (time>b.time) return false;
        return id<b.id;
    }
};

barber B [4500000];

int GCD (int a, int b){
    return (b)?GCD(b,a%b):a;
}

int LCM (int a, int b){
    return (a*b)/GCD(a,b);
}

int main(){
    //freopen ("B-small-attempt0.in", "r", stdin);
    //freopen ("Bout.txt", "w", stdout);
    int cases, caseno=0, b, n, lcm, i, j, mul, total;
    scanf ("%d", &cases);
    while (cases--){
        scanf("%d %d", &b, &n);
        lcm = mul = 1;
        total = 0;

        for (i=0; i<b; i++){
            B[i].id = i+1;
            B[i].time = 0;
        }

        j = 1;
        for (i=b; i<2*b; i++){
            B[i].id = j++;
            scanf ("%d", &B[i].time);
            lcm = LCM(lcm, B[i].time);
        }

        for (j=b ; j<2*b; j++){
            total += lcm/B[j].time;
        }

        for (j=b; j<2*b; j++){
            mul = 2;
            for ( ;B[j].time*mul<lcm ; i++){
                B[i] = B[j];
                B[i].time*=mul;
                mul++;
            }
        }
        sort (B, B+i);
        printf ("Case #%d: %d\n", ++caseno, B[(n-1)%total]);
    }
    return 0;
}
