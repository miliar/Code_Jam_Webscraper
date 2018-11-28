#include<iostream>
#include<cstdlib>
#include<vector>
using namespace std;

typedef long long LL;

vector<int> v;
vector<int> e;
int E, R, N;
int best;

void calc(int i, int En)
{
    if ( i==v.size())
    {
        int cur =0;
        for (int j=0;j<v.size();++j)
            cur += v[j]*e[j];
        if ( cur > best ) best = cur;
        return;
    }
    for (int j=0;j<=En;++j)
    {
        e[i]=j;
        calc(i+1, min(En-j+R,E));
    }

}

void print(int i, int ans)
{
    cout << "Case #" << i << ": " << ans << endl;
}

int main()
{
    int T;
    cin >> T;
    for (int t=0;t<T;++t)
    {
        v.clear();
        best = 0;
        cin >> E >> R >> N;
        for (int i=0;i<N;++i)
        {
            int x;
            cin >> x;
            v.push_back(x);
        }
        e.assign(v.size(),0);
        calc(0,E);
        print( t+1, best);
    }
}
