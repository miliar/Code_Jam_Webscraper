#include <cstdio>
#include <algorithm>

using namespace std;

#define MAX_MAGIC_NUMBER 17

int num[MAX_MAGIC_NUMBER];

void up() {
    int x, row;
    scanf("%i", &row);
    for(int r=1; r<=4; ++r) 
        for(int c=1; c<=4; ++c) {
            scanf("%i", &x);
            if (r==row) num[x]++;
        }    
}

int main() {
    int tt;
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);

    scanf("%i", &tt);
    for(int t=1; t<=tt; ++t) {
        printf("Case #%i: ", t);
        fill(num, num + MAX_MAGIC_NUMBER, 0);
        up();
        up();
        int c = count(num, num + MAX_MAGIC_NUMBER, 2);
        if (c==0) printf("Volunteer cheated!\n");
        else if (c>1) printf("Bad magician!\n");
        else printf("%i\n", find(num, num + MAX_MAGIC_NUMBER, 2) - num);            
    }
}