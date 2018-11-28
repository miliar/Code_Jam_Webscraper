#include <iostream>
#include <fstream>

using namespace std;

bool a[10];

bool check(long long x)
{
   while(x > 0)
   {
      a[x % 10] = true;
      x /= 10;
   }
   for(int i = 0; i < 10; ++i)
      if(!a[i]) return false;
   return true;
}

int main()
{
   freopen("A-large.in","r",stdin);
   freopen("A-large.out","w",stdout);
   cin.tie(0);
   ios_base::sync_with_stdio(0);
   int T;
   cin>>T;
   for(int t = 1; t <= T; ++t)
   {
      for(int i = 0; i < 10; ++i)
         a[i] = false;
      long long n, x;
      cin>>n; x = n;
      if(n != 0)
      {
         while(!check(x))
            x += n;
         cout<<"Case #"<<t<<": "<<x<<"\n";
      }
      else cout<<"Case #"<<t<<": INSOMNIA\n";
   }
   return 0;
}
