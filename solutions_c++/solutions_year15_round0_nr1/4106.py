#include <bits/stdc++.h>
//#define DEBUG
using namespace std;

int main()
{

    #ifndef DEBUG

    ifstream in("qa_l.in");
    cin.rdbuf(in.rdbuf());
    ofstream out("qa_l.out");
    cout.rdbuf(out.rdbuf());

    #endif

    //ios_base::sync_with_stdio(false);
    int T;
    cin>>T;
    for(int X = 1; X <= T; X++)
    {
        int SMax;
        string S;
        cin>>SMax>>S;
        int cnt = S[0] - '0',ans = 0;
        for(int i = 1; i <= SMax; i++)
        {
            //cout<<cnt<<endl;
            if(cnt < i)
            {
                ans += i - cnt;
                cnt = i;
            }
            cnt += S[i] - '0';
        }
        cout<<"Case #"<<X<<": "<<ans<<endl;

    }
    return 0;
}
