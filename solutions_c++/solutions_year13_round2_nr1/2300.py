#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;


vector <long long> mote;
        int n;
long long get_num(long long AS, int k) {
    if (n == k)
        return 0;
    if (AS == 1)
        return get_num(AS, k + 1) + 1;
    long long boneat = 10000000, eat = 1000000, del = 10000000;;
    if (AS > mote[k])
        eat = get_num(AS + mote[k], k + 1);
    if (AS <= mote[k]) {
        del = get_num(AS, k + 1) + 1;
        boneat = get_num(2*AS - 1 , k) + 1;
    }
    return min(min(eat, del), boneat);
}

int main(void) {
    freopen("/Users/Alexandret/Downloads/a.in", "r", stdin);
    
//    freopen("/Users/Alexandret/Desktop/Programs/[Contests]/[Google Code Jam]/2013-1B/a.in", "r", stdin);
    freopen("/Users/Alexandret/Desktop/Programs/[Contests]/[Google Code Jam]/2013-1B/a.out", "w", stdout);
    
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        mote.clear();
        long long Asize;
        scanf("%lld%d", &Asize, &n);
        for (int j = 0; j < n; ++j) {
            int tmp;
            scanf("%d", &tmp);
            mote.push_back(tmp);
        }
        sort(mote.begin(), mote.end());
        printf("Case #%d: %lld\n", i + 1, get_num(Asize, 0));
    }
    return 0;
}