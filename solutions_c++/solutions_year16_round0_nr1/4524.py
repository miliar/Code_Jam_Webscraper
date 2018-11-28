#include <iostream>
#include <vector>
#include <set>
using namespace std;

vector<int> get_digits(int n)
{
    vector<int> result;

    return result;
}

int count_sheep(int start)
{
    if (start == 0)
        return -1;

    set<int> seen_digits;
    int n = start;
    while(true)
    {
        int d = n;
        while (d > 0)
        {
            int digit = d % 10;
            if (seen_digits.find(digit) == seen_digits.end())
            {
                seen_digits.insert(digit);
                if (seen_digits.size() == 10)
                    return n;
            }
            d = d / 10;
        }
        n = n + start;
    }
}
int main()
{
    int test_cases;
    cin >> test_cases;
    for(int t = 0; t < test_cases; ++t)
    {
        int n;
        cin >> n;
        int result = count_sheep(n);
        cout << "Case #" << t+1 << ": ";
        if (result == -1)
            cout << "INSOMNIA" << endl;
        else
            cout << result << endl;
    }
}