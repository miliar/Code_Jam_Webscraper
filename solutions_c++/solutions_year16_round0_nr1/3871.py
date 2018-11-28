#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>

using namespace std;

string getCountingSheep(long long num) {
    // cout << "num: " << num << endl;
    int cnt = 0;
    const int target = (1<<10) - 1;
    // cout << "target: " << target << endl;
    unordered_map<long long, int> num_cnt;
    int i = 1;
    int tmp = num;
    while (true) {
        tmp = num * i++;
        if (num_cnt.find(tmp) != num_cnt.end()) return "INSOMNIA";

        int last_num = tmp;
        while (tmp) {
            int d = tmp%10;
            tmp /= 10;
            cnt |= (1 << d);
            if (cnt == target) return to_string(last_num);
        }
        num_cnt[num]++;
    }
    return "INSOMNIA";
}

int main(int argc, char* argv[]) {
    ifstream in(argv[1]);
    ofstream out(argv[2]);
    // out.open();
    if (in.is_open()) {
        string line;
        int num_test_case;
        getline(in, line);
        num_test_case = stoi(line);
        cout << "num_test_case: " << num_test_case << endl;
        int num;
        int test_cast = 1;
        while (num_test_case-- && getline(in, line)) {
            num = stol(line);
            out << "Case #" << test_cast++ << ": " << getCountingSheep(num) << endl;
        }
        in.close();
        out.close();
    }
}
