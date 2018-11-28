#include<iostream>
#include<bitset>

using namespace std;

#define ll long long

bitset<10> arr;
ll diff;

ll func(ll a)
{
  ll b = a;      
  while(a)
  {
    int d = a%10;
    a /= 10;
    arr[d] = 1;
  }
  string hardSet =  "1111111111";
  if(hardSet.compare(arr.to_string()) == 0)
  {    
    return b;
  }
  else
  {
    return func(b+diff);
  }  
}

int main()
{
  int t;
  cin>>t;
  int icase =1;
  while(t--)
  {
    ll n ;    
    cin>>n;
    cout<<"Case #"<<icase++<<": ";
    if(n == 0)
    {
      cout<<"INSOMNIA"<<endl;
      continue;      
    }
    arr =  bitset<10>();    
    diff = n;
    cout<<func(n)<<endl;    
  }
  
}