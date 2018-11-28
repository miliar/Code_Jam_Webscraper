#include <iostream>
#include <algorithm>
#include <functional>

void solve()
{
   double nw[1000];
   double kw[1000];
   unsigned n;
   std::cin>>n;
   for (int i = 0; i < n; ++i)
      std::cin>>nw[i];
   for (int i = 0; i < n; ++i)
      std::cin>>kw[i];
   int j = 0;
   std::sort(nw, nw + n, std::less<double>());
   std::sort(kw, kw + n, std::less<double>());
   unsigned ans1 = 0;
   unsigned ans2 = 0;
   bool kp[1000];
   memset(kp, 0x00, sizeof(kp));

   for (int i = 0 ; i < n; ++i)
   {
      double ns = nw[i];
      double ks = -1;
      for (int j = 0; j < n; ++j)
      {
         if ((kw[j] > ns) && !kp[j])
         {
            kp[j] = true;
            ks = kw[j];
            break;
         }
      }
      if (ks == -1)
      {
         for (int j = 0; j < n; ++j)
         {
            if (!kp[j])
            {
               kp[j] = true;
               ks = kw[j];
               break;
            }
         }
      }
      if (ns > ks) ans2++;
   }

   memset(kp, 0x00, sizeof(kp));
   for (int i = 0; i < n; ++i)
   {
      double ns = nw[i];
      double ks = -1;
      for (int j = 0; j < n; j++)
      {
         if ((kw[j] < ns) && !kp[j])
         {
            kp[j] = true;
            ks = kw[j];
            break;
         }
      }
      if (ks == -1)
      {
         for (int j = n - 1; j >= 0; --j)
         {
            if (!kp[j])
            {
               kp[j] = true;
               ks = kw[j];
               break;
            }
         }
      }
      if (ns > ks) ans1++;
   }

   std::cout<<ans1<<" "<<ans2<<std::endl;
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