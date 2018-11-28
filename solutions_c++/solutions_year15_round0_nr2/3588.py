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
        int n;
        cin >> n;
        vector<int> A(n);
        for (int i = 0; i < n; ++i)
            cin >> A[i];
        int MAX = 0;
        for (int i = 0; i < n; ++i)
            MAX = max(MAX, A[i]);
        int answer = MAX;
        for (int amount = 2; amount < MAX; ++amount)
        {
            int current = 0;
            for (int i = 0; i < n; ++i)
                current += (A[i] + amount - 1) / amount - 1;
            answer = min(answer, amount + current);
        }
        cout << "Case #" << q + 1 << ": " << answer << endl;
    }
}
