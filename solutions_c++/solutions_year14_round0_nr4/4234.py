#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;
#define ll long long
#define pb push_back 

#include <vector>
#include <algorithm>
double myFun(double d1, double d2)
{
   return ( -(d1- d2) );
}

int readVec(vector<double>& v, const int n)
{
   double tem;
   for(int j=0; j!=n; j++)
   {
      cin >> tem;
      v.pb(tem);
   }
   return 1;
}


int getWWW(vector<double> v1, vector<double> v2)
{
   int ret= 0;
   while(!v1.empty() && !v2.empty())
   {
      if(v1.back() < v2.back())
      {
	 v1.pop_back();
	 v2.erase(v2.begin());
      }
      else
      {
	 v1.pop_back();
	 v2.pop_back();
	 ret++;
      }
   }
   return ret;
}


int getWar(vector<double> v1, vector<double> v2)
{
   int ret= 0;
   while(!v1.empty() && !v2.empty())
   {
      if(v1[0] > v2[0])
      {
	 v1.erase(v1.begin());
	 v2.pop_back();
	 ret++;
      }
      else
      {
	 v1.erase(v1.begin());
	 v2.erase(v2.begin());
      }
   }
   return ret;
}

int main()
{
   int T;
   cin >> T;

   for(int j=0; j!=T; j++)
   {
      int N;
      cin >> N;
      vector<double> v1, v2;
      readVec(v1, N);
      readVec(v2, N);

      sort(v1.begin(), v1.end()); reverse(v1.begin(), v1.end());
      sort(v2.begin(), v2.end()); reverse(v2.begin(), v2.end());

      cout << v1.size() << " " << v2.size() << endl; 
      for(int k=0; k!=N; k++)
   // cout << v1[k] << "  " << v2[k] << endl;
      printf("%8.3f %8.3f\n", v1[k], v2[k]);

      int retWWW= getWWW(v1, v2);
      int retWar= getWar(v1, v2);
      cout << "Case #" << (j+ 1)<< ": " << retWWW << " " << retWar;
      cout << endl;
   }

   return 0;
}
