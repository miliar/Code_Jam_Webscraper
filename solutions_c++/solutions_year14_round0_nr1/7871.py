#include <vector>
#include <map>
#include <set>
#include <stack>
#include <string>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <queue>
#include <fstream>
using namespace std;

int main()
{
    ifstream fin("A-small-attempt0.in");
    ofstream fout("output1.txt");
    # define cin fin
    # define cout fout
    int i,j,a,b,t,k,match=0,ans;
    int m[4][4],n[4][4];
     cin>>t;
     for(k=1;k<=t;k++)
     {
         cin>>a;
         for(i=0;i<4;i++)
         {
         for(j=0;j<4;j++)
         {
          cin>>m[i][j];
          }
         }
         cin>>b;
         for(i=0;i<4;i++)
         {
         for(j=0;j<4;j++)
         {
          cin>>n[i][j];
          }
         }
         for(i=0;i<4;i++)
         {
         for(j=0;j<4;j++)
         {
          if(m[a-1][i] == n[b-1][j] )
           {
            match++;
            ans=m[a-1][i];
           }               
         }
         }
         if(match==0)
         cout<<"Case #"<<k<<": "<<"Volunteer cheated!\n";
         else
         if(match==1)
         cout<<"Case #"<<k<<": "<<ans<<'\n';
         else
         cout<<"Case #"<<k<<": "<<"Bad magician!\n";
         match=0;
     }
     return 0;
}
