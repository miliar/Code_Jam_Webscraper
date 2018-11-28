#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
const int inf=2000000000;

int main()
{
    ios_base::sync_with_stdio(0);
    int T;
    cin>>T;
    for (int ttt=1; ttt<=T; ttt++)
    {
        int D;
        cin>>D;
        vector <int> V;
        for (int i=0; i<D; i++) {int p; cin>>p; V.push_back(p);}
        sort(V.begin(), V.end());
        int ans=inf;
        for (int out=V[V.size()-1]; out>=1; out--)
        {
            int added=0;
            for (int i=0; i<V.size(); i++)
            {
                if (V[i]<=out) continue;
                if (V[i]%out==0) added+=(V[i]/out)-1;
                else added+=V[i]/out;
            }
            ans=min(ans, out+added);
        }
        cout<<"Case #"<<ttt<<": "<<ans<<"\n";
    }
}
