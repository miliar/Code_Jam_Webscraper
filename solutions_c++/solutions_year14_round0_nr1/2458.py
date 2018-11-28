#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;
int main()
{
   long long int t,T,row1,row2,inputs;
   vector<long long int> myVector1,myVector2;
   vector<long long int> :: iterator it;
   freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
   cin>>T;
   for(t=1;t<=T;t++)
   {
      myVector1.clear();
      myVector2.clear();
      cin>>row1;
      for(int i=1;i<=4;i++)
         for(int j=1;j<=4;j++)
         {
            cin>>inputs;
            if(i==row1)
               myVector1.push_back(inputs);
         }
      cin>>row2;
      for(int i=1;i<=4;i++)
         for(int j=1;j<=4;j++)
         {
            cin>>inputs;
            if(i==row2)
               myVector2.push_back(inputs);
         }
      int myCount = 0,value;
      for(int i=0; i<myVector1.size();i++)
      {
         it = find (myVector2.begin(), myVector2.end(), myVector1[i]);
         if(it!= myVector2.end())
         {
            myCount++;
            value = *it;
         }
      }
      switch(myCount)
      {
         case 1:  cout<<"Case #"<<t<<": "<<value<<"\n";
                  break;
         case 0:  cout<<"Case #"<<t<<": "<<"Volunteer cheated!"<<"\n";
                  break;
         default: cout<<"Case #"<<t<<": "<<"Bad magician!"<<"\n";
                  break;
      }
   }
   return 0;
}
