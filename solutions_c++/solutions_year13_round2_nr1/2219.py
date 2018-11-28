#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

void writeAnswer(int testCount, int answer) {
    out << "Case #" << testCount + 1 << ": " << answer << endl;
}

int main() {
    int T;

    in >> T;
    for (int t=0; t < T; t++) {

        if (t == 15) {
            cerr << "trololo";
        }
        int n, mainSize;
        in >> mainSize >> n;
        vector <int> sizes;
        for (int i=0; i < n; i++) {
            int x;
            in >> x;
            sizes.push_back(x);
        }

        sort(sizes.begin(), sizes.end());

        cerr << "Test " << t << endl;
        cerr << mainSize << endl;
        for (int i=0; i < n; i++) {
            cerr << sizes[i] << " ";
        }

        cerr << endl;

        int result = 0;

        for (int i=0; i < n; i++) {
            if (mainSize > sizes[i]) {
                mainSize += sizes[i];
            } else {
                int x = mainSize;
                int count = 0;

                if (x != 1) {
                    while (x <= sizes[i]) {
                        x += x - 1;
                        count++;
                    }
                } else {
                    count = n + 2100;
                }

                if (count < n - i) {
                    result += count;
                    mainSize = x + sizes[i];
                } else {
                    result += n - i;
                    break;
                }
            }
        }

        writeAnswer(t, result);
        cerr << "result: " << result << endl;
    }
    return 0;
}
