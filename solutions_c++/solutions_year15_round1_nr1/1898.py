#include<iostream>
#include<math.h>
#include<stdio.h>
#include<string>
using namespace std;
int print(int a, int b, int x)
{
    cout<<"Case #"<<x<<": "<<a<<" "<<b<<endl;
    return 0;
}
int main()
{
    freopen("out.txt", "w", stdout);
    freopen("in.in", "r", stdin);
    int t, n, arr[10000];
    cin>>t;
    for(int test = 0 ; test < t ; test++)
    {
        int cur, mx = 0, ans=0, ans2 = 0;
        cin>>n;
        for(int i = 0 ; i < n ; i++)
            cin>>arr[i];
        cur = arr[0];
        for(int i = 1 ; i< n ; i++)
        {
            if(arr[i]< arr[i-1])
            {
                ans += arr[i-1] - arr[i];
                mx = max(mx, arr[i-1] - arr[i]);
            }
        }
        for(int i = 0 ; i < n-1 ; i++)
        {
            ans2 += min(mx, arr[i]);
        }
        print(ans, ans2, test+1);
    }
}
