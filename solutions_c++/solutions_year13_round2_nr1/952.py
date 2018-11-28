#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

typedef long long LL;
typedef vector<int> VI;

#define dbg(x) cerr << #x << " = " << x << " "

void print( int t, int res)
{
    cout << "Case #" << t << ": " << res << endl;
}

int solve_rec( VI& motes, int i, LL A)
{
    if ( motes.size() == i)
    {
        return 0;
    }

    if ( motes[i] < A )
    {
        return solve_rec( motes, i+1, A+motes[i]);
    }

    dbg(A); dbg(motes[i]) << endl;
    int m1 = 10000000, m2;
    if ( A >1)
    {
        int time =0;
        LL A1= A;
        while ( A1 <= motes[i])
        {
            A1 += A1-1;
            time++;
        }
        m1 = solve_rec( motes, i, A1)+time;
    }
    m2 = solve_rec( motes, i+1, A)+1;
    return min(m1,m2);
}

int main()
{
    int T;
    cin >> T;
    for (int t=0;t<T;++t)
    {
        LL A;
        int N;
        cin >> A >> N;
        VI motes;
        for (int i=0;i<N;++i)
        {
            int x;
            cin >> x;
            motes.push_back(x);
        }   
        sort( motes.begin(), motes.end());
        int res = solve_rec( motes, 0, A);
        print( t+1, res);
    }
}
