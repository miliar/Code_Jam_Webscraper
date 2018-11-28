#include <iostream>
#include <cstdio>
#include <string>

using namespace std;
int main()
{
    freopen("/home/shaza/Desktop/Projects/CJam16Q/B-large.in","r",stdin);
    freopen("/home/shaza/Desktop/Projects/CJam16Q/Bout_LARGE.txt","w",stdout);
    int n;
    string t;
    cin >> n;
    int changes;
    for(int i = 0; i < n; i++)
    {
        cin >> t;
        changes = 0;
        for(int j = 1; j < t.size(); j++)
        {
            if(t[j] != t[j -1])
            {
                changes++;
            }
        }
        if(changes > 0)
        {
            if(t[t.size()-1] == '+')
            {
                cout << "Case #" << i + 1 << ": " << changes <<endl;
            }
            else{
                cout << "Case #" << i + 1 << ": " << changes + 1 <<endl;
            }
        }
        else{
            if(t[0] == '+')
            {
                cout << "Case #" << i + 1 << ": " << 0 <<endl;
            }
            else{
                cout << "Case #" << i + 1 << ": " << 1 <<endl;
            }
        }

    }

    return 0;
}
