#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <set>

using namespace std;

int main()
{
    freopen("D-small-attempt1.in","r",stdin);
    freopen("D-small-attempt1.out","w",stdout);
    int T,C,K,S;
    cin>>T;
    for(int cas = 1;cas <= T;cas ++)
    {
        cin>>K>>C>>S;
        cout<<"Case #"<<cas<<":";
        if(K == 1) cout<<" 1";
        else if(C > 1 && S >= K - 1)
        {
            for(int i = 2;i <= K;i ++)
                cout<<" "<<i;
        }
        else if(C == 1 && S == K)
        {
            for(int i = 1;i <= K;i ++)
                cout<<" "<<i;
        }
        else
            cout<<" IMPOSSIBLE";
        cout<<endl;
    }
    return 0;
}
