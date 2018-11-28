#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#define ll long long

using namespace std;

int ar[100];
ll number, n, j;
ll result[100];

bool check(){
    for (int i = 2; i < 11; ++i){
        result[i] = 0;
        number = 0;
        for (int j = 0; j < n; ++j){
            number *= i;
            number += ar[j];
        }
        //cout << i << " " << number << endl;;
        ll k = sqrt(number) + 1;
        for (int j = 2; j < k && result[i] == 0; ++j){
            if (number % j == 0){
                result[i] = j;
            }
        }
        if (result[i] == 0){
            return false;
        }
    }
    for (int i = 0; i < n; ++i){
        cout << ar[i];
    }
    for (int i = 2; i < 11; ++i){
        cout << " " << result[i];
    }
    cout << endl;
}

int main(){

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> n;
    cin >> n >> j;
    cout << "Case #1:" << endl;

    ar[0] = 1;
    ar[n - 1] = 1;

    int count = 0;

    while (j){
        if (check()) j--;
        ar[n - 2] ++;
        for (int i = n - 2; i > 0; --i){
            ar[i - 1] += ar[i] / 2;
            ar[i] = ar[i] % 2;
        }
    }

}
