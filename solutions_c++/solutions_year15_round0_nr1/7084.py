#include <iostream>
#include <cstdio>
#include <cmath>

#include <string>
#include <vector>
#include <set>
#include <map>

#include <algorithm>

using namespace std;

#define ll long long
#define pb push_back 

#define vT int
#define vit  vector<vT>::iterator 
#define vitr vector<vT>::reverse_iterator 

#define sT int
#define sit  set<sT>::iterator 
#define sitr set<sT>::reverse_iterator 

#define mT1 int
#define mT2 int
#define mit  map<mT1, mT2>::iterator 
#define mitr map<mT1, mT2>::reverse_iterator 

int main()
{
   int N;
   cin >> N;

   int M;
   string ss;
   for(int j=0; j!=N; j++)
   {
      cin >> M;
      cin >> ss;
      /*
      cout << "Case #" << (j+ 1)<< ": " << M;
      cout << " *" << ss << "*" << ss.length() << endl ;
      */

      const int len= ss.length();
      int cum= 0;
      int req= 0;
      int dif= 0;
      if(len>1)
      {
	 for(int k=0; k!=len; k++)
	 {
	    if(cum< req)
	    {
	       dif+= req- cum;
	       cum= req;
	    }
	    int num= ss[k]- '0';
	    cum+= num;

	    req++;
	 }
      }
      cout << "Case #" << (j+ 1)<< ": " << dif << endl;
   }

   return 0;
}
