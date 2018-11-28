#include <iostream>
#include <string.h>
#include <string>
#include <math.h>
#include <stdio.h>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <list>
#include <vector>
#include <deque>
#include <functional>
using namespace std;

int main()
{

    freopen("A-small-attempt0.in","r",stdin);
    freopen("o.out","w",stdout);
    int i,j,k,l,t,arr[10000],n,sum1,sum2,max;
    cin>>t;
    for (i=0;i<t;i++)
    {
        cout<<"Case #"<<i+1<<": ";
        cin>>n;
        sum1=0;
        sum2=0;
        max=0;
        for (j=0;j<n;j++)
        {
            cin>>arr[j];
            if (j==0)continue;
            if (arr[j-1]-arr[j]>max)max=arr[j-1]-arr[j];
            if (arr[j-1]>arr[j])sum1+=arr[j-1]-arr[j];
        }
        for (j=0;j<n-1;j++)
        {
            sum2+=min(arr[j],max);
        }
        cout<<sum1<<" "<<sum2<<endl;
    }
    return 0;
}
