#include <iostream>
#include<stdio.h>
#include<algorithm>

using namespace std;

#define gi(n) scanf("%d",&n)

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("ousadjvhkj_large.txt", "w", stdout);
    int cases;
    gi(cases);
    int t = 1;
    while(cases--)
    {
        int n;
        cin>>n;
        int arr[n];
        for(int i=0; i<n; i++)
        {
            gi(arr[i]);
        }
        int ans=0;
        int ans1=0;
        int m = 0;
        for(int i=1; i<n; i++)
        {
            if(arr[i]-arr[i-1]<0)
            {
                ans += (arr[i-1]-arr[i]);
            }
            m = max(m, arr[i-1]-arr[i]);
        }

        //int m = *max_element(arr,arr+n);

        for(int i=0; i<n-1; i++)
        {
            if(arr[i]<m)
            ans1 += arr[i];
            else ans1 += m;
        }
        cout<<"Case #"<<t++<<": "<<ans<<" "<<ans1<<endl;
    }
    return 0;
}

