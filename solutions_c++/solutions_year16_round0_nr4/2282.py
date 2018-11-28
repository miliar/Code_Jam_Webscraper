#include <iostream>

using namespace std;
typedef long long ll;

int main()
{
    int n;
    cin >> n;
    int count = 0;
    while (n--)
    {
        long long arr[105] = { 0 };
        count++;
        cout << "Case #" << count << ": ";
        ll K, C, S;
        cin >> K >> C >> S;
        long long cur = K;
        for (int i = 1; i <= K; i++)
            arr[i] = i;
        for (int j = 0; j < C-1; j++)
        {
            for (int i = 1; i <= K; i++)
                arr[i] = K * (arr[i] - 1) + (i);
        }
        for (int i = 1; i <= K; i++)

            cout << arr[i] << " ";
        cout << endl;
    }
    return 0;
}