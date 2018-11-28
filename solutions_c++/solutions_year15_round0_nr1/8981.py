#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main()
{
    ifstream cin("a.in");
    ofstream cout("a.out");
    int t;
    cin >> t;
    for(int tt = 0; tt < t; ++tt)
    {
        int n;
        string s;
        cin >> n >> s;
        vector<int> vc(n + 1, 0);
        for(int i = 0; i < vc.size(); ++i)
            vc[i] = s[i] - '0';
        int ans = 0, done = 0;
        for(int i = 0; i < vc.size(); ++i)
        {
            if(!vc[i])
                continue;
            if(done >= i)
                done += vc[i];
            else
            {
                ans += i - done;
                done += i - done;
                done += vc[i];
            }
        }
        cout << "Case #" << tt + 1 << ": " << ans << endl;
    }
    return 0;
}
