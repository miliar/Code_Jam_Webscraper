#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

void print_answer(int id, int x) {
    cout << "Case #" << id << ": " << x << endl;
}

void process_test(int id) {
    int max_shy_value;
    string shy_data;
    cin >> max_shy_value;
    cin >> shy_data;
    int need_friends = 0;
    long long sum = 0;
    for (int i = 0; i < shy_data.size(); ++i) {
        sum += shy_data[i] - '0';
        int curr_diff = (i + 1) - sum;
        need_friends = max(need_friends, curr_diff);
    }
    print_answer(id, need_friends);

}

int main() {
    int test_count;
    cin >> test_count;
    for (int i = 0; i < test_count; ++i) {
        process_test(i + 1);
    }
    return 0;
}