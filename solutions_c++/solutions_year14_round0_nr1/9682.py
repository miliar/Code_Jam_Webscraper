#include<iostream>
#include<vector>
#include<fstream>
using namespace std;
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
int main()
{
    //READ("A-small-attempt0.in");
    //WRITE("A-small-attempt0.out");
    int t;
    cin>>t;
   for(int T=1;T<=t;T++)
   {
        int arr[4][4];int x,i,j,count,y;
        int arr2[4][4];
        vector<int>first;
        vector<int>second;
        cin>>x;
   for(i=0;i<4;i++)
   {
       for(j=0;j<4;j++)
       {
           cin>>arr[i][j];
           if(i==(x-1))
           {
               first.push_back(arr[i][j]);
           }
       }
   }
   cin>>x;
   for(i=0;i<4;i++)
   {
       for(j=0;j<4;j++)
       {
           cin>>arr2[i][j];
           if(i==(x-1))
           {
               second.push_back(arr2[i][j]);
           }
       }
   }
   count=0;
   for(i=0;i<4;i++)
   {
       for(j=0;j<4;j++)
       {
           if(first[i]==second[j])
           {
               y=first[i];
               count++;
           }
       }
   }
   if(count>1)
   {
       cout<<"Case #"<<T<<": Bad magician!"<<endl;
   }
   else if(count==0)
    cout<<"Case #"<<T<<": Volunteer cheated!"<<endl;
   else if(count==1)
   {
       cout<<"Case #"<<T<<": "<<y<<endl;
   }
}
}
