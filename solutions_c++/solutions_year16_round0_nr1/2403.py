#define _CRT_SECURE_NO_WARNINGS

#pragma comment(linker, "/STACK:16777216")
#include <cmath>
#include <math.h>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <iostream>
#include <queue>
#include <string>
#include <sstream>
#include <time.h>
#include <iomanip>
#include <cstdio>

using namespace std;


int  main()
{
    ios_base::sync_with_stdio(false); cin.tie(0);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    long long tests;
    cin >> tests;
    for (long long test = 0; test < tests; test++) {
        long long n;
        cin >> n;
        if (n == 0) {
            cout << "Case #" << test + 1 << ": " << "INSOMNIA" << endl;
            continue;
        }
        long long k[10];
        for (long long i = 0; i < 10; i++)
            k[i] = 0;
        long long p = 1;
        while (true) {
            long long x = n * p;
            while (x != 0) {
                k[x % 10]++;
                x /= 10;
            }
            bool ans = true;
            for (long long i = 0; i < 10; i++)
                if (k[i] == 0) ans = false;
            if (ans) {
                cout << "Case #" << test + 1 << ": " << p*n << endl;
                break;
            }
            p++;
        }
        
    }
}