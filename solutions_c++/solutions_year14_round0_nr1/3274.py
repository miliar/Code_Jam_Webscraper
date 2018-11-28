#include <cstdio>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <cstring>
#include <cctype>
#include <queue>

using namespace std;

typedef long long          ll;
typedef pair <int, int>    ii;
typedef vector <ii>       vii;
typedef vector <int>       vi;
#define INF 1000000000
#define pb push_back
#define mp make_pair

int grid[4][4];
int otherGrid[4][4];

int main() {
    freopen ("inputA.txt","r",stdin);
    freopen ("outputA.txt","w",stdout);
    int k;
    scanf(" %d", &k);
    for (int a = 1; a <=k;a++) {
        int n;
        scanf(" %d", &n);
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                scanf(" %d", &grid[i][j]);
            }
        }
        int m;
        scanf(" %d", &m);
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                scanf(" %d", &otherGrid[i][j]);
            }
        }
        int ans;
        int cont = 0;
        for (int i = 0; i < 4; i++) {
            int num = grid[n-1][i];
            for (int j = 0; j < 4; j++) {
                int num2 = otherGrid[m-1][j];
                if (num == num2) {
                    ans = num;
                    cont++;
                    break;
                }
            }
        }
        if (cont == 0) printf("Case #%d: Volunteer cheated!\n", a);
        else if (cont == 1) printf("Case #%d: %d\n",a,ans);
        else printf("Case #%d: Bad magician!\n",a);

    }
    return 0;
}
