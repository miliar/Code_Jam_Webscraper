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

const int Maxn = 1000010;
set<int> se;
int ans[Maxn];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    //freopen("out.txt","w",stdout);
    for(int i = 1;i <= 1000010;i ++)
    {
        se.clear();
        int tmp = i;
//        while(tmp % 10 == 0)
//        {
//            //se.insert(0);
//            tmp /= 10;
//        }

        for(int j = 1;;j ++)
        {
            int x = tmp * j;
            while(x)
            {
                se.insert(x % 10);
                x /= 10;
            }
            if(se.size() >= 10)
            {
                //cout<<"i = "<<i<<" j = "<<tmp * j<<endl;
                ans[i] = tmp * j;
                break;
            }
        }
    }
    int T,N;
    cin>>T;
    for(int cas = 1;cas <= T;cas ++)
    {
        cin>>N;

        cout<<"Case #"<<cas<<": ";
        if(N == 0)
            cout<<"INSOMNIA"<<endl;
        else
            cout<<ans[N]<<endl;
    }
    return 0;
}
