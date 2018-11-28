#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

long long divisor(long long n){
    for(long long i=2; i*i<=n; i++)
        if(n % i == 0) return i;
    return -1;
}

bool divisible(int num) {
    vector<long long> rescale(11, 1);
    vector<long long> result(11, 0);
    int cur = num;
    while (cur) {
        for (int base = 2; base<=10; base++) {
            if ((cur&1)*rescale[base] > LLONG_MAX)
                return false;
            result[base] += (cur&1)*rescale[base];
            rescale[base] *= base;
        }
        cur = cur >> 1;
    }
    vector <long long> divisors;
    for (int base = 2; base <= 10; base++) {
        long long div = divisor(result[base]);
        if (div == -1)
            break;
        else
            divisors.push_back(div);
    }

    if (divisors.size() == 9) {
        cout << result[10] << " ";
        for (auto &div:divisors) cout << div << " ";
        cout << endl;
        return true;
    } else
        return false;
}

void coinJam(int N, int J) {
    int lb = pow(2, N-1) + 1;
    int ub = pow(2, N);
    int count = 0;
    for (int i = lb; i < ub && count < J; i += 2) {
        if (divisible(i))
            count++;
    }
}

int main(){
    int T, id = 1;
    cin >> T;
    int N, J;
    while (T--) {
        cout << "Case #" << id << ":" << endl;
        id++;
        cin >> N >> J;
        coinJam(N, J);
    }
    return 0;
}