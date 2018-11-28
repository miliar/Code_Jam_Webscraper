#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int numToSleep(int N)
{
    int tmp = 0;
    int tmpN = 0;
    int tmp1 = 0;
    int tmp2 = 0;
    int count = 1;
    unordered_set <int> set;

    if (N <= 0) {
        return -1;
    }

    while (set.size() < 10) {
        tmpN = N * count;
        tmp = tmpN;
        if (tmp < 10) {
            if (set.find(tmp) == set.end()) {
                set.insert(tmp);
            }
        } else {
            do {
                tmp1 = tmp/10;
                tmp2 = tmp%10;
                if (set.find(tmp2) == set.end()) {
                    set.insert(tmp2);
                }
                tmp = tmp1;
            } while(tmp > 0);
        }
        count++;
    }
    return tmpN;
}

int main()
{
    int T = 0;
    int N = 0;
    int rc = 0;
    vector <int> v;

    cin >> T;
    cin.get();

    for (int i=0; i<T; i++) {
        cin >> N;
        v.push_back(N);
        cin.get();
    }

    for (int j=0; j<T; j++) {
        rc = numToSleep(v[j]);
        if (rc < 0) {
            cout << "Case #" << j+1 << ": "<< "INSOMNIA" << endl;
        } else {
            cout << "Case #" << j+1 << ": "<< rc << endl;
        }
    }
    return 0;
}
