#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

bool isPrime(long long num) {
    if (num <= 3) {
        return num > 1;
    } else if (num % 2 == 0 || num % 3 == 0) {
        return false;
    } else {
        for (long long i = 5; i * i <= num; i += 6) {
            if (num % i == 0 || num % (i + 2) == 0) {
                return false;
            }
        }
        return true;
    }
}

long long genNumber(int base, int num, int n) {
    long long ret = 0;
    for (size_t i = 0; i < n; ++i) {
        ret = ret * base + ((num >> (n-i-1)) & 1);
    }

    return ret;
}

string genStr(int num, int n) {
    string res;
    for (size_t i = 0; i < n; ++i) {
        if((num >> (n-i-1)) & 1) {
            res += "1";
        } else {
            res += "0";
        }
    }

    return res;
}

long long get_divisor(long long num) {
    for (long long i = 2; i < num / 2; ++i) {
        if (num % i == 0) return i;
    }
    return -1;
}

void genCoin(int n, int j, ofstream& out) {
    cout << "n: " << n << ", j: " << j << endl;

    out << "Case #1:" << endl;
    int start = (1 << (n-1)) + 1;
    int end = (1 << n) - 1;
    for (int i = start; i <= end; ++i) {
        vector<long long> divisor(9);
        if (!(i&1)) continue;
        long long num = 0;
        int b = 2;
        for (b = 2; b <=10; ++b) {
            num = genNumber(b, i, n);
            if (isPrime(num)) {
                break;
            }
            auto r = get_divisor(num);
            if (r== -1) break;
            divisor[b-2] = r;
        }
        if (b == 11) {
            j--;
            auto str = genStr(i, n);
            out << str + " ";
            for (auto dd : divisor) out << " " << dd;
            out << "\n";
            if (j==0) break;
        }
    }

}

int main(int argc, char* argv[]) {
    ifstream in(argv[1]);
    ofstream out(argv[2]);
    if (in.is_open()) {
        string line;
        int num_test_case;
        getline(in, line);
        num_test_case = stoi(line);
        cout << "num_test_case: " << num_test_case << endl;
        while (num_test_case-- && getline(in, line)) {
            istringstream is(line);
            int n = 0, j = 0;
            is >> n >> j;
            genCoin(n, j, out);
        }
        in.close();
        out.close();
    }

    for (int b = 2; b <= 10; ++b) {
        auto num = genNumber(b, 6, 3);
        cout << num << endl;
        // auto str = genStr(9, 4);
        // cout << str << endl;
    }
    cout << genStr(6, 3);

    // cout << genNumber(3, 55, 6) << endl;
}
