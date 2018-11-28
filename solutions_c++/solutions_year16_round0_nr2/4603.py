#include <iostream>
#include <string>
using namespace std;

string transform(string& s)
{
    string result;
    int last_c = ' ';
    for(int i = 0; i< s.size(); ++i)
    {
        if (s[i] != last_c)
        {
            last_c = s[i];
            result += last_c;
        }
    }
    return result;
}


int main()
{
    int test_cases;
    cin >> test_cases;
    for (int t = 0; t < test_cases; ++t)
    {
        string s;
        cin >> s;
        s = transform(s);
        int result = s.size();
        if (s[s.size() - 1] == '+')
            result--;
        cout << "Case #" << t + 1 << ": " << result << endl;
    }

}
