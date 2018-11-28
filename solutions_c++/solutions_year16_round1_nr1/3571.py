#include <iostream>
#include <string>

using namespace std;

string solve(string inp)
{
    string s = "";
    s += inp[0];

    for(int i = 1; i < inp.length(); i++) {
        if(inp[i] >= s[0]) {
            s = inp[i] + s;
        } else {
            s += inp[i];
        }
    }
    return s;
}

int main()
{
    string s;
    int cases, i, j;

    cin >> cases;

    for (i = 1; i <= cases; i++) {
        cin >> s;
        cout << "Case #" << i << ": " << solve(s) << "\n";
    }
    return 0;
}
