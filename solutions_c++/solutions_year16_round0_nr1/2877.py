#include <iostream>
#include <string>

using namespace std;

typedef long long ll;

int main()
{
    int n;
    cin >> n;
    int count = 0;
    while (n--)
    {
        ll N;
        int bits[10] = { 0 };
        count++;
        cin >> N;
        int save = N;
        cout << "Case #" << count << ": ";
        if (N == 0)
            cout << "Insomnia" << endl;
        else
        {
            while (true)
            {
            start:
                ll temp;
                temp = N;
                while (temp)
                {
                    bits[temp % 10]++;
                    temp /= 10;
                }
                N += save;
                int found = false;
                for (int i = 0; i < 10; i++)
                {
                    if (!bits[i])
                        goto start;
                }
                cout << N - save << endl;
                break;
            }
        }
    }
        return 0;
}