#include <iostream>
#include <vector>
#include <string>
#include <numeric>
#include <cmath>

using namespace std;

struct Item {
    string value;
    // vector<long> bases;
    vector<int> divisors;
};

long interpret_base(const string& input, long base) {
    long answer = 0;
    long pow = 1;
    for (int i = input.size()-1; i >= 0; --i) {
        answer += (input[i] == '1') * pow;
        pow *= base;
    }

    return answer;
}

long get_divisor(long input) {
    if (input % 2 == 0) return 2;

    for (long i = 3; i <= sqrt(input); i += 2) {
        if (input % i == 0) {
            return i;
        }
    }
    return -1;
}

void examine(vector<Item>& answer, string& current) {
    current.push_back('1');
    
    Item add;
    add.value = current;
    
    for (long i = 2; i <= 10; ++i) {
        long base_i = interpret_base(current, i);
        long divisor = get_divisor(base_i);
        if (divisor == -1) {
            break;
        }
        // add.bases.push_back(base_i);
        add.divisors.push_back(divisor);
    }

    if (add.divisors.size() == 9) {
        answer.push_back(add);
    }

    current.pop_back();
}

void solveHelper(vector<Item>& answers, 
                string& current,
                int start_idx,
                int end_idx,
                int count) {
    if (start_idx == end_idx) {
        examine(answers, current);
        return;
    }

    for (char c = '0'; c <= '1' && answers.size() < count; ++c) {
        current.push_back(c);
        solveHelper(answers, current, start_idx+1, end_idx, count);
        current.pop_back();
    }
}

int solve(int n, int j) {
    vector<Item> answers;
    string current = "1";
    solveHelper(answers, current, 1, n-1, j);

    for (auto& item: answers) {
        cout << item.value;
        for (long d : item.divisors) {
            cout << " " << d;
        }
        cout << endl;
    }

    return 0;
}

int main() {
    int T;
    int n, j;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> n >> j;
        cout << "Case #" << i << ": " << endl;
        solve(n, j);
    }
    return 0;
}
