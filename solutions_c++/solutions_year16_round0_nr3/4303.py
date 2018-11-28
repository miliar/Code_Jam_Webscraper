/*
* @Author: ahteeGang
* @Date:   2016-04-10 00:43:56
* @Last Modified by:   ahteeGang
* @Last Modified time: 2016-04-10 00:44:09
*/

#include <iostream>
#include <cmath>
#include <stdint.h>

using namespace std;

uint64_t findBase(int base, uint64_t num)
{
    int power = 0;
    uint64_t result = 0;
    while (num != 0) {
        result += (num % 10) * (uint64_t)pow(base, power);
        num /= 10;
        power++;
    }
    return result;
}

bool is_prime(uint64_t num, int i, uint64_t base_result[])
{
    for (int j = 2; j < sqrt(num); j++) {
        if (num % j == 0) {
            base_result[i] = j;
            return false;
        }
    }
    return true;
}

bool checkCoinjam(uint64_t coin, uint64_t base_result[])
{
    for (int i = 2; i <= 10; i++) {
        if (is_prime(base_result[i - 2] = findBase(i, coin), i - 2, base_result))
            return false;
    }
    return true;
}

uint64_t addCoin(uint64_t coin)
{
    bool added = false;
    uint64_t i = 0;
    while (!added) {
        if (coin % 10 == 1) {
            i++;
            coin /= 10;
        } else {
            coin += 1;
            for (uint64_t j = 0; j < i; j++) {
                coin = (coin * 10);
            }
            added = true;
        }
    }
    if (coin % 10 == 0)
        coin++;
    return coin;
}

void genCoinjam(int n, int j)
{
    cout << endl;
    uint64_t base_result[9];
    uint64_t coin = 1;
    for (int i = 0; i < n-1; ++i) {
        coin *= 10;
    }
    coin += 1;
    uint64_t max = (coin - 1) * 10;
    for (int i = 0; i < j; i++) {
        if (checkCoinjam(coin, base_result)) {
            cout << coin << ' ';
            for (int k = 0; k < 9; k++) {
                cout << base_result[k] << ' ';
            }
            cout << endl;
        } else
            i--;
        coin = addCoin(coin);
        if (coin > max)
            break;
    }
}

int main()
{
    int loop;
    cin >> loop;
    int n, j;
    for (int i = 0; i < loop; ++i) {
        cin >> n >> j;
        cout << "case #" << i + 1 << ":";
        genCoinjam(n, j);
    }
    return 0;
}