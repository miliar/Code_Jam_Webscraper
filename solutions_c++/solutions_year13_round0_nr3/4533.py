#include<iostream>
#include<cstring>
#include<cstdio>
#include<vector>
#include<fstream>
using namespace std;
main()
{
      int t,a,b,ans;
      ifstream in;
      ofstream out;
      in.open("input.txt");
      out.open("output.txt");
      in>>t;
      int arr[6]={0,1,4,9,121,484};
      for(int i=0;i<t;i++)
      {
              in>>a>>b;
              cout<<a<<b<<"\n";
              ans=0;
              for(int j=0;j<6;j++)
              if(arr[j]<=b && arr[j]>=a)
              {ans++;cout<<arr[j]<<"\n";}
              out<<"Case #"<<i+1<<": "<<ans<<"\n";
     }




          system("pause");
      }
