#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const int MOD = 1000000007;

vector<string> S;
int N, MaxSize, Count;

inline int LCP(const string &a, const string &b) {
    int p = 0;
    for (; p < int(a.length()) && p < int(b.length()) && a[p] == b[p]; ++p);
    return p;
}

inline int GetTrieSize(vector<string> stringSet) {
    if (stringSet.empty())
        return 0;
    int size = 1;
    sort(stringSet.begin(), stringSet.end());
    size += int(stringSet[0].length());
    for (int i = 0; i + 1 < int(stringSet.size()); ++i)
        size += int(stringSet[i + 1].length()) - LCP(stringSet[i], stringSet[i + 1]);
    return size;
}

void Back(vector<int> &servers, const int index) {
    if (index == int(S.size())) {
        vector< vector<string> > sets = vector< vector<string> >(N, vector<string>());
        for (int i = 0; i < int(S.size()); ++i)
            sets[servers[i]].push_back(S[i]);
        int size = 0;
        for (int i = 0; i < N; ++i)
            size += GetTrieSize(sets[i]);
        if (size > MaxSize) {
            MaxSize = size;
            Count = 0;
        }
        if (size == MaxSize)
            Count = (Count + 1) % MOD;
        return;
    }
    for (servers[index] = 0; servers[index] < N; ++servers[index])
        Back(servers, index + 1);
    servers[index] = -1;
}

int main() {
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    int testCount;
    cin >> testCount;
    for (int test = 1; test <= testCount; ++test) {
        int setSize;
        cin >> setSize >> N;
        S = vector<string>(setSize, "");
        for (int i = 0; i < setSize; ++i)
            cin >> S[i];
        vector<int> servers = vector<int>(setSize, -1);
        MaxSize = Count = 0;
        Back(servers, 0);
        cout << "Case #" << test << ": " << MaxSize << " " << Count << "\n";
    }
    cin.close();
    cout.close();
    return 0;
}
