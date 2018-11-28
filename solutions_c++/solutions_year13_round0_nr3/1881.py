#include <cstdio>
#include <algorithm>
#include <iostream>
#include <vector>
#include <list>
#include <fstream>
#include<string.h>
#define MAX 3050
using namespace std;


int main()
{
      ifstream cin ("C-large-1.in");
      ofstream cout ("output.txt");
      long long  arr[]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};
    
     int t,r=1;
      cin>>t;
      while(t--)
      {
            cout<<"Case #"<<r++<<": ";
            long long a,b;
            cin>>a>>b;
            int st=0,en=0;
            while(arr[st]<a)
            st++;
            while(arr[en]<=b)
            en++;
          //  cout<<st<<"  "<<en<<endl;
         //  cout<<arr[st]<<"  "<<arr[en]<<endl;
            int ans=en-st;
          //  if(b<arr[st])
           // ans--;
            
            cout<<ans<<endl;
            
      }
      
      
      return 0;
}
