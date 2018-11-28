#include <bits/stdc++.h>

using namespace std;

int t;
int n,numa,j,i;
long long num;
vector < long long > all;

long long prime(long long x)
 {
  for (long long i=2;i*i<=x;i++)
    if (x%i == 0) return i;
  return 0;
 }


int main()
 {
 freopen("in.in","r",stdin);
 freopen("3.out","w",stdout);
  cin>>t;
  for (int tt=1;tt<=t;tt++)
   {
    cout<<"Case #"<<tt<<":"<<endl;
    cin>>n>>numa;
    for (j=0;j<(1<<n);j++)
     {
      if (!(j&1)) continue;
      if (!(j&(1<<(n-1)))) continue;

      bool can=1;
      all.clear();

      for (int base=2;base<=10;base++)
      {
        num=0;

       for (i=0;i<n;i++)
        num=num*base+(((1<<i)&j)?(1):(0));

         all.push_back(prime(num));
        if (!all.back()) { can=0; break; }
       }
      if (!can) continue;
      numa--;
      cout<<num;
      for (i=0;i<all.size();i++)
        cout<<" "<<all[i];
      cout<<endl;
      if (!numa) break;
     }
   }
 }
