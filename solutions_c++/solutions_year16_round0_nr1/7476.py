#include<iostream>
#include<stdio.h>
#include<string.h>
#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<vector>
#include<cstdio>
#include<cmath>
#include<queue>
#include<stack>

using namespace std;

int main() {
    int t;
    scanf("%d",&t);
    long long n;
    int caseNumber = 1;
    while (t--) {
        long long multiplier = 1;
        long long answer;
        int check[20];
        for (int i = 0; i < 10; i++) {
            check[i] = 0;
        }
        int flag = 0;
        scanf("%lld",&n);
        if (n == 0) {
            flag = 1;
        } else {
            int checkSum = 0;
            while (checkSum != 10) {
                long long tempN = n*multiplier;
                long long storeResult = tempN;
                multiplier++;
                while (tempN != 0) {
                    check[tempN%10] = 1;
                    tempN /= 10;
                }
                for (int i = 0; i < 10; i++) {
                    checkSum += check[i];
                }
                if (checkSum == 10) {
                    answer = storeResult;
                } else {
                    checkSum = 0;
                }
            }
        }
        
        if (flag) {
            printf("Case #%d: INSOMNIA\n",caseNumber);
        } else {
            printf("Case #%d: %lld\n",caseNumber, answer);
        }
        caseNumber++;
    }
    return 0;
}