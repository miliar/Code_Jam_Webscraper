//BIG-OH
//prob-
//Algo-
//complexity-
#include<cstdio>
#include<iostream>
#include<cstring>
#include<sstream>
#include<stdlib.h>
#include<algorithm>
#include<cmath>
#include<vector>
#include<map>
#include<set>
#include<list>
#include<stack>
#include<queue>
#include<iomanip>
#include<ctype.h>
#include<complex>
#include<utility>
#include<functional>
#include<bitset>
#include<numeric>
#include<cassert>
#include<climits>
 
using namespace std;
#define ll long long 
#define gc getchar_unlocked
#define mod 1000000009
#define pq priority_queue
#define vi vector<int>
#define eps 1e-9
#define inf (1 << 28)
#define  MX 1111
int main()
{
  int test;
  cin>>test;
  int X,R,C;
  for (int z=1;z<=test;z++)
 {
   cin>>X>>R>>C;
   cout << "Case #" <<z<<": ";
   if(X==1) cout<<"GABRIEL\n";
   else if(X==2)
   {
      if((R*C)%2==0) cout<<"GABRIEL\n";
      else  cout<<"RICHARD\n";
   }
   else if(X==3)
   {
     if(R==3||C==3)
     {
        if(R==1 ||C==1)  cout<<"RICHARD\n";
        else  cout<<"GABRIEL\n";
     }
     else cout<<"RICHARD\n";
   }
   else if(X==4)
   {
     if(R==4 && C==4) cout<<"GABRIEL\n";
     else if((R==4 && C==3) ||(R==3 && C==4))
          cout<<"GABRIEL\n";
     else
      cout<<"RICHARD\n";
   }
  }
  return 0;
}
