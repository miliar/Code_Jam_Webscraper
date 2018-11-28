#include <iostream>

void solve()
{
   double c;
   double f;
   double x;
   double ans = 0;
   double s =2;
   std::cin>>c>>f>>x;
   while (true)
   {
      if (x / s < c / s + x / (s + f))
      {
         std::cout<<(ans + x / s) << std::endl;
         break;
      }
      else
      {
         ans += c / s;
         s += f;
      }
   }
}

int main()
{
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
   std::cout.precision(7);
   std::cout.setf(std::ios::fixed);
   int T;
   std::cin>>T;
   for (int i = 1; i <= T; ++i)
   {
      std::cout<<"Case #"<<i<<": ";
      solve();
   }
   fclose(stdin);
   fclose(stdout);
   return 0;
}