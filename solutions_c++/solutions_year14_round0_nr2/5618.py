#include <fstream>
#include <iostream>
#include <iomanip>
#include <map>
#include <sstream>
#include <string>
#include <vector>

using std::cout;
using std::endl;
using std::fstream;
using std::map;
using std::stringstream;
using std::string;
using std::vector;

double
get_minmum_time(const double _c, const double _f, const double _x);
// @_n: from 0
double
get_n_time(const double _c, const double _f, const int _n);

int main(int argc, char *argv[])
{
  fstream fs("input.txt", fstream::in);
  fstream fout("output.txt", fstream::out);

  if (fs.good())
  {
    int case_amount = 0;
    string line = "";

    getline(fs, line);
    stringstream stream(line);
    stream >> case_amount;
    
    for (int i = 0; i < case_amount; ++i)
    {
      string line = "";
      getline(fs, line);
      stringstream stream(line);
      double c, f, x;
      stream >> c;
      stream >> f;
      stream >> x;
      
      double result = get_minmum_time(c, f, x);
      
      fout << "Case #" << 1 + i << ": "
           << std::fixed
           << std::setprecision(7)
           << result
           << endl;
    }
  }

  fs.close();
  fout.close();
  
  return 0;
}

double
get_minmum_time(const double _c, const double _f, const double _x)
{
  double t_max = _x / 2;
  double t_min = t_max;
  double t = 0;
  int i = 0;
  
  if (0 == _c || 0 == _x)
  {
    return 0;
  }
  else if (0 == _f)
  {
    return t_max;
  }

  double pre_t = t_max;
  while (t <= t_max)
  {
    t = get_n_time(_c, _f, i);
    t += _x / (2 + i * _f);
    
    if (t < t_min)
    {
      t_min = t;
    }
    ++i;

    if (pre_t < t)
    {
      break;
    }

    pre_t = t;
  }
  
  return t_min;
}

// @_n: from 0
double
get_n_time(const double _c, const double _f, const int _n)
{
  double time = 0;
  double speed = 2;

  for (int i = 0; i < _n; ++i)
  {
    time += _c / speed;
    speed += _f;
  }

  return time;
}
