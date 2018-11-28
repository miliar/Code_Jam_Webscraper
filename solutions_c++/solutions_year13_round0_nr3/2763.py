#include <iostream>
#include <cmath>
#include <cstdio>

using namespace std;

int solve(int A, int B);

int main(void)
{
    int T;
    int A, B;
    cin >> T;
    for(int round=1;round<=T;round++) {
        cin >> A >> B;
        printf("Case #%d: %d\n", round, solve(A, B));
    }
    return 0;
}

bool is_palindromes(int num)
{
    int num2 = num, num3 = 0;
    while(num2) {
        num3 *= 10;
        num3 += num2 % 10;
        num2 /= 10;
    }
    return num == num3;
}

int solve(int A, int B)
{
    int count = 0;
    int q = sqrt(A) - 1;
    for(;q*q <= B;q++) {
        if(q*q < A) continue;
        if(!is_palindromes(q)) continue;
        if(!is_palindromes(q*q)) continue;
        count++;
    }
    return count;
}

