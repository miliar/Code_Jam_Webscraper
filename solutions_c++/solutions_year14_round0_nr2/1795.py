#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

int T;
double C , F , X , ret , S;

int main () {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> T;
    for (int i = 1;i <= T;i ++) {
        cin >> C >> F >> X;
        S = 2;
        ret = 0;
        while (X / S > C / S + X / (S + F)) {
              ret += C / S;
              S = S + F;
        }
        ret += X / S;
        cout << "Case #" << i << ": ";
        printf("%.7f\n",ret);
    }
    return 0;
}
