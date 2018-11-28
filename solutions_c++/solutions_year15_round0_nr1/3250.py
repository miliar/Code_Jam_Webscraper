#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        int smax;
        string s;
        cin >> smax >> s;
        int result = 0, counter = s[0] - '0';
        for (int i = 1; i <= smax; ++i)
        {
            if (counter < i)
            {
                result += i - counter;
                counter = i;
            }
            counter += s[i] - '0';
        }
        cout << "Case #" << t << ": " << result << endl; 
    }
}