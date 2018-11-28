#include <bits/stdc++.h>
using namespace std;
#define endl "\n"
#define l long 
#define ll long long
#define f(a,b,c) for(a=b;a<c;a++)
#define pi 3.1415929203539825

ll x_pow_y_modm(ll x, ll y, ll m){
    if(y==0)
        return 1;
    ll temp;
    temp = x_pow_y_modm(x,y/2,m);
    if(y%2==0)
        return (temp*temp)%m;
    else
        return (x*((temp*temp)%m))%m;
}
 
ll modularInverse(ll a, ll m) {
    return x_pow_y_modm(a,m-2,m);
}
 
ll gcd(ll a,ll b)
{
  if(a==0)
    return b;
  if(b==0)
    return a;
  return gcd(b,a%b);
}
 
// function to get index of smallest number just greater than the given number----------------
// ll binarySearch( vector<ll>& arr, ll t)
// {
//   ll n=arr.size();
//   ll i=0,j=n-1;
//     while(i<=j)
//     {
//         if(t < arr[mid])
//           j=mid-1;
//         else
//           i=mid+1;
//     }
//     return i;
// }
//--------------------------------------------------------------------------------------------
 
// ll isPowerOfTwo (unsigned ll x)
// {
//   return ((x != 0) && ((x & (~x + 1)) == x));
// }
 
// /* This function calculates (a^b)%MOD */
// ll power(l a, l b, l MOD) {
// ll x = 1, y = a;
//     while(b > 0) {
//         if(b%2 == 1) {
//             x=(x*y);
//             if(x>MOD) x%=MOD;
//         }
//         y = (y*y);
//         if(y>MOD) y%=MOD;
//         b /= 2;
//     }
//     return x;
// }
 
// ll modInverse(l a, l m) {
//     return power(a,m-2,m);
// }
 
ll min(l x,l y, l z)
{
  return min(x,min(y,z));
}

int main(){
  ll i,j;
  ios_base :: sync_with_stdio(0);
  cin.tie(NULL);
  cout.tie(NULL);
  ll t,n,x,y;
  bool fre[10],flag;
  cin>>t;
  ll test=1;
  while(t--)
  {
    cout<<"Case #"<<test<<": ";
    test++;
    cin>>n;
    if(n == 0)
    {
      cout<<"INSOMNIA"<<endl;
      continue;
    }
    memset(fre,0,sizeof(fre));
    y=n;
    x=y;
    while(x>0)
    {
      fre[x%10]=1;
      x/=10;
    }
    // cout<<y<<" ";
    j=2;
    while(1)
    {
      y = j*n;
      j++;
      // cout<<y<<" ";
      x=y;
      while(x>0)
      {
        fre[x%10]=1;
        x/=10;
      }
      flag=0;
      f(i,0,10)
      {
        if(fre[i]==0)
        {
          flag=1;
          break;
        }
      }
      if(!flag)
        break;
    }
    cout<<y<<endl;
  }  
  return 0;
}




