#include <bits/stdc++.h>

using namespace std;

#define MAX 100005;
#define INF 0x3f3f3f3f
#define MOD 1000000007
#define PI 3.14159265359
#define pb push_back
#define ppb pop_back()
#define sz size()
#define fi first
#define se second
#define all(c) (c).begin(), (c).end()

typedef unsigned long long ull;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<string> vs;
typedef pair<int,int> pii;

int a[17][17];
int ans, t;
int pos[17];
int ret, cnt;

int main()
{
    freopen("A-small-attempt0.in", "r",stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    //freopen("output.txt", "w", stdout);
    //freopen("dualpal.in", "r",stdin);
    //freopen("dualpal.out", "w", stdout);

    cin >> t;
    for(int test = 1 ; test <= t ; test++)
    {
        memset(pos, 0, sizeof(pos));
        cout << "Case #" << test << ": ";

        ret = 0; cnt = 0;

        cin >> ans;
        for(int i = 1 ; i <= 4 ; i++) for(int j = 1 ; j <= 4 ; j++) cin >> a[i][j];
        for(int i = 1 ; i <= 4 ; i++) pos[a[ans][i]]++;

        cin >> ans;
        for(int i = 1 ; i <= 4 ; i++) for(int j = 1 ; j <= 4 ; j++) cin >> a[i][j];
        for(int i = 1 ; i <= 4 ; i++) pos[a[ans][i]]++;

        for(int i = 1 ; i <= 16 ; i++)
            if(pos[i] == 2)
            {
                cnt++;
                ret = i;
            }
        if(cnt > 1) cout << "Bad magician!";
        else if(cnt < 1) cout << "Volunteer cheated!";
        else cout << ret;
        cout << endl;
    }


    return 0;
}
