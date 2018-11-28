#include <iostream>
#include <stdio.h>

using namespace std;

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int time_limit;
    cin >> time_limit;
/*    string ns[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
    int base[10][26];
    memset(base,0,sizeof(base));
    for (int i = 0; i < 10; i ++)
    {
        for (int j = 0; j < ns[i].length(); j++)
        {
            base[i][ns[i][j]-'A']++;
        }
    }*/

    for (int time_current = 1; time_current <= time_limit; time_current++)
    {
        printf("Case #%d: ",time_current);
        string num;
        cin >> num;
        int count[26];
        memset(count,0,sizeof(count));
        for (int i = 0; i < num.length(); i ++) {
            count[num[i] - 'A']++;
        }
        int ans[10];
        ans[0] = count['Z'-'A'];
        ans[8] = count['G'-'A'];
        ans[6] = count['X'-'A'];
        ans[4] = count['U'-'A'];
        ans[2] = count['W'-'A'];
        ans[5] = count['F'-'A'] - ans[4];
        ans[3] = count['H'-'A'] - ans[8];
        ans[7] = count['V'-'A'] - ans[5];
        ans[9] = count['I'-'A'] - ans[5] - ans[6] -ans[8];
        ans[1] = count['N'-'A'] - ans[9]*2 - ans[7];
        for (int i = 0; i < 10; i++)
        {
            for (int r= 0; r < ans[i]; r++)
            {
                printf("%d",i);
            }
        }
        cout << endl;
    }

}