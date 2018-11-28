#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)

typedef stringstream ss;
typedef pair < int, int >pii;
typedef vector < pii > vpii;
typedef vector < string > vs;
typedef vector < int >vi;
typedef vector < double >vd;
//typedef vector < vector <int>>vii;
typedef long long ll;
typedef long double ld;
typedef pair < int, int >PII;
typedef vector < int >VI;
typedef vector < PII > VPII;
typedef vector < VI > VVI;

int CheckWin (int &sum);

int
main ()
{

  ifstream infile;
  ofstream outfile;

  string inFileName, outFileName;

  cout << "Enter the input file name : ";
  cin >> inFileName;
  cout << "Enter the output file name : ";
  cin >> outFileName;

//  inFileName = "A-small-practice.in";
//  outFileName = "A-small-practice.out";

  infile.open (inFileName.c_str ());
  outfile.open (outFileName.c_str ());

  //error checking
  if (!infile)
    {
      cerr << "File could not be opened." << endl;
      exit (1);
    }

  int t;
  infile >> t;
  REP (tt, t)
  {
    outfile << "Case #" << (tt + 1) << ": ";
    char board[4][4];
    int rowsum[4] = { };
    int columnsum[4] = { };
    int diagonalsum[2] = { };
    bool inprogress (false);
    int winner = 0;

    REP (row, 4) REP (column, 4)
    {

      infile >> board[row][column];
      if (board[row][column] == '.')
	inprogress = true;
      else
	{
	  rowsum[row] += board[row][column];
	  columnsum[column] += board[row][column];
	  if (row == column)
	    diagonalsum[0] += board[row][column];
	  if (row + column == 3)
	    diagonalsum[1] += board[row][column];
	}
    }

    rep (i, 4)
    {

      winner = CheckWin (rowsum[i]);
      if (winner == -1)
	{
	  outfile << "X won" << endl;
	  break;
	}
      else if (winner == 1)
	{
	  outfile << "O won" << endl;
	  break;
	}

      winner = CheckWin (columnsum[i]);
      if (winner == -1)
	{
	  outfile << "X won" << endl;
	  break;
	}
      else if (winner == 1)
	{
	  outfile << "O won" << endl;
	  break;
	}

      if (i < 2)
	{
	  winner = CheckWin (diagonalsum[i]);
	  if (winner == -1)
	    {
	      outfile << "X won" << endl;
	      break;
	    }
	  else if (winner == 1)
	    {
	      outfile << "O won" << endl;
	      break;
	    }


	}

    }



    if (!winner)
      if (inprogress)
	outfile << "Game has not completed" << endl;
      else
	outfile << "Draw" << endl;
  }
  infile.close ();
  outfile.close ();
  return 0;
}

int
CheckWin (int &sum)
{

//bool winner
  switch (sum)
    {
    case 348:			//XXXT
    case 352:			//XXXX
//        outfile << "X won";
      return -1;		//X won
      break;
    case 321:			//OOOT
    case 316:			//OOOO
//        outfile << "O won";
      return 1;			//O won
      break;
    default:
//        outfile << "value of x unknown";
      return -0;		//none won
    }

}
