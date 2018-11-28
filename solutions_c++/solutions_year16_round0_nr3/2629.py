#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<long long> primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149};

long long getDivisor(long long n) {
    for (unsigned i = 0; i < primes.size(); i++) {
        if (n % primes[i] == 0 && n != primes[i]) {
            return primes[i];
        }
    }
    return 0;
}

vector<int> getBase2(long long n) {
    vector<int> res;
    while (n > 0) {
        res.push_back(n%2);
        n /= 2;   
    }
    reverse(begin(res), end(res));
    return res;
}

long long withBase(vector<int> &base2, int base) {
    long long mul = 1;
    long long res = 0;
    for (int i = base2.size()-1; i >= 0; i--) {
        res += base2[i] * mul;
        //cout << res << " ";
        mul *= base;
    }
    return res;
}

void calc(int N, int J) {
    vector<long long> divisors(15);
    vector<long long> numbers(15);
    int j = 0;
    
    long long num = 1 << (N-1);
    num++;
    while (j < J) {
        vector<int> base2 = getBase2(num);
        
        bool failed = false;
        for (int base = 2; base <= 10 && !failed; base++) {
            long long curNum = withBase(base2, base);
            long long div = getDivisor(curNum);
            if (div < 2) failed = true;
            divisors[base] = div;
            numbers[base] = curNum;
        }
        
        if (!failed) {
            j++;
            //print number base 2
            for (int i = 0; i < base2.size(); i++) {
                cout << base2[i];   
            }
            for (int i = 2; i <= 10; i++) {
//                cout << "   " << numbers[i];
                cout << " " << divisors[i];
            }
            cout << endl;
        }

        num += 2;
    }
    
}

int main() {
    vector<int> t = {1,0,0,0,1,1};
    //cout << withBase(t, 2) << endl;
	int testCases;
    cin >> testCases;
    int N, J;

    for (int i = 1; i <= testCases; i++) {
        cin >> N >> J;
        cout << "Case #" << i << ":" << endl;
        calc(N, J);
    }

    return 0;
}
