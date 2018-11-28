
#include <iostream>
using namespace std;
inline long long test(long long N)
{
    if (N == 0)
        return -1;

    long long curN = N;
    unsigned short flag = 0;
    for (; (flag & 0x3FF) != 0x3FF; curN += N)
    {
        //cout << curN << " ";
        long long temp = curN;
        while (temp > 0)
        {
            flag |= 1 << (temp % 10);
            temp /= 10;
        }
    }

    return curN - N;
}


int main()
{
    int caseCount;
    cin >> caseCount;
    for (int i = 1; i <= caseCount; ++i)
    {
        long long N;
        cin >> N;
        long long result = test(N);
       // cout << endl;
        if (result == -1)
        {
            cout << "Case #" << i << ": INSOMNIA" << endl;
        }
        else
        {
            cout << "Case #" << i << ": " << result << endl;
        }
    }

    return 0;
}