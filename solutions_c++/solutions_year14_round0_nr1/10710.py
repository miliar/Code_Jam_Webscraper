#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
   //cout << "Hello World" << endl; 
   int T;
   cin>>T;
   for(int i=0; i<T; i++)
   {
       int r1,r2;
       cin>>r1;
       int garbage;
       int row1 [4];
       int row2 [4];
       for(int j=0;j<4;j++)
       {
           if(j!=r1-1)
           {
               for(int k=0;k<4;k++)
               {
                   cin>>garbage;
               }
           }
           else
           {
               for(int k=0;k<4;k++)
               {
                   cin>>row1[k];
               }
           }
       }
       
       cin>>r2;
       for(int j=0;j<4;j++)
       {
           if(j!=r2-1)
           {
               for(int k=0;k<4;k++)
               {
                   cin>>garbage;
               }
           }
           else
           {
               for(int k=0;k<4;k++)
               {
                   cin>>row2[k];
               }
           }
       }
       
       sort(row1,row1+4);
       sort(row2,row2+4);
       vector<int> v(4);
       vector<int>::iterator it;
       it = set_intersection(row1,row1+4,row2,row2+4,v.begin());
       v.resize(it-v.begin());
       cout<<"Case #"<<i+1<<": ";
       if(v.size()==0)
       {
           cout<<"Volunteer cheated!"<<endl;
       }
       else if(v.size()==1)
       {
           cout<<v[0]<<endl;
       }
       else
       {
           cout<<"Bad magician!"<<endl;
       }
   }
   
   return 0;
}
