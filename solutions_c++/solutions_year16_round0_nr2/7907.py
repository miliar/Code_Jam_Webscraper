
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);

    int z;
    cin >> z;
    for(int i = 1; i <= z; i++)
    {
        string s;
        cin >> s;
        s += '+';

        int cnt = 0;
        for(int i = 1; i < s.size(); i++)
            if(s[i] != s[i-1])
                cnt++;

        cout << "Case #" << i << ": " << cnt << endl;
    }

    return 0;
}
