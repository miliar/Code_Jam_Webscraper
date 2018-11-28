#include <iostream>
#include <fstream>
#include <vector>
using namespace std;




int main()
{
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    int n;
    cin >> n;

    vector <int> ans(n);
    for(int i = 0;i < n;++i)
    {
         int m;
    cin >> m;
    char c;
    int max_r = 0;
    int dop = 0;
    for(int i = 0;i <= m;++i)
    {
        cin >> c;
        if(max_r >= i || c == '0')
        {
            max_r += (c - '0');
        }
        else
        {
            dop += (i - max_r);
            max_r = i + (c - '0');
        }
    }
    ans[i] = dop;
    }


    for(int i = 0;i < n;++i)
        cout << "Case #" << i + 1 << ": " << ans[i] << endl;

    return 0;
}
