#include <cstdio>
#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

vector <long long> v;

bool checkPalin(long long number) {
    long long temp = number;
    long long reversed = 0LL;
    while (temp) {
        //cout << reversed "   " << temp
        reversed *= 10LL;
        reversed += temp % (10LL);
        temp /= 10LL;
    }
    if (reversed == number)
        return true;
    else
        return false;
}

int main() {
    v.clear();
    for (long long i=1;i<=10000000;++i) {
        if (checkPalin(i) == true) {
            //cout << i << endl;
            long long k = i*i;
            if (checkPalin(k) == true) {
                v.push_back(k);
                //cout << k << " ";
            }
        }
    }
    //cout << v[v.size() - 1];
    /*for (int i=1;i<122;++i)
        cout << tab[i] << endl;*/
    int T;
    scanf("%d",&T);
    for (int caseNumber = 1;caseNumber<=T;++caseNumber) {
        long long A,B;
        int result;
        scanf("%lld %lld",&A,&B);
        int upB;
        int lowA;
        if (A > v[v.size()-1]) {
                //cout << "aa";
            result = 0;
            printf("Case #%d: %d\n",caseNumber,result);
            continue;
        }
        else if (A == v[v.size()-1]) {
            result = 1;
            printf("Case #%d: %d\n",caseNumber,result);
            continue;
        }

        for (int i=0;i<v.size();++i) {
            if (A <= v[i]) {
                lowA = i;
                break;
            }
        }
        if (B >= v[v.size()-1])
            upB = v.size()-1;
        else
            for (int i=0;i<v.size();++i) {
                if (B < v[i]) {
                    upB = i-1;
                    break;
                }
            }
        result = upB - lowA + 1;
        printf("Case #%d: %d\n",caseNumber,result);
    }
    return 0;
}
