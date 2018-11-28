#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int ti=0;ti<t;++ti)
    {
        int d;
        cin>>d;
        vector<pair<float, pair<int,int> > > din(d);
        for(int i=0;i<d;++i)
        {
            int c;
            cin>>c;
            din[i].first=c;
            din[i].second.first=c;
            din[i].second.second=1;
        }

        sort(din.rbegin(),din.rend());

        int mtime=din[0].first;

        for(int i=1;i<mtime;++i)
        {
            float u=din[0].second.first;
            int l=(++din[0].second.second);
            din[0].first=u/l;
            sort(din.rbegin(),din.rend());
            mtime=min(mtime,static_cast<int>(ceil(din[0].first)+i));
        }

        cout<<"Case #"<<ti+1<<": "<<mtime<<endl;
    }
    return 0;
}
