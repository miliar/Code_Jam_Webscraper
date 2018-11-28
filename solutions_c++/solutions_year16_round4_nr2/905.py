#include <bits/stdc++.h>
#include <iomanip>
using namespace std;

typedef double rl;

const int MX=209;

struct poly
{
    //vector<rl> V;
    rl V[MX];
};

poly ONE()
{
    poly result;
    //result.V.resize(1);
    result.V[0]=1.0;
    for(int i=1; i<MX; i++) result.V[i]=0;
    return result;
}

poly mul(const poly& A, rl a, rl b) // *(a+bx)
{
    //int N=A.size();
    poly R;

    R.V[0]=A.V[0]*a;

    for(int i=1; i<MX; i++)
    {
        R.V[i]=A.V[i]*a+A.V[i-1]*b;
    }

    return R;
}

rl P[MX];
int N, K;

rl probability(bool* marked)
{
    int kk=0;
    poly R=ONE();
    for(int i=0; i<N; i++)
    {
        if(marked[i])
        {
            //cout << "marked:" << i << endl;

            kk++;
            R=mul(R, 1.0-P[i], P[i]);
        }
    }

    assert(kk==K);

    /*
    cout << "---------" << endl;
    for(int i=0; i<N; i++) cout << R.V[i] << ' ';
    cout << "-----------" << endl;
    */

    return R.V[K/2];
}

typedef unsigned int ui;

rl solve()
{
    rl result=0.0;

    assert(N<=16);

    for(ui mask=0; mask<(1U<<N); mask++)
    {


        int kk=0;
        //ui temp=mask;

        bool marked[MX];

        for(int i=0; i<N; i++)
        {
            kk += (mask>>i)&1;
            marked[i]=((mask>>i)&1)?true:false;
        }

        if(kk==K)
        {
            //cout << "MASK: " << bitset<4>(mask) << endl;
            result=max(result, probability(marked));
        }
    }

    return result;

}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    cout << setprecision(10) << fixed;

    int T;
    cin >> T;
    for(int t=1; t<=T; t++)
    {
        //int N;
        //cin >> N;
        //int result=solve(N);
        cin >> N >> K;
        for(int i=0; i<N; i++) cin >> P[i];

        rl res=solve();

        cout << "Case #" << t << ": " << res << endl;
    }
    return 0;
}
