#define _CRT_SECURE_NO_WARNINGS
#include<bits/stdc++.h>
main()
{
  freopen("c.in", "r", stdin);
   freopen("c.out", "w", stdout);
   int t;
  register long double c,f,x,m=1,s,k,i;
   std::cin>>t;
   while(t--)
   {
       i=0;
      std::cin>>c;
       std::cin>>f;
       std::cin>>x;
       s=x/2;
       k=s;
       while((s+(c/(2+(i*f))+(x/(2+((i+1)*f)))-(x/(2+(i*f)))))<k)
       {
           s+=(c/(2+(i*f)))+(x/(2+((i+1)*f)))-(x/(2+(i*f)));
           k=s;
           i++;
       }
       std::cout<<"Case #"<<m++<<": " ;
  std::cout << std::setprecision(13) << s << '\n';
   }
   }
