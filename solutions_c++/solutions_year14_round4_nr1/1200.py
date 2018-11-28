#include <vector>
#include <iterator>
#include <list>
#include <map>
#include <math.h>
#include <cmath>
#include <set>
#include <queue>
#include <deque>
#include <string>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <string.h>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
    freopen ("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);
    int t,n,m;
    cin>>t;
    for(int F=1;F<=t;F++)
    {
        int arr[10009]={0},arr1[10009]={0},arr2[10009];
        cin>>n>>m;
        for(int f=0;f<n;f++)
        {
            cin>>arr2[f];
        }
        sort(arr2,arr2+n);
        for(int f=n-1;f>=0;f--)
        {
            for(int f1=0;f1<n;f1++)
                if(arr[f1]+arr2[f]<=m&&arr1[f1]<2)
                {
                    arr[f1]+=arr2[f];
                    arr1[f1]++;
                    break;
                }
        }
        int ans=0;
        for(int f=0;f<n;f++)
            if(arr1[f])
                ans++;
        cout<<"Case #"<<F<<": "<<ans<<endl;
    }
}
