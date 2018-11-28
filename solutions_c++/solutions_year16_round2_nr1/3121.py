#include <bits/stdc++.h>
using namespace std;

#define REP(i, n) for(int i = 0; i < n; i++)
#define RREP(i,n) for(int i = (n)-1; i >= 0; i--)
#define FOR(i, l, r) for(int i = l; i < r; i++)
#define RFOR(i, l,r) for(int i= (l)-1; i>= (r) ; i--)

int s[10] = { 0 };

void solve(int i)
{
    cout << "Case #" << i + 1 << ": ";
    s[4] -= s[0];
    s[9] -= s[6] + s[8];
    s[7] -= s[6];
    s[3] -= s[8];

    s[1] -= s[7];
    s[5] -= s[7];
    s[4] -= s[3];

    s[9] -= s[5];
    
    s[1] -= s[9] * 2;

    REP(i, 10)
    {
        while(s[i] > 0){
            cout << i;
            s[i]--;
        }
    }
    cout << '\n';
}

int main()
{
    int N;
    cin >> N;
    REP(i, N)
    {
        string st;
        cin >> st;
        REP(j, st.size())
        {
            switch(st[j]){
                case 'Z': s[0]++; break;
                case 'N': s[1]++; break;
                case 'W': s[2]++; break;
                case 'H': s[3]++; break;
                case 'R': s[4]++; break;
                case 'V': s[5]++; break;
                case 'X': s[6]++; break;
                case 'S': s[7]++; break;
                case 'G': s[8]++; break;
                case 'I': s[9]++; break;
                default : break;
            }
        }
        solve(i);
    }

}
    


