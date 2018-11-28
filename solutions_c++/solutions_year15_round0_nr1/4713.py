#include <iostream>
#include <stdio.h>
#include <string>
#include <stdlib.h>
using namespace std;
int main()
{
  freopen("A-large.in","r",stdin);
  freopen("A-large.out","w",stdout);
  int T;
  cin>>T;
  for(int t=1; t<=T; t++)
  {
      int n,total = 0,pre = 0;
      int o;
      cin>>n;
      string str ;
      cin >> str ;
      for(int i=0; i<n; i++)
      {
       		pre = pre+ str[i] - 48 ;
          while( (pre + total ) <= i) {
          	total++;
          }
      }
      
      cout<<"Case #"<<t<<": "<< total<<endl;
      
   }
}