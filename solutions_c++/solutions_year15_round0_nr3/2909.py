#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

void print_answer(int id, bool can) {
    cout << "Case #" << id << ": " << (can ? "YES" : "NO") << endl;
}

inline char ichar(const string &s, int idx) {
    return s[idx % s.size()];
}

vector<vector<int>> lookup {
    {0, 0, 0, 0, 0},
    {0, 1, 2, 3, 4},
    {0, 2,-1, 4,-3},
    {0, 3,-4,-1, 2},
    {0, 4, 3,-2,-1},
};

inline int mult(int x, int y) {
    return lookup[x][y];
}

int sgn(int val) {
    return (0 < val) - (val < 0);
}

int check_rest(const string& input, int ssize, int max_repeats) {
    int target = 2;
    int curr_result = 1;
    for (int rep_idx = 0; rep_idx < max_repeats; ++rep_idx) {
        for (int str_idx = 0; str_idx < ssize; ++ str_idx) {
            int curr = ichar(input, rep_idx * ssize + str_idx) - 'i' + 2;
            curr_result = mult(abs(curr_result), curr) * sgn(curr_result);
        }
        if (curr_result == 1)
            return rep_idx + 1;
    }
    return -1;
}

void process_test(int id) {
    int result = false;
    int ssize, repeats;
    cin >> ssize >> repeats;
    string input;
    cin >> input;

    int target = 2;
    int curr_result = 1;
    int idx = 0;
    for (idx = 0; idx < ssize * repeats; ++idx) {
        int curr = ichar(input, idx) - 'i' + 2;
        curr_result = mult(abs(curr_result), curr) * sgn(curr_result);
        if (curr_result == target) {
            ++target;
            curr_result = 1;
        }
        if (target == 5 && curr_result == 1 && (idx + 1) % ssize == 0) {
            ++idx;
            break;
        }
    }

    int rest_repeats = repeats - idx / ssize;
    int good_tail = true;
    if (rest_repeats > 0) {
        good_tail = false;
        int rep_time = check_rest(input, ssize, rest_repeats);
        if (rep_time > 0 && rest_repeats % rep_time == 0)
            good_tail = true;
    }

    result = (target == 5 && curr_result == 1 && good_tail);

    print_answer(id, result);

}

int main() {
    int test_count;
    cin >> test_count;
    for (int i = 0; i < test_count; ++i) {
        process_test(i + 1);
    }
    return 0;
}