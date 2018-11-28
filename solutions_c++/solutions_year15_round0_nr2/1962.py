#include <set>
#include <map>
#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
using namespace std;

string path = "/home/nicolai/work/CLionProjects/untitled/";

int main() {
    int N;
    ifstream in(path + "input.txt");
    ofstream out(path + "output.txt");
    in >> N;
    for (int t = 0; t < N; t++) {
        int n;
        in >> n;
        vector<int> v(n);
        int min_time = 0;
        for (int i = 0; i < n; i++) {
            in >> v[i];
            min_time = max(min_time, v[i]);
        }
        for (int i = 1; i < min_time; i++) {
            int add = 0;
            for (int j = 0; j < v.size(); j++)
                add += v[j] / i - 1 + (v[j] % i ? 1 : 0);
            min_time = min(min_time, add + i);
        }
        out << "Case #" << t + 1 << ": " << min_time << endl;
    }
    return 0;
}

