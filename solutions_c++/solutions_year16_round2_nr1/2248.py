#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
using namespace std;

const int MAXN = 2100;

int N;
char s[MAXN];
int cnt[30];
int number[30];

string key[10] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

void solve(int idx)
{
    int len = strlen(s);
    memset(cnt,0,sizeof(cnt));
    memset(number,0,sizeof(number));
    for(int i=0;i<len;i++)
        cnt[ s[i]-'A' ] ++;
    number[0] = cnt['Z'-'A'];
    number[2] = cnt['W'-'A'];
    number[4] = cnt['U'-'A'];
    number[6] = cnt['X'-'A'];
    number[8] = cnt['G'-'A'];

    number[1] = cnt['O'-'A'] - number[0] - number[2] - number[4];
    number[3] = cnt['T'-'A'] - number[2] - number[8];
    number[5] = cnt['F'-'A'] - number[4];
    number[7] = cnt['V'-'A'] - number[5];
    number[9] = cnt['I'-'A'] - number[5] - number[6] - number[8];
//    for(int i=0;i<16;i++) cout << cnt[i] << " "; cout << endl;
    cout << "Case #" << idx << ": ";
    for(int i=0;i<10;i++)
    {
        for(int j=0;j<number[i];j++)
            cout << i;
    }
    cout << endl;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large-out.txt","w",stdout);

    cin >> N;
    for(int i=1;i<=N;i++)
    {
        cin >> s;
        solve(i);
    }

    return 0;
}
