#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    int Q;
    cin >> Q;
    for (int q = 0; q < Q; ++q)
    {
        int n, answer = 0, current = 0;
        string S;
        cin >> n >> S;
        for (int i = 0; i < n + 1; ++i)
        {
            answer += max(0, i - current);
            current += (S[i] - '0') + max(0, i - current);
        }
        cout << "Case #" << q + 1 << ": " << answer << endl;
    }
}

