#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
    freopen("Aman4.txt", "r", stdin);
    freopen("Question_4_ans.txt", "w", stdout);

    int t;
    cin >> t;
    for(int k = 1; k <= t; k++)
    {
        int x, r, c;
        int flag = 0;
        cin >> x >> r >> c;
        if(x == 1)
            flag = 1;
        else if(x == 2)
        {
            if((r * c) % 2 == 0)
                flag = 1;
        }
        else if(x == 3)
        {
            if((r % 3 == 0 && c != 1) || (c % 3 == 0) && (r != 1))
                flag = 1;
        }
        else if(x == 4)
        {
            if((r >= 4 && c >= 3) || (r >= 3 && c >= 4))
            {
                if(r % 4 == 0 || c % 4 == 0)
                    flag = 1;
            }
        }
        if(flag == 1)
            printf("Case #%d: GABRIEL\n", k);
        else
            printf("Case #%d: RICHARD\n", k);

    }
    return 0;
}
