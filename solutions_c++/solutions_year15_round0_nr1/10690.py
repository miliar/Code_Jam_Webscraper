#include <iostream>
using namespace std;

int main()
{
    int T, max;
    int result;
    int count;
    string s;
    cin >> T;

    for(int i=0; i<T; ++i)
    {
        result = 0;
        count = 0;
        cin >> max >> s;
        for(int j=0; j<=max; ++j)
        {
            int kth = s[j] - '0';
            if(kth && (j > count))
            {
                int diff = j-count;
                result += diff;
                count += diff;
            }
            count += kth;
        }
        cout << "Case #" << i+1 << ": " << result << "\n";
    }
    return 0;
}
