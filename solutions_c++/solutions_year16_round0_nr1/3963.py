#include <iostream>
#include <map>

using namespace std;

#define ll long long

map<int, int> tracker;

void Update_Map(ll num) {
    while (num) {
        tracker[num % 10]++;
        num /= 10;
    }
}

bool Can_Sleep() {
    for (map<int, int>::iterator it = tracker.begin(); it != tracker.end();
         ++it) {
        if (!it->second)
            return false;
    }
    return true;
}

void Reinitialize_Map() {
    tracker[0] = 0;
    tracker[1] = 0;
    tracker[2] = 0;
    tracker[3] = 0;
    tracker[4] = 0;
    tracker[5] = 0;
    tracker[6] = 0;
    tracker[7] = 0;
    tracker[8] = 0;
    tracker[9] = 0;
}

void Solve(ll num) {
    ll num_given = num;
    if (num) {
        ll count = 1;
        while (count < 1e17) {
            count++;
            Update_Map(num);
            if (Can_Sleep()) {
                cout << num;
                return;
            } else {
                num = num_given * count;
                continue;
            }
        }
    } else {
        cout << "INSOMNIA";
        return;
    }
}

int main()
{
    int T;
    ll N;

    cin >> T;

    for (int i = 0; i < T; ++i) {
        cin >> N;
        cout << "Case #" << i+1 << ": ";
        Reinitialize_Map();
        Solve(N);
        cout << endl;
    }

    return 0;
}
