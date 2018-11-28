#include <bits/stdc++.h>
using namespace std;

int arr[1005];

int main()
{
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int t;
  cin>>t;
  for(int i = 1; i <= t; i++)
  {
    int n;
    cin>>n;
    for(int i = 0; i < n; i++)
    {
      cin>>arr[i];
    }

    //case1
    int ans1 = 0;
    for(int i = 1; i < n; i++)
    {
      if(arr[i] < arr[i-1])
        ans1 += (arr[i-1] - arr[i]);
    }

    //case 2
    int ans2 = 0;
    int mx = 0,carry;
    for(int i = 1; i < n; i++)
    {
      int diff = arr[i - 1] - arr[i];
      mx = max(mx,diff);
    }

    for(int i = 0; i < n - 1; i++)
    {
      if(arr[i] <= mx)
        ans2 += arr[i];
      else
      {
        ans2 += mx;
      }

    }
    cout<<"Case #"<<i<<": "<<ans1<<" "<<ans2<<endl;
  }
  return 0;
}   