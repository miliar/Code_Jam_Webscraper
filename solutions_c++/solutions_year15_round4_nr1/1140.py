/*
 * Google Code Jam
 * Vladimir Rutsky <vladimir@rutsky.org>
 */

#undef NDEBUG
#include <cassert>

#include <iostream>
#include <cstdio>
#include <iomanip>
#include <sstream>
#include <cstring>
#include <locale>
#include <ctime>
#include <iterator>
#include <algorithm>
#include <array>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>

using namespace std;

tuple<bool, bool, bool, bool> has_neighbour(vector<string> const & M, int r, int c)
{
  bool left(false), right(false), up(false), down(false);

  for (int i = c + 1; i < M[0].size(); ++i)
    if (M[r][i] != '.')
      right = true;
  for (int i = c - 1; i >= 0; --i)
    if (M[r][i] != '.')
      left = true;
  for (int i = r + 1; i < M.size(); ++i)
    if (M[i][c] != '.')
      down = true;
  for (int i = r - 1; i >= 0; --i)
    if (M[i][c] != '.')
      up = true;

  return make_tuple(left, right, up, down);
}

string solve(vector<string> const & M)
{
  size_t res = 0;

  for (size_t r = 0; r != M.size(); ++r)
    for (size_t c = 0; c != M[0].size(); ++c)
    {
      char const ch = M[r][c];
      if (ch == '.')
        continue;

      bool left, right, up, down;
      tie(left, right, up, down) = has_neighbour(M, r, c);

      bool has_neighbour = left || right || up || down;

      if (!has_neighbour)
        return "IMPOSSIBLE";

      if (ch == '>' && !right)
        ++res;
      else if (ch == '<' && !left)
        ++res;
      else if (ch == '^' && !up)
        ++res;
      else if (ch == 'v' && !down)
        ++res;
    }

  return to_string(res);
}

int main(int argc, char *argv[])
{
  if (true)
  {
    std::tm local_tm;
    // "Mmm dd yyyy hh:mm:ss"
    char const * compile_time_string = __DATE__ " " __TIME__;
    std::time_t const cur_time = std::time(nullptr);

    /*
    std::istringstream ss(compile_time_string);
    ss.imbue(std::locale::classic());
    ss >> std::get_time(&local_tm, "%b %d %Y %H:%M:%S");
    */

    std::memcpy(&local_tm, localtime(&cur_time), sizeof(local_tm));
    strptime(compile_time_string, "%b %d %Y %H:%M:%S", &local_tm);

    std::time_t const compile_time = mktime(&local_tm);

    double const diff = difftime(cur_time, compile_time);

    std::cerr << "DEBUG: Compiled " << diff << " seconds ago" << (diff > 60 ? "!!!" : ".") << "\n";
  }

  //FILE * res = std::freopen("small.in", "rt", stdin);
  //FILE * res = std::freopen("A-small-attempt0.in", "rt", stdin);
  //FILE * res = std::freopen("A-large.in", "rt", stdin);
  //assert(res);

  if (argc > 2)
  {
    std::cerr
      << "Usage:\n"
      << "    " << argv[0] << " [input.in]";
  }
  else if (argc == 2)
  {
    std::string const suffix = ".in";
    std::string const input_path = argv[1];
    assert(input_path.size() > suffix.size());
    assert(input_path.substr(input_path.length() - suffix.size()) == suffix);

    std::string const file_path = input_path.substr(0, input_path.length() - suffix.size());

    std::string const output_path = file_path + ".out";

    std::FILE * in_file = std::freopen(input_path.c_str(), "rt", stdin);
    assert(in_file);

    std::FILE * out_file = std::freopen(output_path.c_str(), "wt", stdout);
    assert(out_file);

    std::cerr << "DEBUG: Reading from '" << input_path << "', writing to '" << output_path << "'\n";
  }
  else
  {
    std::cerr << "DEBUG: Reading from STDOUT, writing to STDOUT\n";
  }

  size_t T = 0;
  cin >> T;

  for (size_t ci = 1; ci <= T; ++ci)
  {
    size_t R, C;
    cin >> R >> C;
    vector<string> M(R);
    for (size_t r = 0; r != R; ++r)
        cin >> M[r];

    cout << "Case #" << ci << ": " << solve(M) << "\n";
  }
}
