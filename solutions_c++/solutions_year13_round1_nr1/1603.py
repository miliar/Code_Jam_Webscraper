#include <cstdio>
using namespace std;

int t[100][100];

int counter = 0;
void make() {
    printf("Case #%d: ", ++counter);

    int r, t; scanf("%d %d", &r, &t);

    int n = 0;
    while(1)
    {
        t-=2*r+1+4*n;
        if (t<0)
        {
            break;
        }
        n++;
    }

    printf("%d\n",n);
    return;
}

int main() {
    int t; scanf("%d", &t);
    while(t--) {
        make();
    }
    return 0;
}
