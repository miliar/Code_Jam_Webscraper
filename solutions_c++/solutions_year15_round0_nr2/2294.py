#include<iostream>
using namespace std;

const int inf = 2*1000*1000*1000 + 7;
int P[1001];


int main() {
    ios_base::sync_with_stdio(0);
    int T;
    cin>>T;

    for(int tt = 1; tt<=T; tt++) {
        int d, m=0, o = inf;
        cin>>d;
        for(int i = 1; i<=d; i++)
        {
            cin>>P[i];
            m=max(m, P[i]);
        }

        for(int i = 1; i<=m; i++) {
            int w = i;
            for(int j = 1; j<=d; j++)
            {
                int q = P[j] / i - 1;
                if( P[j] % i != 0)
                    q++;
                w += q;
            }
            o = min( o, w);
        }

        cout<<"Case #"<<tt<<": "<<o<<endl;
    }
    return 0;
}
