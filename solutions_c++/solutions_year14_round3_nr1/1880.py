#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>

using namespace std;

int testNum;
long long P, Q;

void convertToNum(char str[], long long &P, long long &Q){
    char * pch;

    pch = strtok (str,"/");
    P = (long long)atof(pch);

    pch = strtok (NULL, "/");
    Q = (long long)atof(pch);

}

int calc(long long P, long long Q){
    int cnt = 1;
    while (Q % 2 ==0){
        if (Q > P * 2) cnt++;
        Q = Q / 2;
    }
    if (Q > 1) return 0;
    return cnt;
}

int GCD(long long x, long long y){
    long long r;
    while (y != 0){
        r = x % y;
        x = y;
        y = r;
    }

    return x;
}
int main(){
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int testCase = 0, res;
    cin >> testNum;
    char s[100];
    gets(s);
    while (testCase < testNum){
        testCase++;
        gets(s);
        convertToNum(s, P, Q);
        long long X = GCD(P, Q);
        P /= X; Q /= X;

        res = calc(P, Q);

        switch (res){
            case 0:
                cout << "Case #" << testCase << ": impossible" << endl;
                break;
            default:
                cout << "Case #" << testCase << ": " << res << endl;
                break;
        }
    }
    return 0;
}
