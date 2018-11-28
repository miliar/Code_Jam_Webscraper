#include <iostream>
#include <cstdio>
#include <algorithm>
#include <memory.h>

using namespace std;

int main()
{
    //freopen("q.in","r",stdin);
    freopen("output.out","w",stdout);
    int t, cur = 0;
    cin >> t;
    for(int r = 1; r <= t; r++)
    {
        int x, y, num = 0, cur = 0, q, a[20], idx;
        memset(a,0,sizeof(a));
        cin >> x;
        for(int i = 1; i <= 4; i++)
            for(int j = 1; j <= 4; j++)
            {
                cin >> q;
                if(i == x)
                    a[q] = 1;
            }
        cin >> y;
        for(int i = 1; i <= 4; i++)
        {
            for(int j = 1; j <= 4; j++)
            {
                cin >> q;
                if(i != y) continue;
                if(a[q]) num++, idx = q;
            }
        }
        cout << "Case #" << r << ": " ;
        if(num == 1) cout <<  idx << endl;
        else if(num == 0) cout <<  "Volunteer cheated!"<< endl;
        else cout << "Bad magician!" << endl;
    }
    return 0;
}
