#include<cstdio>
#include<vector>
#include<cmath>
using namespace std;


bool chpal(long long a) {
    vector<int> t;
    while (a) {
        t.push_back(a%10);
        a/=10;
    }
    int b = 0;
    int e = t.size() -1;
    while(b<e) {
        if (t[b] != t[e]) return false;
        b++;
        e--;
    }
    return true;
}

bool checkok(long long i) {
    return chpal(i) && chpal(i*i);
}

int ans[10000001];

int main() {
    ans[0] = 0;
    for (int i=1; i<=10000000; i++) {
        ans[i] = ans[i-1] + (checkok(i) ? 1 : 0);
    }
    int z; scanf("%d", &z);
    int all = z;
    while(z--) {
        int a, b;
        scanf("%d%d", &a, &b);
        int first = floor(sqrt(a-1));
        int last = floor(sqrt(b));
        printf("Case #%d: %d\n", all-z, ans[last]-ans[first]);
    }
}





