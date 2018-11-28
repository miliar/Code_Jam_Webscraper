#include <iostream>
#include <map>

using namespace std;

int minCnt;
map<string, int> hashMap;

// int steps[100];
// int final[100];

string reversePancake(string pancake, int index) {
    string reversed;
    for (int i = index; i >= 0; --i) {
        reversed += pancake[i] == '+' ? '-' : '+';
    }
    reversed += pancake.substr(index + 1);

    return reversed;
}

void search(string order, int cnt) {
    if (hashMap.find(order) != hashMap.end() && cnt >= hashMap[order]) {
        return;
    } else {
        hashMap[order] = cnt;
    }

    size_t endPos = order.find_last_not_of('+');

    if (endPos == string::npos) {
        if (cnt < minCnt) {
            minCnt = cnt;
            // for (int i = 0; i < cnt; ++i) {
            //     final[i] = steps[i];
            // }
        }
        return;
    }

    if (cnt + 1 < minCnt) {
        for (int i = endPos; i >= 0; --i) {
            // steps[cnt] = i;
            order = reversePancake(order, i);
            search(order, cnt + 1);
            order = reversePancake(order, i);
        }
    }
}

int main() {
    int t;

    cin >> t;

    for (int i = 0; i < t; ++i) {
        string order;
        cin >> order;

        minCnt = order.size() * 2;
        hashMap.clear();

        search(order, 0);
        cout << "Case #" << i + 1 << ": " << minCnt << endl;
        // for (int i = 0; i < minCnt; ++i) {
        //     cout << final[i] << " ";
        // }
        // cout << endl;
    }

    return 0;
}