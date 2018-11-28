#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> getset() {
    vector<int> x(4);
    scanf("%d %d %d %d", &x[0], &x[1], &x[2], &x[3]);
    sort(x.begin(), x.end());
    return x;
}

void ignore() {
    scanf("%*d %*d %*d %*d");
}

void solve() {
    int ra, rb;
    vector<int> A, B;
    scanf("%d", &ra);
    for(int i = 1; i <= 4; i ++)
        if(i == ra)
            A = getset();
        else
            ignore();

    scanf("%d", &rb);
    for(int i = 1; i <= 4; i ++)
        if(i == rb)
            B = getset();
        else
            ignore();
    vector<int> v(4);
    vector<int>::iterator it;
    it = set_intersection(A.begin(), A.end(), B.begin(), B.end(), v.begin());
    v.resize(it - v.begin());
    switch(v.size()) {
        case 0:
            printf("Volunteer cheated!\n");
            return;
        case 1:
            printf("%d\n", v[0]);
            return;
        default:
            printf("Bad magician!\n");
            return;
    }
}

int main() {
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i ++) {
        printf("Case #%d: ", i);
        solve();
    }
}