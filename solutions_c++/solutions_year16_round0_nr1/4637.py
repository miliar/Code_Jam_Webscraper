#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>

using namespace std;
void insertDigits(int digits[], int number);
bool containsAll(int digits[]);
int main(){
    FILE *fin = freopen("A-large.in", "r", stdin);
    assert(fin!=NULL);
    FILE *fout = freopen("A-large.out", "w", stdout);
    int testCases;
    cin >> testCases;
    //digits[0] = -1;
    for (int x = 0; x < testCases; x++){
        int digits[10] = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1};
        int number;
        cin >> number;
        bool check = 0;
        for (int i = 1; i < 1000000; i++){
            insertDigits(digits, i*number);
            check = containsAll(digits);
            if (check == 1){
                number = i* number;
                break;
            }
        }
        if (check)
            cout << "Case #" << x+1 << ": " << number << endl;
        else
            cout << "Case #" << x+1 << ": " << "INSOMNIA" << endl;
    }

    return 0;
}
void insertDigits(int digits[], int number){
    while (number > 0){
        int digit = number % 10;
        digits[digit] = digit;
        number = number/10;
    }
}
bool containsAll(int digits[]){
    for (int i = 0; i < 10; i++){
        if (digits[i] != i){
            return 0;
        }
    }
    return 1;
}
