#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>

int arr[10];
int rest;
long long curNum;

using namespace std;

int main ()
{
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    int t;
    cin >> t;
    for(long long i = 0;i < t;i++){
        for (int j = 0;j < 10;j++){
            arr[j] = 0;
        }
        rest = 10;

        long long n;
        cin >> n;
        if (n == 0){
            printf ("Case #%d: INSOMNIA\n", i + 1);
            continue;
        }
        int k = 1;
        while (rest > 0){
            curNum = n * k;
            while (curNum > 0){
                arr[curNum % 10]++;
                if (arr[curNum % 10] == 1){
                    rest--;
                }
                curNum /= 10;
            }
            k++;
        }
        printf ("Case #%d: %lld\n", i + 1, n * (k - 1));
    }
    return 0;
}