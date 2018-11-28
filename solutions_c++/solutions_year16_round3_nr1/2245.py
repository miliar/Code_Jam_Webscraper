#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    int T, n, *p, sum, maxm, maxi0, maxi1, maxi2;
    cin >> T;
    for(int t=1;t<=T;++t)
    {
        cin >> n;
        p = new int[n];
        sum = 0;
        maxm = -1;
        maxi0 = maxi1 = maxi2 = -1;
        for(int i=0;i<n;++i)
        {
            cin >> p[i];
            sum += p[i];
        }
        cout << "Case #" << t << ":";
        while(1)
        {
            for(int i=0;i<n;++i)
            {
                if(p[i] > maxm)
                {
                    maxm = p[i];
                    maxi0 = i;
                }
                else if(p[i] == maxm && (maxi1 == -1 || (maxi1 != -1 && p[maxi1] != maxm)))
                {
                    maxi1 = i;
                }
                else if(p[i] == maxm)
                {
                    maxi2 = i;
                }
            }
//            cout << " maxm:" << maxm << " maxi0:" << maxi0 << " maxi1:" << maxi1 << " maxi2:" << maxi2 << endl;
            if(maxm == 0)
            {
                cout << endl;
                break;
            }
            else if(maxi0 != -1 && maxi1 != -1 && maxi2 != -1 && p[maxi0] == p[maxi1] && p[maxi1] == p[maxi2])
            {
                cout << " " << char(maxi0+'A');
                p[maxi0]--;
                sum -= 1;
            }
            else if(maxi0 != -1 && maxi1 != -1 && p[maxi0] == p[maxi1])
            {
                cout << " " << char(maxi0+'A') << char(maxi1+'A');
                p[maxi0]--;
                p[maxi1]--;
                sum -= 2;
            }
            else if(maxi0 != -1)
            {
                cout << " " << char(maxi0+'A');
                p[maxi0]--;
                sum -= 1;
            }
            else
            {
                cout << endl;
                break;
            }
            maxm = maxi0 = maxi1 = maxi2 = -1;
        }
        free(p);
    }
    return 0;
}

