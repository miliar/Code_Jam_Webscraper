
/**
 * Michael V. Antosha   (mivael)
 *
 * Michael.Antosha@gmail.com
 *
 * April 2013
 */

#include <iostream>
using std::clog;
using std::endl;
using std::flush;
using std::istream;

#include <string>
using std::string;

#include <vector>
using std::vector;

#include <cassert>

const int MIN_NUMBER_OF_CASES = 1;
const int MAX_NUMBER_OF_CASES = 100;

const int MIN_LAWN_SIZE = 1;

const int MIN_HEIGHT = 1;

#ifdef SMALL_DATASET
const int MAX_LAWN_SIZE = 10;
const int MAX_HEIGHT = 2;
#endif
//
#ifdef LARGE_DATASET
const int MAX_LAWN_SIZE = 100;
const int MAX_HEIGHT = 100;
#endif

int matr[MAX_LAWN_SIZE][MAX_LAWN_SIZE];

static bool ensure_eol(istream& in)
{
  assert(in.good());
  string str;
  getline(in, str);
  assert(in.good());
  // clog << "ensure_eol: remainder='" << str << "'" << endl;
  assert(str.empty());
  return true;
}

static int read_next_integer(istream& in)
{
  assert(in.good());
  int num;
  in >> num;
  assert(in.good());
  return num;
}

static int read_last_integer(istream& in)
{
  int num = read_next_integer(in);
  ensure_eol(in);
  return num;
}

static int read_tc_number(istream& in)
{
  int tc = read_last_integer(in);
  assert(MIN_NUMBER_OF_CASES <= tc  &&  tc <= MAX_NUMBER_OF_CASES);
  return tc;
}

static int read_N(istream& in)
{
  int sz = read_next_integer(in);
  assert(MIN_LAWN_SIZE <= sz  &&  sz <= MAX_LAWN_SIZE);
  return sz;
}

static int read_M(istream& in)
{
  int sz = read_last_integer(in);
  assert(MIN_LAWN_SIZE <= sz  &&  sz <= MAX_LAWN_SIZE);
  return sz;
}

static int read_height_value(istream& in)
{
  int h = read_next_integer(in);
  assert(MIN_HEIGHT <= h  &&  h <= MAX_HEIGHT);
  return h;
}

int main(void)
{
  using std::cin;
  using std::cout;

  clog << "Hello." << endl;

  const int T = read_tc_number(cin);

  for (int tc = 1;  tc <= T;  ++tc)
    {
      clog << "Test case #" << tc << "..." << endl;

      const int N = read_N(cin);  // number of lines of input
      const int M = read_M(cin);  // number of nums in each line

      // read the matrix and count maximum values for each row and col
      vector<int> rowmax(N);  // maximum value in each row
      vector<int> colmax(M);  // maximum value in each row
      for (int rind = 0;  rind < N;  ++rind)  // row index (input lines iterated)
	{
	  int row_max = -1;  assert(MIN_HEIGHT > 0);

	  for (int cind = 0;  cind < M;  ++cind)  // column index
	    {
	      int h = read_height_value(cin);
	      matr[rind][cind] = h;

	      if (h > row_max)  row_max = h;
	      if (h > colmax[cind])  colmax[cind] = h;
	    }

	  rowmax[rind] = row_max;

	  ensure_eol(cin);
	}

      // iterate through each cell looking for impossible
      // configuration
      bool okay = true;
      for (int y = 0;  y < N  &&  okay;  ++y)
	for (int x = 0;  x < M;  x++)
	  {
	    const int& h = matr[y][x];
	    if (h < rowmax[y]  &&  h < colmax[x])
	      { okay = false;  break; }
	  }

      cout << "Case #" << tc << ": "
	   << (okay ? "YES" : "NO") << endl;
    }

  return 0;
}
