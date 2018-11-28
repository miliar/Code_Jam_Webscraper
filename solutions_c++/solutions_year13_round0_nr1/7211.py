#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <utility>
#include <vector>
#include <iostream>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <cctype>
#include <sstream>
#include <cassert>
#include <bitset>
#include <memory.h>
#include <complex>

using namespace std;

#pragma comment(linker, "/STACK:200000000")

typedef long long int64;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define fore(i, a, n) for(int i = (int)(a); i < (int)(n); i++)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) (int(a.size()) - 1)
#define all(a) a.begin(), a.end()

const double EPS = 1E-9;
const int INF = 1000000000;
const int64 INF64 = (int64) 1E18;
const double PI = 3.1415926535897932384626433832795;

int main() {
  freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);
  int t, i, j, n;
  cin>>t;
  char inp[5][6], temp[4];
  cin.getline(temp, 4);
  for(n = 1; n <= t; n++)
    {
      // flags and counts
      int notcomp = 0;
      int rowX[4] = {0}, colX[4] = {0}, rowO[4] = {0}, colO[4] = {0}, diagX = 0, diagO = 0, rdiagX = 0, rdiagO = 0;
      cin.getline(inp[0], 5); //cout<<"Got first one: "<<inp[0]<<endl;
      cin.getline(inp[1], 5); //cout<<"Got second one: "<<inp[1]<<endl;
      cin.getline(inp[2], 5); //cout<<"Got third one: "<<inp[2]<<endl;
      cin.getline(inp[3], 5); //cout<<"Got the last one: "<<inp[3]<<endl;
      cin.getline(temp, 4); //cout<<"Just read empty line!\n";
      for(i = 0; i < 4; i++)
	{
	  for(j = 0; j < 4; j++)
	    {
	      if(inp[i][j] == '.')
		notcomp = 1;
	      else if(inp[i][j] == 'T')
		{
		  rowX[i]++; rowO[i]++;  colX[j]++; colO[j]++;
		  if(i == j)
		    {
		      diagX++; diagO++;
		    }
		  else if( i + j == 3)
		    {
		      rdiagX++; rdiagO++;
		    }
		}
	      else if(inp[i][j] == 'O')
		{
		  rowO[i]++; colO[j]++;
		  if(i == j)
		    diagO++;
		  else if( i + j == 3)
		    rdiagO++;
		}
	      else
		{
		  rowX[i]++; colX[j]++;
		  if(i == j)
		    diagX++;
		  else if( i + j == 3)
		    rdiagX++;
		}

	    }
	}
	  cout<<"Case #"<<n<<": ";
	  if((rowX[0] == 4 )||(rowX[1] == 4 )||(rowX[2] == 4 )||(rowX[3] == 4 ) || (colX[0] == 4)|| (colX[1] == 4)|| (colX[2] == 4)|| (colX[3] == 4) || (diagX == 4) || (rdiagX == 4))
	    cout<<"X won";
	  else if((rowO[0] == 4 )||(rowO[1] == 4 )||(rowO[2] == 4 )||(rowO[3] == 4 ) || (colO[0] == 4)|| (colO[1] == 4)|| (colO[2] == 4)|| (colO[3] == 4) || (diagO == 4) || (rdiagO == 4))
	    cout<<"O won";
	  else if(notcomp == 1)
	    cout<<"Game has not completed";
	  else
	    cout<<"Draw";
	  cout<<endl;      
    }
  return 0;
}
