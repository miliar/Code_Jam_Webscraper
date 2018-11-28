#include <iostream>
#include <stack>
#include <queue>
#include <cstdlib>

using namespace std;

string flipString(string S, size_t idx)
{
    string cpy = S.substr(0, idx+1);
    for(int i = 0; i <= idx; i++)
        if(cpy[idx-i] == '+')
            S[i] = '-';
        else
            S[i] = '+';
    return S;
}

int numFlips(string S)
{
    int count = 0;
    size_t l = S.length();
    for(int i = 0; i < l - 1; i++)
        if(S[i] != S[i+1]) {
            S = flipString(S, i);
            count++;
        }
    if(S[0] == '-') {
        flipString(S, S.length() - 1);
        count++;
    }
    return count;
}

int main()
{
    int T;
    size_t l;
    string S;
    stack<char> stk;
    cin >> T;
    for(int x = 1; x <= T; x++) {
        cin >> S;
        cout << "Case #" << x << ": " << numFlips(S) << endl;
    }
}
