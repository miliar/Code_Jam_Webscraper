#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#define ll long long
using namespace std;

int ar[5][5];
int br[20];

int main()
{
    freopen("0.in","r",stdin);
    freopen("0.out","w",stdout);

    int a,b,c,d,e,x,y,z,t;

    cin>>t;

    for(int i=1;i<=t;i++)
    {
        cin>>z;
        z--;
        for(a=0;a<4;a++)
        {
            for(b=0;b<4;b++) cin>>ar[a][b];
        }
        for(a=0;a<=16;a++) br[a]=0;

        for(a=0;a<4;a++) br[ ar[z][a] ]++;

        cin>>z;
        z--;
        for(a=0;a<4;a++)
        {
            for(b=0;b<4;b++) cin>>ar[a][b];
        }
        e=0;
        b=0;
        for(a=0;a<4;a++) if(br[ ar[z][a] ]) br[ ar[z][a] ]++;

        for(a=0;a<=16;a++)
        {
            if(br[a]==2)
            {
                e=e+br[a];
                b=a;
            }
        }
        if(e==2)
        {
            cout<<"Case #"<<i<<": "<<b<<endl;
            continue;
        }
        if(e==0)
        {
            cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
            continue;
        }
        cout<<"Case #"<<i<<": Bad magician!"<<endl;

    }


    return 0;
}
