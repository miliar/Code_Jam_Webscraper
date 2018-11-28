#include<bits/stdc++.h>
#define rep(i,k,n) for(int i= (int) k;i< (int) n;i++)
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define ft first
#define sd second
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef unsigned int uint;
const long long INF = 4e18L + 1;
const int IINF = 2e9 + 1;
const int limit = 1048576;
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
//     cin.tie(0);
    int T; cin >> T;
    rep(t, 1, T + 1)
    {
        int n; cin >> n;
        if(n == 0)
        {
            cout << "Case #" << t << ": INSOMNIA" << "\n";
            continue;
        }
        int current = 0;
        vector<bool>done(10, false);
        while(count_if(all(done), [](bool a){return a;}) != 10)
        {
            current += n;
            int temp = current;
            while(temp)
            {
                done[temp % 10] = true;
                temp /= 10;
            }
        }
        cout << "Case #" << t << ": " << current << "\n"; 
    }
    return 0;
}