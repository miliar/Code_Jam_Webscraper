#include <fstream>

using namespace std;

ifstream cin("date.in");
ofstream cout("date.out");

int t,A,B,K,sol;

void solve();

int main()
{
    int i;cin>>t;
    for (i=1;i<=t;i++)
    {
        cin>>A>>B>>K;
        solve();
        cout<<"Case #"<<i<<": "<<sol<<'\n';
    }
    cin.close();cout.close();
    return 0;
}

void solve()
{
    int i,j,nr;sol=0;
    for (i=0;i<A;i++)
        for (j=0;j<B;j++)
        {
            nr=i&j;
            if (nr<K) sol++;
        }
}
