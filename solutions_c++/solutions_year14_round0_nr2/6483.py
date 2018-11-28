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

double C, F, X, s, currentRate, ret;
int t;

int main()
{
    //freopen("input.txt", "r", stdin);
    freopen("B-large.in", "r",stdin);
    freopen("B-large.out", "w", stdout);
    //freopen("output.txt", "w", stdout);
    //freopen("dualpal.in", "r",stdin);
    //freopen("dualpal.out", "w", stdout);

    cin >> t;
    for(int test = 1 ; test <= t ; test++)
    {
        cin >> C >> F >> X;
        ret = 0.0; s = 0.0;
        currentRate = 2;
        while(true)
        {
            if(X / currentRate < (C / currentRate + X / (currentRate + F)))
            {
                ret += X / currentRate;
                break;
            }
            else
            {
                ret += C / currentRate;
                currentRate += F;
            }
        }
        printf("Case #%d: %.6f\n", test, ret);
        //cout << "Case #" << test << ": " << ret << endl;
    }


    return 0;
}
