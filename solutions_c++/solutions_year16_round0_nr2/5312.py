#include <bits/stdc++.h>

using namespace std;

int T;
string curStr;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%d", &T);
    for (int i = 0; i < T; ++i)
    {
        int curState = 0;
        cin>>curStr;
        if (curStr[curStr.size() - 1] == '-') curState++;

       /* int indx = curStr.size() - 1;
        while (indx > 0 and curStr[indx] == '+')
            indx--;

            cout<<indx<<endl;*/

        for (int i = curStr.size() - 2; i >= 0; --i)
        {
            if (curStr[i] != curStr[i + 1]) curState++;
        }
        printf("Case #%d: %d\n", i + 1, curState);
    }
}
