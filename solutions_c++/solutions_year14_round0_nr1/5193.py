#include <iostream>

using namespace std;

int row1[5];
int row2[5];

int main()
{
    int t, n, a;
    cin >> t;
    for(int test=1; test<=t; test++)
    {
        cin >> n;
        for(int i=1; i<=4; i++)
        {
            for(int j=1; j<=4; j++)
            {
                if(i == n) cin >> row1[j];
                else cin >> a;
            }
        }

        cin >> n;
        for(int i=1; i<=4; i++)
        {
            for(int j=1; j<=4; j++)
            {
                if(i == n) cin >> row2[j];
                else cin >> a;
            }
        }

        int same = 0;
        int ans;
        for(int i=1; i<=4; i++)
        {
            for(int j=1; j<=4; j++)
                if(row1[i] == row2[j])
                {
                    same++;
                    ans = row1[i];
                }
        }

        if(same == 0) cout << "Case #" << test << ": " << "Volunteer cheated!" << "\n";
        else if(same == 1) cout << "Case #" << test << ": " << ans << "\n";
        else cout << "Case #" << test << ": " << "Bad magician!" << "\n";
    }
    return 0;
}
