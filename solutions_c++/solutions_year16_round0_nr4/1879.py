#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int lp=1;lp<=t;++lp)
    {
        int k, c, s;
        cin >> k >> c >> s;
        cout << "Case #" << lp << ":";
        for(int i=1;i<=s;++i)
        {
            cout << " " << i;
        }
        cout << "\n";
    }

    return 0;
}
