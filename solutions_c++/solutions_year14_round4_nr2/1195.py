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
    int t,n;
    cin>>t;
    for(int F=1;F<=t;F++)
    {
        cin>>n;
        long long arr[1009],arr2[1009],maxi=0;
        for(int f=0;f<n;f++)
        {
            cin>>arr[f];
            if(arr[f]>arr[maxi])
                maxi=f;
            arr2[f]=arr[f];
        }
        long long max1=arr[maxi];
        long long out=1e8;
        sort(arr2,arr2+n);
        do
        {
            int arr3[1009];
            for(int f=0;f<n;f++)
                arr3[f]=arr2[f];
            int maxi1=0;
            long long ans=0;
            for(int f=0;f<n;f++)
            {
                if(arr2[maxi1]<arr2[f])
                    maxi1=f;
            }
            bool bad=false;
            for(int f=0;f<maxi1;f++)
                if(arr2[f+1]<=arr2[f])
                    bad=1;
            for(int f=maxi1+1;f<n;f++)
                if(arr2[f-1]<=arr2[f])
                    bad=1;
            if(bad)
                continue;
            for(int f=n-1;f>=0;f--)
            {
                long long max2=arr[f];
                int i=0;
                for(;i<f;i++)
                    if(arr2[i]==max2)
                        break;
                for(int f1=i;f1<f;f1++)
                {
                    ans++;
                    swap(arr2[f1],arr2[f1+1]);
                }
            }
            out=min(out,ans);
            for(int f=0;f<n;f++)
                arr2[f]=arr3[f];
        }
        while(next_permutation(arr2,arr2+n));
        cout<<"Case #"<<F<<": "<<out<<endl;
    }
}
