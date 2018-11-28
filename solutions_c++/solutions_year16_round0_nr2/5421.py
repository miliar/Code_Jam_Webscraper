#include <array>
#include <vector>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

template <typename T>
void format(int caseId, T &&str) {
    cout << "Case #" << ++caseId << ": " << str << endl;
}

template <typename T>
bool cond(T &&data) {
    for (auto b : data)
        if (!b)
            return false;
    return true;
}

template <typename T>
void update(T &&data, unsigned long num) {
    int first = 0;
    int last = num - 1;
    while (first < last) {
        std::swap(data[first], data[last]);
        data[first] = !data[first];
        data[last] = !data[last];
        ++first;
        --last;
    }
    if (first == last) {
        data[first] = !data[first];
    }
}

template <typename T>
unsigned numPlus(T &&data) {
    unsigned res = 0;
    while (res < data.size() && data[res])
        ++res;
    return res;
}

template <typename T>
void trunc(T &&data) {
    while (data.back())
        data.pop_back();
}

template <typename T>
void play(int caseId, T data) {
    unsigned nMoves = 0;
    trunc(data);
    while (!cond(data)) {
        ++nMoves;
        if (!data[0]) {
            update(data, data.size());
            trunc(data);
        } else {
            update(data, numPlus(data));
        }
    }
    format(caseId, nMoves);
}

int main(int argc, char *argv[]) {
    if (argc == 1)
        return 1;
    ifstream f(argv[1]);

    int nLines;
    f >> nLines;
    for (int i = 0; i < nLines; ++i) {
        vector<bool> v;
        string str;
        f >> str;
        for (auto c : str)  {
            if (c == '-')
                v.push_back(false);
            else if (c == '+')
                v.push_back(true);
            else
                return 1;
        }
        play(i, v);
    }
}
