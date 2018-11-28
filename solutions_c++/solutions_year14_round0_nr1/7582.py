#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int T,f,s;
    int rec[4][4];
    cin>>T;
    for(int ca=1;ca<=T;ca++)
    {
        cin>>f;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>rec[i][j];
            }
        }
        set<int> S;
        S.clear();
        for(int i=0;i<4;i++)
        {
            S.insert(rec[f-1][i]);
        }
        cin>>s;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>rec[i][j];
            }
        }
        int cnt=0,cwj=-1;
        for(int i=0;i<4;i++)
        {
            if(S.find(rec[s-1][i])!=S.end())
            {
                cnt++;
                cwj=rec[s-1][i];
            }
        }
        printf("Case #%d: ",ca);
        if(cnt==1) cout<<cwj<<endl;
        if(cnt==0) cout<<"Volunteer cheated!"<<endl;
        if(cnt>1) cout<<"Bad magician!"<<endl;
    }
    return 0;
}
