#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;
int main()
{
   freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
   vector<double> myVector1,myVector2;
   long long int n,t,T,k;
   double d;
   cin>>T;
   for(t=1;t<=T;t++)
   {
      myVector1.clear();
      myVector2.clear();
      cin>>n;
      for(int i=1;i<=n;i++)
      {
         cin>>d;
         myVector1.push_back(d);
      }
      for(int i=1;i<=n;i++)
      {
         cin>>d;
         myVector2.push_back(d);
      }
      sort(myVector1.begin(),myVector1.end());
      sort(myVector2.begin(),myVector2.end());
//
//      for(long long int i=0;i<n;i++)
//         cout<<myVector1[i]<<" ";
//      cout<<"\n";
//      for(long long int i=0;i<n;i++)
//         cout<<myVector2[i]<<" ";


      long long int countWar=0;
      for(long long int i=0,k=0;i<n && k<n;i++)
      {
         while(1)
         {
            if(k>=n)
               break;
            if(myVector1[i]<myVector2[k])
            {
               countWar++;
               k++;
               break;
            }
            else
               k++;
         }
      }
      countWar = n-countWar;
      //
      long long int countDWar=0;
      for(long long int i=0,k=0;i<n && k<n;i++)
      {
         while(1)
         {
            if(k>=n)
               break;
            if(myVector2[i]<myVector1[k])
            {
               countDWar++;
               k++;
               break;
            }
            else
               k++;
         }
      }
      countDWar = countDWar;
      cout<<"Case #"<<t<<": "<<countDWar<<" "<<countWar<<"\n";
   }
   return 0;
}
