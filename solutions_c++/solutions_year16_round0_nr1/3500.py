#include <iostream>
#include <set>
using namespace std;

int main ()
{
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N, i = 1, temp;
        set<char> s;
        s.clear();
        cin >> N;
        if (!N) {
            cout << "Case #" << t + 1 << ": " << "INSOMNIA" << endl;
            continue;
        }
        while (s.size() != 10) {
            temp = i * N;
            for (char c : to_string(temp))
                s.insert(c);
            i++;
        }
        cout << "Case #" << t + 1 << ": " << temp << endl;
    }
    return 0;
}
