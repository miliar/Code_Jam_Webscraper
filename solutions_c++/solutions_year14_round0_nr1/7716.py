#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <fstream>

typedef long long int ll;
ll gcd(ll a, ll b){ if(!b) return a; return gcd(b,a%b);}
using namespace std;

int main()
{ 
    ifstream  in("input.txt");
    ofstream out("output.txt");
    
    int l,t;
    in>>t;
    for(l=1;l<=t;l++)
    {
       int f[5][5];
       int i,j,k;
       int r1,r2;
       int flag=0,ans,dummy;
       
       in>>r1;
       for(i=1;i<=4;i++)
          for(j=1;j<=4;j++)
             in>>f[i][j];
       
       in>>r2;    
       for(i=1;i<=4;i++)
          for(j=1;j<=4;j++)
          {
             in>>dummy;
             for(k=1;k<=4;k++)
               if(i==r2 && dummy==f[r1][k])
               {
                   flag++;
                   ans = dummy;
               }
          }
          
       out<<"Case #"<<l<<": ";
       if(flag>1)
         out<<"Bad magician!";
       else if(flag==0)
         out<<"Volunteer cheated!";
       else
         out<<ans;
       if(l<t)
         out<<endl;
    }
      
return 0;
}
