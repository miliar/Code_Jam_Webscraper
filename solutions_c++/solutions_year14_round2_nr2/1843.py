#include <iostream>

using namespace std;

int main()
{
  int a, b, k;
  int t;
  int c = 1;
  ios_base::sync_with_stdio(false);
  cin>>t;
  while(t--)
  {
    int count = 0;
    cin>>a>>b>>k;
    for(int i = 0; i < a; i++)
      for(int j = 0; j < b; j++)
      {
        if((i&j) < k)
          count++;
      }
    cout<<"Case #"<<c++<<": "<<count<<"\n";
  }
  return 0;  
}
