#include <iostream>

using namespace std;

int GetMinPeople() {
    int maxS;
    cin >> maxS;
    string shyness;
    cin >> shyness;
    
    int needPeople = 0;
    int curPeople = shyness[0] - '0';
    for (size_t i = 1; i < shyness.size(); ++i) {
        int addPeople = curPeople < i;
        needPeople += addPeople;
        curPeople += (shyness[i] - '0') + addPeople;
    }
    
    return needPeople;
}

void Solve() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        // Case #1: 0
        cout << "Case #" << i << ": " << GetMinPeople() << endl;
    }
}

int main(int argc, const char * argv[]) {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    Solve();
    return 0;
}
