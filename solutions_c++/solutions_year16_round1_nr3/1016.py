#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int n,f[1000];
int main()
{
    int t,tt,i,j,l,lmax;
    cin>>t;
    for (tt=1;tt<=t;tt++)
    {
        cin>>n;
        for (i=0;i<n;i++)
        {
            cin>>f[i];
            f[i]--;
        }
        lmax=0;
        for (i=(1<<n)-1;i>=0;i--)
        {
            vector<int> v;
            for (j=0;j<n;j++) if (i&(1<<j)) v.push_back(j);
            l=v.size();
            do
            {
                for (j=0;j<l;j++)
                {
                    if (f[v[j]]!=v[(j+1)%l]&&f[v[j]]!=v[(j+l-1)%l]) break;
                }
                if (j==l) lmax=max(lmax,l);
            } while (next_permutation(v.begin(),v.end()));
        }
        cout<<"Case #"<<tt<<": "<<lmax<<endl;
    }
    return 0;
}
