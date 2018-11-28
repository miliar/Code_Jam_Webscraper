#include <iostream>
#include <fstream>
#include <stdlib.h>
int main()
{
     long int a,b,c,n=0,d[100],sum;
     char ch[10];
      std ::ifstream fp1;
     fp1.open("ip");
     fp1>>a;
    // std ::cout<<"a"<<a;
     int i,j=1;
     std ::ofstream fp;
     fp.open("op");

     while(a!=0)
     {

      //  std ::cout<<"smax";

         fp1>>b;
         std ::cout<<"\nb"<<b<<"\n";
          n=0;
          sum = 0;
         for(i=0;i<=b;++i)
         {
            fp1>>ch[0];

            c = atoi(ch);
             std ::cout<<c<<" c\n";
            if(sum < i)
            {

                 ++n;
                 ++sum;


              //  std::cout<<"\nc"<<c;

                //std::cout<<"\nn"<<n;
            }
            sum = sum + c;

         }
        std::cout<<"no is: "<<n<<"\n";
         fp<<"Case #"<<j<<": "<<n<<"\n";
         ++j;
          d[a+1] = n;
          n=0;
      --a;
     }
     fp1.close();
  /*     std ::ofstream fp;
     fp.open("op");
      for(i=1;i<=j;++i)
      {

          std::cout<<"Case #"<<i<<": "<<d[i+1]<<"\n";
           fp<<"Case #"<<i<<": "<<d[i+1]<<"\n";
      }*/
    fp.close();
}
