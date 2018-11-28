#include <iostream>
#include <algorithm>
#include <vector>
#include <cassert>

using namespace std;

bool checkThem(vector<char> & output, int i, int j, int width) {
    for (int w = 0; w < width / 2; ++w) {
        if (output[j + w] < output[i + w])
            return true;
        if (output[i + w] > output[j + w])
            return false;
    }
    return false;
}
void switchThem(vector<char> & output, int i, int j, int width) {
    for (int w = 0; w < width / 2; ++w) {
        char tmp;
        tmp = output[i + w];
        output[i + w] = output[j + w];
        output[j + w] = tmp;
    }
}
void sortThem(vector<char> & output) {
    for (int width = 2; width <= output.size(); width *= 2) {
        for (int i = 0; i < output.size(); i += width) {
            if (checkThem(output, i, i + (width / 2), width))
                switchThem(output, i, i + (width / 2), width);
        }
    }
}

void tryOne(int lvl, int N, vector<char> & output) {
    if (lvl == N)
        return;
    vector<char> newOutput;
    for (char c : output) {
        if (c == 'P') {
            newOutput.push_back('P');
            newOutput.push_back('R');
        }
        if (c == 'R') {
            if (lvl + 1 == N)
            {
                newOutput.push_back('R');
                newOutput.push_back('S');
            }
            else
            {
                newOutput.push_back('S');
                newOutput.push_back('R');
            }
        }
        if (c == 'S') {
            newOutput.push_back('P');
            newOutput.push_back('S');
        }
    }
    output = newOutput;
    tryOne(lvl + 1, N, output);
}

bool isValid(vector<char> output, int R, int P, int S) {
    return count(output.begin(), output.end(), 'P') == P && count(output.begin(), output.end(), 'R') == R && count(output.begin(), output.end(), 'S') == S;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N, R, P, S;
        cin >> N >> R >> P >> S;
        vector<char> output, output2, output3;
        output.push_back('P');
        output2.push_back('R');
        output3.push_back('S');
        tryOne(0, N, output);
        tryOne(0, N, output2);
        tryOne(0, N, output3);
        assert(output.size() == R + P + S);
        assert(output2.size() == R + P + S);
        assert(output3.size() == R + P + S);
        cout << "Case #" << t << ": ";
        if (isValid(output, R, P, S)) {
            sortThem(output);
            cout << string(output.begin(), output.end());
            assert(!isValid(output2, R, P, S));
            assert(!isValid(output3, R, P, S));
        } else if (isValid(output2, R, P, S)) {
            sortThem(output2);
            cout << string(output2.begin(), output2.end());
            assert(!isValid(output, R, P, S));
            assert(!isValid(output3, R, P, S));
        } else if (isValid(output3, R, P, S)) {
            sortThem(output3);
            cout << string(output3.begin(), output3.end());
            assert(!isValid(output, R, P, S));
            assert(!isValid(output2, R, P, S));
        } else {
            cout << "IMPOSSIBLE";
        }
        cout << endl;
    }

    return 0;
}
