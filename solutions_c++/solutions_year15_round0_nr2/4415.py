#include <iostream>
#include <stdlib>
#include <stdio>
#include <map>
#include <algorithm>
#include <math.h>

typedef unsigned long long Int;

using namespace std;

//std::map <string, short int> cache;
std::map <unsigned long long, short int> cache;


int minimize(short int sz, short int *arr2) {
    short int max = -1;
    short int i, j;
    short int max_idx = -1;
    short int MIN = 32000;
    short int tmp = 0;

    unsigned long long hash = 0;

    unsigned short *arr = new unsigned short[sz];

    memcpy(arr, arr2, sz * sizeof(short int));

    std::sort(arr, arr + sz, std::greater<int>());

    // Find the maximum element
    for (int i=0; i<sz; i++) {
       // cout << ' ' << arr[i];
        hash = hash * 10 + arr[i];
        if (arr[i] > max) {
                max = arr[i];
                max_idx = i;
        }
    }

    if (cache.find(hash) != cache.end()) {
        //cout << "HASH " << hash << " -> " << cache[hash] << endl;
        //exit(0);
        return cache[hash];
    }

    // Remove trailing zeroes

    for (i=sz-1; i>0; i--) {
        if (arr[i] > 0)
            break;
    }
    sz = i + 1;


    //cout << endl;
    if (max <= 3)
        return max;

    // Scenario 1 (everyone eats)
    short int *sc1;
    sc1 = new short int[sz];
    for (i=0; i<sz; i++)
        if (arr[i] > 0)
            sc1[i] = arr[i] - 1; else
            sc1[i] = 0;
    MIN = minimize(sz, sc1);
    delete sc1;


    // Scenario 2 (max gets split)
    short int *sc2;
    sc2 = new short int[sz + 1];
    for (i=0; i<sz; i++) {
            sc2[i] = arr[i];
    }
    for (i=1; i<=ceil(arr[max_idx]/2.0); i++) {
        sc2[max_idx] = arr[max_idx] - i;
        sc2[sz] = i;
        tmp = minimize(sz + 1, sc2);
        if (tmp < MIN) MIN = tmp;
    }
    delete sc2;
    delete arr;

    cache[hash] = MIN + 1;

    return MIN + 1;
}



int solve() {
    int l;
    int cnt = 0;
    short int *arr;
    scanf("%d", &l);
    arr = new short int[l];
    //cout << "LEN: " << l << endl;
    for (int i=0; i<l; i++) {
        scanf("%hd", &arr[i]);
    }

    cnt = minimize(l, arr);

    delete arr;
    scanf("%c", &l);
    return cnt;
}

int main()
{
    //freopen("in.txt", "r", stdin);
    freopen("B-small-attempt4.in", "r", stdin);
   	freopen("a.out.bad4", "w", stdout);
    int cases = 123;
    scanf("%d", &cases);
    //cout << "CASES " << cases << endl;
    for (int c=0; c < cases; c++) {
         cout << "Case #" << (c + 1) << ": " << solve() << endl;
//         return 0;
    }

    return 0;
}

