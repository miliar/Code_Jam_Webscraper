#include <iostream>
#include <fstream>

#define lfo(i,a,b) for (int i=a,_b=b; i<=_b ; ++i)

using namespace std;

int t,first,second,res;
int a[4][4],b[4][4];

int main()
{
    freopen("","r",stdin);
    freopen("","w",stdout);
    cin>>t;
    lfo(k,1,t)
    {
        cin>>first;
        lfo(i,1,4)
        lfo(j,1,4) cin>>a[i][j];
        cin>>second;
        lfo(i,1,4)
        lfo(j,1,4) cin>>b[i][j];
        int count=0;
        lfo(i,1,4)
            lfo(j,1,4)
                if (a[first][i]==b[second][j])
                {
                    count++;
                    res=a[first][i];
                }
        cout<<"Case #"<<k<<": ";
        if (count==1) cout<<res<<endl;
        if (count==0) cout<<"Volunteer cheated!"<<endl;
        if (count>1) cout<<"Bad magician!"<<endl;
    }
    return 0;
}
