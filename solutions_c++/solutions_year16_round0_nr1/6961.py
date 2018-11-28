#include <iostream>
#include <fstream>

using namespace std;

bool check(bool a[])
{
    for (int i = 0; i < 10; i++)
    {
        if (!a[i])
            return false;
    }

    return true;
}

int main()
{
	//freopen("A-large.in", "r", stdin);
    //freopen("out.txt", "w", stdout);

    int T, case_count = 1;
    long long int N;

    cin >> T;

    while (T--)
    {
        cin >> N;

        if (!N)
        {
            cout << "Case #" << case_count++ << ": " << "INSOMNIA" << endl;
            continue;
        }

        bool digits[10];
        for (int i = 0; i < 10; i++)
            digits[i] = false;

        long long int k = 1;
        long long int ans;

        while (!check(digits))
        {
            long long int M = k*N;
            ans = M;

            while (M)
            {
                digits[M % 10] = true;
                M /= 10;
            }

            k++;
        }

        cout << "Case #" << case_count++ << ": " << ans << endl;
    }

    return 0;
}