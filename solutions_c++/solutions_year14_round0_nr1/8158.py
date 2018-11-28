#include "bits/stdc++.h"
using namespace std;
int test(int id)
{
    vector<int> v1[10], v2[10];
    vector<int> V1;
    vector<int> V2;
    int t,ans;
    int r1,r2;
    cin>>r1;
    for (int i=1; i<=4; i++)
    {
        for (int j=0; j<4; j++)
        {
            cin>>t;
            v1[i].push_back(t);
        }
    }
    V1 = v1[r1];
    cin>>r2;

    for (int i=1; i<=4; i++)
    {
        for (int j=0; j<4; j++)
        {
            cin>>t;
            v2[i].push_back(t);
        }
    }

    V2 = v2[r2];
    sort(V1.begin(), V1.end());
    sort(V2.begin(), V2.end());
    cout<<"Case #"<<id<<": ";
    int c=0;

    for (int i=0; i<4; i++)
    {
        t = V1[i];
        if (binary_search(V2.begin(), V2.end(), t)){c++; ans = t;}
    }
    if (c==0)
    {
        cout<<"Volunteer cheated!\n";
        return 0;
    }
    if (c==1)
    {
        cout<<ans<<"\n";
        return 0;
    }
    if (c>1)
    {
        cout<<"Bad magician!\n";
        return 0;
    }
    return 0;
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("outA.txt","w",stdout);
    int T; scanf("%d",&T);
    for (int i=1; i<=T; i++)
    {
        test(i);
    }
}
