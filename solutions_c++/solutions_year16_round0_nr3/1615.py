//C.cpp
//Coin Jam
//By phoenixinter@gmail.com
//Apr 9, 2016

#include<iostream>
#include<string>
using namespace std;

int main()
{
    int t, kaseno = 0;
    cin >> t;
    while (t--)
    {
        int n, j;
        cin >> n >> j;
        cout << "Case #" << ++kaseno << ":" << endl;
        int cnt = 0;
        for (int i = 1; i < n - 1; i++)
            for (int k = i + 1; k < n - 1; k += 2)
                for (int i1 = k + 1; i1 < n - 1; i1 += 2)
                    for (int i2 = i1 + 1; i2 < n - 1; i2 += 2)
                    {
                        string str = "";
                        for (int l = 0; l < n; l++)
                        {
                            if (l == 0 || l == i || l == k || l == n - 1 || l == i1 || l == i2) str += '1';
                            else str += '0';
                        }
                        int divisorCnt = 9;
                        /*
                        for (int l = 2; l <= 10; l++)
                        {
                            long long sum = 0;
                            for (int ii = 0; ii < str.size(); ii++)
                                sum = sum * l + (str[ii] - '0');
                            int divisor = l + 1;
                            if (sum % divisor == 0)
                                divisorCnt++;
                        }
                        */
                        if (divisorCnt == 9)
                        {
                            cout << str;
                            for (int l = 3; l <= 11; l++)
                                cout << " " << l;
                            cout << endl;
                            cnt++;
                        }
                        if (cnt == j) goto end;
                    }
    end:;
    }
    return 0;
}