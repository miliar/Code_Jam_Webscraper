#include<bits/stdc++.h>
#define ll long long 
using namespace std;
int arr[10];
bool func( int val )
{
  while( val )
  {
    arr[ val % 10 ]++;
    val /= 10;
  }
  for( int i = 0 ; i < 10 ; i++ )
  {
    if( not arr[i] )
      return false;
  }
  return true;
}
int res[1000005];
int main()
{
  ios::sync_with_stdio(false);
  res[0] = -1;
  res[1] = 10;
  for( ll i = 2 ; i < 1000005 ; i++ )
  {
    memset( arr , 0 , sizeof(arr) );
    ll ans = i;
    while( not func(ans) )
      ans += i;
    res[i] = ans;
  }
  int t;
  cin >> t;
  for( int test = 1 ; test <= t ; test++ )
  {
    int n;
    cin >> n;
    if( not n )
      cout<<"Case #"<< test <<": INSOMNIA"<<endl;
    else
      cout<<"Case #"<<test <<": "<< res[n] <<endl;
  }
}
   

  
