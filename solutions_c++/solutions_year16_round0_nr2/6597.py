#define _USE_MATH_DEFINES
#include<iostream>
#include<vector>
#include<cstdio>
#include<string>
#include<algorithm>
#include<iomanip>
#include<cmath>
#include<numeric>
#include<map>
#include<stack>
#include<regex>
#include<set>
#include<initializer_list>
#include<tuple>
#include<queue>
#include<functional>
#include<random>
using namespace std;

#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define RFOR(i,a,b) for (int i=(b)-1;i>=(a);i--)
#define REP(i,n) for (int i=0;i<(n);i++)
#define RREP(i,n) for (int i=(n)-1;i>=0;i--)
#define all(a) (a).begin(),(a).end()

const int INFTY = 100000000;
const long long LINFTY = 1e20;
typedef long long ll;
typedef vector<int> vi;
typedef vector<double> vd;

int main()
{
    int T;
    cin >> T;
    vector<string> V(T);
    for (int i = 0; i < T; i++) cin >> V[i];
    int cnt = 0;
    for (auto& S : V)
    {
        cnt++;
        int ans = 0;
        bool reversed = false;
        for (int i = S.size() - 1; i >= 0; i--)
        {
            if (S[i] == '-' && !reversed)
            {
                reversed = !reversed;
                ans++;
            }
            else if (S[i] == '+' && reversed)
            {
                reversed = !reversed;
                ans++;
            }
        }
        cout << "Case #" << cnt << ": "<< ans << endl;
    }
    return 0;
}