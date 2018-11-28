#include <string>
#include <iostream>
using namespace std;

string solve(string s)
{
    string answer;
    for(int i = 0; i < s.length(); ++i) {
        string x = s[i] + answer;
        string y = answer + s[i];
        if(x < y)
            answer = y;
        else
            answer = x;
    }
    return answer;
}

int main(void)
{
    int n;
    string s;
    cin >> n;
    for(int i = 1; i <= n; ++i) {
        cin >> s;
        string answer = solve(s);
        cout << "Case #" << i << ": " << answer << endl;
    }
    return 0;
}
