#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

int n;

int solve(vector<int> x) {
    int i, j, k, ret = 1, m = x[x.size()-1];

    /*puts("CALLED FOR");
    for(i=0;i<x.size();i++) {
        printf("%d  ", x[i]);
    }
    puts("==========");
    getchar();*/

    int last = x[x.size()-1];
    if(last < 4) {
//        puts("RETURN");
        return last;
    }

    for(k = 2; k <= last/2; k++) {
        vector<int> tmp;
        for(i = 0; i < x.size() - 1; i++) {
            tmp.push_back(x[i]);
        }

        tmp.push_back(k);
        tmp.push_back(last - k);
        sort(tmp.begin(), tmp.end());
        m = min(m, 1 + solve(tmp));
    }
    return m;
}

int main() {
    int cases, i, j, t=1;
    scanf("%d", &cases);
    while(cases--) {
        vector<int> V;
        scanf("%d", &n);
        for(i=0;i<n;i++) {
            scanf("%d", &j);
            V.push_back(j);
        }
        sort(V.begin(), V.end());
        printf("Case #%d: %d\n",t++, solve(V));
    }
}
