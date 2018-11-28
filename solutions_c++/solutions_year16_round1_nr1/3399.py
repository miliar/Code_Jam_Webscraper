#include <bits/stdc++.h>

using namespace std;

#define REP(i, a, b) for(int i = int(a); i < int(b); i++)

int main(int argc, char** argv)
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    REP(t, 1, T + 1)
    {
        string str, result;
        cin >> str;
        cout << "Case #" << t << ": " ;

        int length = str.length();

        result += str[0];
        REP(i, 1, length)
        {
            if(str[i] >= result[0]) {
                result.insert(0, 1, str[i]);
            } else {
                result += str[i];
            }
        }

        cout << result << endl;
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}