#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;

const int N = 1010;

double Naomi[1010];
double Ken[1010];

int worst(int n){
    int ret = 0;

    int pos = n-1;
    for (int i = n-1; i >= 0; --i){
        if (Ken[pos] > Naomi[i]) --pos;
        else ++ret;
    }

    return ret;
}

int best(int n){
    int ret = 0;

    int pos = 0;
    for (int i = 0; i < n; ++i){
        if (Ken[pos] < Naomi[i]){
            ++ret;
            ++pos;
        }
    }
    return ret;
}

int main()
{
//    freopen("in.txt", "r", stdin);
//    freopen("B-large.in", "r", stdin);
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t, cas = 0;
    scanf("%d", &t);

    int n;

    while (t--){

        scanf("%d", &n);

        for (int i = 0; i < n; ++i) scanf(" %lf", &Naomi[i]);
        for (int i = 0; i < n; ++i) scanf(" %lf", &Ken[i]);

        sort(Naomi, Naomi+n);
        sort(Ken, Ken+n);

        printf("Case #%d: %d %d\n", ++cas, best(n), worst(n));
    }

    return 0;
}
