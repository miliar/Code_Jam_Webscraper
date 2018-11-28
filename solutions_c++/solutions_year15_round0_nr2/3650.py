#include <iostream>
#include <fstream>
#include <vector>
using namespace std;




int main()
{
    //ifstream cin("input.txt");
    //ofstream cout("output.txt");
    int n;
    cin >> n;

    vector <int> ans(n);
    for(int i = 0;i < n;++i)
    {
        int m;
        int r;
        int cnt = 0;
        int dop = 1000*1000*1000;
        cin >> m;
        vector <int> num(m);
        for(int j = 0; j < m;++j)
        {
            cin >> num[j];
            r = max(r,num[j]);
        }

        for(int j= 1;j <= r; ++j)
        {
            cnt = j;
            for(int k = 0;k < m;++k)
            {
                cnt += (num[k] + j - 1)/j - 1;
            }
            dop = min(dop, cnt);
        }

        ans[i] = dop;
    }


    for(int i = 0;i < n;++i)
        cout << "Case #" << i + 1 << ": " << ans[i] << endl;

    return 0;
}

