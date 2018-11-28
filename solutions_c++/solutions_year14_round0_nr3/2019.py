#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using std::cout;
using std::endl;
using std::fstream;
using std::stringstream;
using std::string;
using std::vector;

struct Point
{
  int x;
  int y;
  Point(const int _x, const int _y)
  {
    x = _x;
    y = _y;
  }
};

vector<vector<char> >
get_result(const int _r, const int _c, const int _m);

vector<vector<char> >
recuresive_run(vector<vector<char> > _record,
               int _index,
               vector<Point> _wait_vec,
               int _amount_of_unrevealed,
               const int _amount_of_not_mines);

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
      getline(fs, line);      
      stringstream stream(line);

      int r, c, m;
      stream >> r
             >> c
             >> m;

      vector<vector<char> > result = get_result(r, c, m);

      
      fout << "Case #" << 1 + i << ": " << endl;

      if (0 != result.size())
      {
        result[1][1] = 'c';

        for (int j = 0; j < result.size(); ++j)
        {
          std::replace(result[j].begin(), result[j].end(), '1', '.');
          std::replace(result[j].begin(), result[j].end(), '0', '.');
        }
        
        for (int j = 1; j < result.size() - 1; ++j)
        {
          for (int k = 1; k < result[j].size() - 1; ++k)
          {
            fout << result[j][k];
          }
          fout << endl;
        }
      }
      else
      {
        fout << "Impossible" << endl;
      }
    }
  }

  fs.close();
  fout.close();
  
  return 0;
}

vector<vector<char> >
get_result(const int _r, const int _c, const int _m)
{
  vector<vector<char> > record(2 + _r, vector<char>(2 + _c, '*'));

  std::fill(record[0].begin(), record[0].end(), '#');
  std::fill(record.back().begin(), record.back().end(), '#');

  for (int i = 0; i < 2 + _r; ++i)
  {
    record[i][0] = '#';
    record[i].back() = '#';
  }

  const int amount_of_not_mines = _r * _c - _m;

  vector<Point> wait_vec;
  record[1][1] = '0';
  wait_vec.push_back(Point(1, 1));
    
  record = recuresive_run(record,
                          0,
                          wait_vec,
                          1,
                          _r * _c - _m);
  return record;
}

vector<vector<char> >
recuresive_run(vector<vector<char> > _record,
               int _index,
               vector<Point> _wait_vec,
               int _amount_of_unrevealed,
               const int _amount_of_not_mines)
{
  if (0 != _record.size())
  {
    if (_amount_of_unrevealed != _amount_of_not_mines)
    {
      Point p = _wait_vec[_index];
      _wait_vec.erase(_wait_vec.begin() + _index);
      _record[p.x][p.y] = '0';

      // Right
      if ('*' == _record[p.x][p.y + 1])
      {
        _record[p.x][p.y + 1] = '1';
        Point _p(p.x, p.y + 1);
        _wait_vec.push_back(Point(p.x, p.y + 1));
        _amount_of_unrevealed++;
      }
      
      // Down Right
      if ('*' == _record[p.x + 1][p.y + 1])
      {
        _record[p.x + 1][p.y + 1] = '1';
        _wait_vec.push_back(Point(p.x + 1, p.y + 1));
        _amount_of_unrevealed++;
      }

      // Down
      if ('*' == _record[p.x + 1][p.y])
      {
        _record[p.x + 1][p.y] = '1';
        _wait_vec.push_back(Point(p.x + 1, p.y));
        _amount_of_unrevealed++;
      }

      // Down Left
      if ('*' == _record[p.x + 1][p.y - 1])
      {
        _record[p.x + 1][p.y - 1] = '1';
        _wait_vec.push_back(Point(p.x + 1, p.y - 1));
        _amount_of_unrevealed++;
      }

      // Left
      if ('*' == _record[p.x][p.y - 1])
      {
        _record[p.x][p.y - 1] = '1';
        _wait_vec.push_back(Point(p.x, p.y - 1));
        _amount_of_unrevealed++;
      }

      // Up Left
      if ('*' == _record[p.x - 1][p.y - 1])
      {
        _record[p.x - 1][p.y - 1] = '1';
        _wait_vec.push_back(Point(p.x - 1, p.y - 1));
        _amount_of_unrevealed++;
      }

      // Up
      if ('*' == _record[p.x - 1][p.y])
      {
        _record[p.x - 1][p.y] = '1';
        _wait_vec.push_back(Point(p.x - 1, p.y));
        _amount_of_unrevealed++;
      }

      // Up Right
      if ('*' == _record[p.x - 1][p.y + 1])
      {
        _record[p.x - 1][p.y + 1] = '1';
        _wait_vec.push_back(Point(p.x - 1, p.y + 1));
        _amount_of_unrevealed++;
      }

      if (_amount_of_unrevealed > _amount_of_not_mines)
      {
        _record.clear();
      }
      else if (_amount_of_unrevealed < _amount_of_not_mines)
      {
        for (int i = 0; i < _wait_vec.size(); ++i)
        {
          vector<vector<char> > result = recuresive_run(_record, i, _wait_vec, _amount_of_unrevealed, _amount_of_not_mines);
          if (0 != result.size())
          {
            return result;
          }
        }        
      }
    }
  }
  else
  {
    _record.clear();
  }

  if (_amount_of_unrevealed != _amount_of_not_mines)
  {
    _record.clear();
  }
  return _record;
}
