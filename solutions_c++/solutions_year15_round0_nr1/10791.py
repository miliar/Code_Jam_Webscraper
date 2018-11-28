#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int tests;
    cin>>tests;
    for(int times=0;times<tests;times++)
    {
        int stand=0;
        int ans=0;
        int maximums;
        int shyness;
        cin>>maximums>>shyness;
        vector<int> shy;
        for(int j=0;j<=maximums;j++)
        {
            shy.push_back(shyness%10);
            shyness/=10;
        }
        reverse(shy.begin(),shy.end());
        for(int i=0;i<shy.size();i++)
        {
            //cout<<shy[i]<<" "<<stand<<" "<<ans<<endl;
            if(stand>=i)
                stand+=shy[i];
            else
            {
                ans+=i-stand;
                stand+=i-stand;
                if(stand>=i)
                    stand+=shy[i];

            }
        }
        cout<<"Case #"<<times+1<<": "<<ans<<endl;
    }

}
