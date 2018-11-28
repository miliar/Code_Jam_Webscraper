#include <iostream>
#include <cstdio>
#include <cmath>

#include <vector>
#include <set>
#include <map>

#include <algorithm>

using namespace std;

#define ll long long
#define pb push_back 

int read(const int num, const int r, vector<int>& v)
{
   v.clear();
   int tem;
   
   for(int j=0; j!=num; j++)
   {
      for(int k=0; k!=num; k++)
      {
	 cin >> tem;
	 if( r == j) v.pb(tem);
      }
   }

   return 1;
}

int main()
{
   int N;
   cin >> N;

   const string strBad= "Bad magician!";
   const string strChe= "Volunteer cheated!";

   const int num= 4;
   for(int j=0; j!=N; j++)
   {
      vector<int> v1, v2;
      int r;
      cin >> r; r--; read(num, r, v1);
      cin >> r; r--; read(num, r, v2);

      int fnd= 0;
      int ret= 0;
      for(int k=0; k!=v1.size(); k++)
      {
	 int tem= find(v2.begin(), v2.end(), v1[k]) != v2.end();
	 fnd+= tem;
	 if(tem) ret= *(find(v2.begin(), v2.end(), v1[k]));
      }

      cout << "Case #" << (j+ 1)<< ": ";
      if(fnd == 1)     cout << ret;
      else if(fnd > 1) cout << strBad;
      else             cout << strChe;
      cout << endl;
   }

   return 0;
}
