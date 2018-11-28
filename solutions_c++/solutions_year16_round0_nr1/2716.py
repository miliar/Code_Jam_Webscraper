#include <iostream>
#include <stack>

using namespace std;

bool checkSeen(bool seen[10])
{
    for(int i = 0; i < 10; i++)
        if(seen[i] == false)
            return false;
    return true;
}

stack<int> getDigits(int X)
{
    stack<int> digits;
    for(; X != 0; X/=10) {
        digits.push(X%10);
    }
    return digits;
}

int sheepNumber(int N)
{
    bool seen[10];
    int i;
    if(N == 0)
        return -1;
    stack<int> stk;
    for(i = 1; !checkSeen(seen); i++)
        for(stk = getDigits(N*i); !stk.empty(); stk.pop()) {
            seen[stk.top()] = true;
        }
    return N * (i - 1);
}

int main()
{
    int T, N, Y;
    cin >> T;
    for(int i = 1; i <= T; i++) {
        cin >> N;
        Y = sheepNumber(N);
        cout << "Case #" << i << ": ";
        if(Y == -1)
            cout << "INSOMNIA";
        else
            cout << Y;
        cout << endl;
    }
}
