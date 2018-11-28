#include <bits/stdc++.h>
using namespace std;

int main()
{
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int t;
  cin>>t;
  for(int i = 1; i <= t; i++)
  {
    vector<int> arr;
    int n;
    cin>>n;
    arr.resize(n);
    for(int j = 0; j < n; j++)
    {
      int temp;
      cin>>temp;
      arr[j] = temp;
    }

    sort(arr.begin(), arr.end());
    int mn = 1000000000;
    for(int j = 1; j <= arr[n-1]; j++)
    {
      int ans = j;
      for(int k = 0; k < n; k++)
      {
        if(arr[k] % j == 0)
          ans += (arr[k] / j) - 1;
        else
          ans += (arr[k] / j);
      }

      if(ans < mn)
        mn = ans;
    }

    cout<<"Case #"<<i<<": "<<mn<<endl;
  }
  return 0;
}  