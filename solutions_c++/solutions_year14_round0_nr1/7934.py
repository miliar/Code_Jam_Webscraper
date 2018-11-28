#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;
int Tcase,t;
int a[5][5];
int b[5][5];
int arow,brow;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>Tcase;
    for(t=1;t<=Tcase;t++)
    {
        cin>>arow;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>a[i][j];
        cin>>brow;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>b[i][j];
        vector<int> ans;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(a[arow-1][i]==b[brow-1][j])
                    ans.push_back(a[arow-1][i]);
            }
        }
        if(ans.size()==0)
        {
            cout<<"Case #"<<t<<": Volunteer cheated!"<<endl;
        }
        else if(ans.size()>1)
        {
            cout<<"Case #"<<t<<": Bad magician!"<<endl;
        }
        else
            cout<<"Case #"<<t<<": "<<ans[0]<<endl;

    }
    return 0;
}
