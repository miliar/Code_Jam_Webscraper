#include <iostream>
#include <cstdio>
using namespace std;
int a[10][10],b[10][10],c[10],d[10],p,q;
int main(){
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T;
    cin >> T;
    for (int o = 1; o <= T; o++){
        cin >> p;
        for (int i = 1; i <= 4; i++)
        for (int j = 1; j <= 4; j++)
            cin >> a[i][j];
        cin >> q;
        for (int i = 1; i <= 4; i++)
        for (int j = 1; j <= 4; j++)
            cin >> b[i][j];
        for (int i = 1; i <= 4; i++)
            {c[i] = a[p][i]; d[i] = b[q][i];}
        int sum = 0, H;
        for (int i = 1; i <= 4; i++)
        for (int j = 1; j <= 4; j++)
            if (c[i] == d[j]) {sum++; H=c[i];}
        printf("Case #%d: ", o);
        if (sum == 1) printf("%d\n",H);
        else if (sum > 1) printf("Bad magician!\n");
        else printf("Volunteer cheated!\n");
    }
}
