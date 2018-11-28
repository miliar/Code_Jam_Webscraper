#include <iostream>
#include <fstream>
#include <set>
#include <vector>
#include <list>
#include <algorithm>
using namespace std;
int main()
{
    ifstream cin("input.in");
    ofstream cout("output.txt");
    int t, z;
    cin>>t;
    for (z=0;z<t;++z)
    {
        int n, x, i, j, k, res=0;
        cin>>n>>x;
        vector<int> v(x+1);
        for (i=0;i<n;++i)
        {
            cin>>k;
            ++v[k];
        }
        i=1;
        while (i<=x)
        {
            if (v[i]==0)
            {
                ++i;
                continue;
            }
            --v[i];
            for (j=x-i;j>=i;--j)
            {
                if (v[j]>0)
                {
                    --v[j];
                    break;
                }
            }
            ++res;
        }
        cout<<"Case #"<<z+1<<": "<<res<<endl;
    }
    return 0;
}
