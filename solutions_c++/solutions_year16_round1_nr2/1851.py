#include <iostream>
#include <cstring>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;
void solveAndPrint(int caseNum);
int main(int argc, char *argv[]) {
    int numOfCase;
    cin >> numOfCase;
    for (int i = 0; i < numOfCase; i++) {
        solveAndPrint(i + 1);
    }
}

void solveAndPrint(int caseNum) {
    int N;
    cin >> N;
    vector<vector<int>> total;
    for (int i = 0; i < N * (2 * N - 1); i++) {
        int tmp;
        cin >> tmp;
        bool has = false;
        for (auto &item : total) {
            if (item[0] == tmp) {
                item[1] = item[1] + 1;
                has = true;
                break;
            }
        }
        if (!has) {
            total.push_back({tmp, 1});
        }
    }

    vector<int> resultList;
    for (auto item : total) {
        if (item[1] % 2 != 0) {
            resultList.push_back(item[0]);
        }
    }
    std::sort(resultList.begin(), resultList.end());

    if (resultList.size() != N) {
        cout << "Incorrect size" << endl;
        cout << "size is: " << resultList.size() << "  "
             << "expected: " << N << endl;
        return;
    }
    cout << "Case #" << caseNum << ": ";
    for (auto i : resultList) {
        cout << i << " ";
    }
    cout << endl;
}
