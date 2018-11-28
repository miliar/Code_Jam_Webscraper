#include <iostream>
#include <fstream>
#include <vector>
#include <utility>
#include <sstream>
#include <cmath>
#include <assert.h>
#include <unordered_map>
#include <unordered_set>
#include <climits>
#include <algorithm>

using namespace std;

typedef long long ll;

ll divisor(ll n) {
    ll square_root = sqrt(n);

    for (ll i = 2; i <= square_root; i++) {
        if (n % i == 0)
            return i;
    }
    return -1;
}

ll computeValue(string s, ll base) {
    ll ret = 0;
    for (ll i = s.size() - 1, j = 0; i >= 0; i--, j++) {
        ret += pow(base, j) * (s[i] - '0');
    }
    return ret;
}

void permutation(vector<string> &container, ll current_index, string current_string) {
    if (current_index == current_string.size() - 1) {
        container.push_back(current_string);
        return;
    }

    current_string[current_index] = '0';
    permutation(container, current_index + 1, current_string);
    current_string[current_index] = '1';
    permutation(container, current_index + 1, current_string);
}

int main() {
    //string file_path = "C:\\Users\\Aidan\\Desktop\\jam\\input.in";
    //ifstream data (file_path.c_str(), ios::in);
    ofstream ret ("C:\\Users\\Aidan\\Desktop\\jam\\output.out");

    vector<string> container;
    container.clear();

    string origin = "1000000000000001";
    permutation(container, 1, origin);

    ll catch_count = 0;
    ret << "Case #1:" << endl;
    for (ll i = 0; i < container.size(); i++) {
        string current_string = container[i];

        bool prime = false;
        // iterate through base 2 to 10
        vector<ll> divisors;
        divisors.clear();
        for (ll base = 2; base <= 10; base++) {
            ll value = computeValue(current_string, base);
            ll divisor_value = divisor(value);
            if (divisor_value != -1) {
                divisors.push_back(divisor_value);
            } else {
                // if there is a way to represent a prime, stop
                prime = true;
                break;
            }
        }
        if (!prime) {
            catch_count++;
            ret << current_string << " ";
            for (ll index = 0; index < divisors.size(); index++) {
                ret << divisors[index] << " ";
            }
            ret << endl;
        }

        if (catch_count == 50)
            return 0;
    }

    return 0;
}
