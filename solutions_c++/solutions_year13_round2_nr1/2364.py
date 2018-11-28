#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
  int t;
  cin>>t;
  for (int q=1;q<=t;q++)
  {
    int a,n,z=0,w;
    cin>>a>>n;
    vector<int> v;
    for (int i=0;i<n;i++)
    {
    int u;
      cin>>u;
      v.push_back(u);
      
      }
    sort(v.begin(),v.end());
    cout<<a<<' '<<n<<endl;
    for (int i=0;i<n;i++)
    cout<<v[i]<<' ';
    cout<<endl;
    w=a;
    for (int i=0;i<n;i++)
    {
      if (v[i]<w)
      {
        w+=v[i];
      }
      else 
      {
        int m=n-i;
        int x=0;
        int o=w;
        if (w>1){
        while (v[i]>=w)
        {
          w=w+w-1;
          x++;
        }
        w+=v[i];
        if (x<m)
        {
          z+=x;
        }
        else
        {
          z++;
          w=o;
        }}
        else z++;
      }
    }
    if (z>n)
    cout<<"diu";
    cout<<"Case #"<<q<<": "<<z<<endl;
  }
  return 0;
}
