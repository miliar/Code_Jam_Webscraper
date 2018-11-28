#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cctype>
#include<cmath>
#include<iostream>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<deque>
#include<string>
#include<utility>
#include<algorithm>
using namespace std;

int main()
{
    int T;
    int m1[4][4], m2[4][4];
    int b3, b2, res, c, s1, s2;
    cin >> T;
    for(int testCase=1;testCase<=T;testCase++)
    {
        cin >> s1;
        s1--;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin >> m1[i][j];
            }
        }
        cin >> s2;
        s2--;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin >> m2[i][j];
            }
        }
        c = 0;
        for(b3=0;b3<4;b3++)
        {
            for(b2=0;b2<4;b2++)
            {
                if(m1[s1][b3] == m2[s2][b2])
                {
                    c++;
                    res = m1[s1][b3];
                }
            }
        }

        if(c > 1)
        {
            cout << "Case #" << testCase << ": " << "Bad magician!" << endl;
        }
        else if(c < 1)
        {
            cout << "Case #" << testCase << ": " << "Volunteer cheated!" << endl;
        }
        else
        {
            cout << "Case #" << testCase << ": " << res << endl;
        }

    }
    return 0;
}
