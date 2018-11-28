#include <iostream>
#include <string>
using namespace std;
typedef pair<bool, char> quaternion;

quaternion multiply(quaternion a, quaternion b) {
    bool positive = !(a.first ^ b.first);
    switch (a.second) {
        case '1':
            return quaternion(positive, b.second);
        case 'i':
            switch (b.second) {
                case '1':
                    return quaternion(positive, 'i');
                case 'i':
                    return quaternion(!positive, '1');
                case 'j':
                    return quaternion(positive, 'k');
                case 'k':
                    return quaternion(!positive, 'j');
            }
        case 'j':
            switch (b.second) {
                case '1':
                    return quaternion(positive, 'j');
                case 'i':
                    return quaternion(!positive, 'k');
                case 'j':
                    return quaternion(!positive, '1');
                case 'k':
                    return quaternion(positive, 'i');
            }
        case 'k':
            switch (b.second) {
                case '1':
                    return quaternion(positive, 'k');
                case 'i':
                    return quaternion(positive, 'j');
                case 'j':
                    return quaternion(!positive, 'i');
                case 'k':
                    return quaternion(!positive, '1');
            }
    }
    __builtin_unreachable();
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    string str;
    int tc, len, times;
    cin >> tc;
    for (int a = 0; a < tc; ++a) {
        cin >> len >> times >> str;
        string newstr;
        while (times--) newstr += str;
        bool valid = false;
        quaternion current = quaternion(true, '1');
        char status = 'k';
        while (!newstr.empty() && !valid) {
            current = multiply(quaternion(true, newstr.back()), current);
            if (current.second == status && current.first) {
                if (status == 'i') {
                    quaternion check = quaternion(true, '1');
                    for (int b = 0; b < newstr.size() - 1; ++b) {
                        check = multiply(check, quaternion(true, newstr[b]));
                    }
                    valid = check == quaternion(true, '1');
                    break;
                } else {
                    --status;
                    current = quaternion(true, '1');
                }
            }
            newstr.pop_back();
        }
        cout << "Case #" << a + 1 << ": " << (valid ? "YES" : "NO") << "\n";
    }
    return 0;
}