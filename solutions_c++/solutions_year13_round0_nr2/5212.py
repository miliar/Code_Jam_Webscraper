#include <vector>
#include <cstring>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <sstream>
#include <fstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define f(i,a,b) for(int i=a;i<b;i++)
using namespace std;
int main()
{
      ifstream in;
      ofstream out;
      in.open("input.txt");
      out.open("output.txt");
   int te;
   in>>te;
   int cas=1;
   while(te--)
   {
              int n,m;
              in>>n>>m;
              int arr[n][m];
              int chk[n][m];
              
              f(i,0,n)
              f(j,0,m)
              {
              in>>arr[i][j];
              chk[i][j]=0;
              }
              int h[n];
              f(i,0,n)
              {
                      int mx=-1;
              f(j,0,m)
              {
                      if(arr[i][j]>mx) mx=arr[i][j];
              }
              h[i]=mx;
              }
              int v[m];
              f(j,0,m)
              {
                      int mx=-1;
                      f(i,0,n)
                      {
                              if(arr[i][j]>mx) mx=arr[i][j];
                      }
              v[j]=mx;        
              }
             
              int flag=0;
              f(i,0,n)
              f(j,0,m)
              {
                      if((arr[i][j]!=h[i])&&(arr[i][j]!=v[j]))
                      {
                                                              //cout<<h[i]<<v[j];
                                                              //out<<i<<j<<"\n";
                                                              flag=1;
                                                              break;
                      }
              }
              if(flag) out<<"Case #"<<cas<<": "<<"NO\n";
              else out<<"Case #"<<cas<<": "<<"YES\n";
              cas++;


   }
return 0;
}
