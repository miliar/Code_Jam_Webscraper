#include<iostream>
#include<vector>
#include<algorithm>
#include<map>
#include<cassert>
#include<cmath>
#include<sstream>
#define REP(i,s,n) for(int i=s;i<n;i++)
#define rep(i,n) REP(i,0,n)
using namespace std;
typedef vector<int> VI;

int main()
{
  int T;
  cin >> T;
  int Nari = 1;
  while(T-- > 0)
    {
      long long r;
      long long t;
      cin >> r >> t;
      long long cnt = 0;
      long long prev = r*r;
      while(1)
	{

	  r++;
	  long long area = r*r;

	  area -= prev;
	  t -= area;
	  r++;
	  prev = r*r;


	  if(t < 0)break;
	  cnt++;

	}

      cout << "Case #" << Nari++ << ": " << cnt << endl;
    }
  return 0;
}


/*
	  cout << "t = " << t << endl;
	  cout << "prev = " << prev << endl;
	  cout << "are = "<< area << endl;
 */
