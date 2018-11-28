#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <cmath>
#include <algorithm>

using namespace std;
typedef long long int llint;
typedef long int lint;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,n,x;
    double arr1[1005];
    double arr2[1005];
    double arr3[1005];
    double arr4[1005];
    int w=0,dw;
    cin>>t;
    for(x=1;x<=t;x++)
    {
        cin>>n;
        w=0;
        dw=0;
        for(int i=0;i<n;++i)
        {
            cin>>arr1[i];
            arr3[i]=arr1[i];
        }
        for(int i=0;i<n;++i)
        {
            cin>>arr2[i];
            arr4[i]=arr2[i];
        }
        sort(arr1,arr1+n);
        sort(arr2,arr2+n);
        sort(arr3,arr3+n);
        sort(arr4,arr4+n);
        for(int i=n-1;i>=0;i--)
        {
            int flag=1;
            for(int j=n-1;j>=0&&flag;j--)
            {
                if(arr3[i]>arr4[j])
                {
                    flag=0;
                    arr4[j]=1;
                }
            }
            if(!flag)
            {
                dw++;
            }
        }
        for(int i=0;i<n;++i)
        {
            int flag=1;
            for(int j=0;j<n&&flag;++j)
            {
                if(arr2[j]>arr1[i])
                {
                    flag=0;
                    arr2[j]=0.0;
                }
            }
            if(flag)
            {
                w++;
            }
        }
        cout<<"Case #"<<x<<": "<<dw<<" "<<w<<endl;
    }
}
