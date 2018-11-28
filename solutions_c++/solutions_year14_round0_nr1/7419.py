#include <fstream>
#include <vector>
using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

const int N = 16;
int used[N];
const int row[] = {1, 1, 1, 1,
                   2, 2, 2, 2,
                   3, 3, 3, 3,
                   4, 4, 4, 4};

void clear() {
    for (int i = 0; i < N; i++)
        used[i] = 0;
}

void read() {
    int ans, x;
    in >> ans;
    for (int i = 0; i < N; i++) {
        in >> x;
        x--;
        if (ans == row[i])
            used[x]++;
    }
}

void print(int c) {
    vector<int> v;
    for (int i = 0; i < N; i++) {
        if (used[i] == 2) {
            v.push_back(i + 1);
        }
    }
    out << "Case #" << c << ": ";
    if (v.size() == 1) {
        out << v[0] << '\n';
    } else if (v.size() > 1) {
        out << "Bad magician!\n";
    } else {
        out << "Volunteer cheated!\n";
    }
}

int main() {
    int t;
    in >> t;
    for (int i = 0; i < t; i++) {
        clear();
        read();
        read();
        print(i + 1);
    }
    return 0;
}
