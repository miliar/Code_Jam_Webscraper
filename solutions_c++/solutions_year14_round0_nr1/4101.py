#include <iostream>

void solve()
{
   int a;
   int l[4];
   int ans;
   int ansCount = 0;
   std::cin>>a;
   for (int i = 0; i < 4; ++i)
   {
      for (int j = 0; j < 4; ++j)
      {
         int e;
         std::cin>>e;
         if (i + 1 == a) l[j] = e;
      }
   }
   std::cin>>a;
   for (int i = 0; i < 4; ++i)
   {
      for (int j = 0; j < 4; ++j)
      {
         int e;
         std::cin>>e;
         if (i + 1 == a)
         {
            for (int k = 0; k < 4; ++k)
            {
               if (l[k] == e)
               {
                  ans = e;
                  ansCount++;
               }
            }
         }
      }
   }
   switch (ansCount)
   {
   case 0:
      std::cout<<"Volunteer cheated! "<<std::endl;
      break;
   case 1:
      std::cout<<ans<<std::endl;
      break;
   default:
      std::cout<<"Bad magician!"<<std::endl;
      break;
   }
}

int main()
{
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
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