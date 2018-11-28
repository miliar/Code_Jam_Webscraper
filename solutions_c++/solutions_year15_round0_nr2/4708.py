//BIG-OH
//prob-
//Algo-
//complexity-
#include<cstdio>
#include<iostream>
#include<cstring>
#include<sstream>
#include<stdlib.h>
#include<algorithm>
#include<cmath>
#include<vector>
#include<map>
#include<set>
#include<list>
#include<stack>
#include<queue>
#include<iomanip>
#include<ctype.h>
#include<complex>
#include<utility>
#include<functional>
#include<bitset>
#include<numeric>
#include<cassert>
#include<climits>
 
using namespace std;
#define ll long long 
#define gc getchar_unlocked
#define mod 1000000009
#define pq priority_queue
#define vi vector<int>
#define eps 1e-9
#define inf (1 << 28)
#define  MX 1111
int arr[MX];
int main()
{
  int test;
  cin>>test;
  for(int z=1;z<=test;z++)
  {
     int max_x=0,n;
    int D;
    cin>>D;
    int mx=0;
    for(int i=1;i<=D;i++)
    {
      cin>>arr[i];
      if(arr[i]>mx) mx=arr[i];
    }
    int val=mx;
    for(int i=1;i<=mx;i++)
    {
      int p=0,q=0;
      for(int j=1;j<=D;j++)
      {
	 if(arr[j]>i)
	 {
	   p+=(arr[j]/i)+((arr[j]%i==0)?0:1)-1;
	   q=max(q,i);
	 }
	 else q=max(q,arr[j]);
      }
      p+=q;
      if(p<val)val=p;
    }
    cout<<"Case #"<<z<<": "<<val<<endl;
  }
  return 0;
}

