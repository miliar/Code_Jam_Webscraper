#include <cstdio>
#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;

int t, n, y, z;

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("d.out","w",stdout);
    scanf("%d",&t);
    for(int i=1; i<=t; i++)
    {
        y=0;
        z=0;
        scanf("%d",&n);
        map<int,bool> m;
        map<int,bool> dw;
        vector<double> v1(n);
        vector<double> v2(n);
        for(int j=0; j<n; j++) cin>>v1[j];
        for(int j=0; j<n; j++) cin>>v2[j];
        sort(v1.begin(),v1.end());
        sort(v2.begin(),v2.end());
        for(int j=n-1; j>=0; j--)
        {
            for(int i=0; i<n; i++)
            {
                if(v1[i]>v2[j]&&dw[i]==false)
                {
                    y++;
                    dw[i]=true;
                    break;
                }
            }
        }
        for(int j=0; j<n; j++)
        {
            for(int k=0; k<n; k++)
            {
                if(v2[k]>v1[j]&&m[k]==false)
                {
                    z++;
                    m[k]=true;
                    break;
                }
            }
        }
        printf("Case #%d: %d %d\n",i,y,n-z);
    }
}
