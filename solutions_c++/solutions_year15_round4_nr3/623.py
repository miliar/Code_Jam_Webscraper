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

void mark_words(vector<int> & is_lang, vector<int> const & words)
{
  for (int w: words)
    is_lang[w] = 1;
}

int num_common(vector<int> & is_lang1, vector<int> & is_lang2)
{
  int res = 0;
  assert(is_lang1.size() == is_lang2.size());
  for (int i = 0; i != is_lang1.size(); ++i)
    if (is_lang1[i] && is_lang2[i])
      ++res;

  return res;
}

string solve(vector<vector<string>> const & words_strings)
{
  int N = words_strings.size();
  int next_id = 0;
  unordered_map<string, int> dict;

  vector<vector<int>> words(words_strings.size());
  int r = 0;
  for (vector<string> const & line : words_strings)
  {
    for (string const & w : line)
    {
      auto it = dict.find(w);
      if (it != dict.end())
        words[r].push_back(it->second);
      else
      {
        int id = next_id++;
        dict[w] = id;
        words[r].push_back(id);
      }
    }

    ++r;
  }

  vector<int> is_english_base(next_id, 0);
  vector<int> is_french_base(next_id, 0);

  mark_words(is_english_base, words[0]);
  mark_words(is_french_base, words[1]);

  int res_base = num_common(is_english_base, is_french_base);

  if (N == 2)
  {
    return to_string(res_base);
  }

  int min_res = 1 << 30;
  for (int x = 0; x != (1 << (N - 2)); ++x)
  {
    vector<int> is_english(is_english_base.begin(), is_english_base.end());
    vector<int> is_french(is_french_base.begin(), is_french_base.end());

    for (int i = 0; i != N - 2; ++i)
    {
      if (x & (1 << i))
        mark_words(is_english, words[2 + i]);
      else
        mark_words(is_french, words[2 + i]);
    }

    int res = num_common(is_english, is_french);
    if (res < min_res)
      min_res = res;
  }

  return to_string(min_res);
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
    size_t N;
    cin >> N;
    {
      string s;
      getline(cin, s);
      assert(s.empty());
    }

    vector<vector<string>> words(N);
    for (size_t r = 0; r != N; ++r)
    {
      string s;
      getline(cin, s);
      istringstream istr(s);

      while (true)
      {
        string w;
        istr >> w;
        if (w.empty())
          break;
        else
          words[r].push_back(w);
      }
    }

    cout << "Case #" << ci << ": " << solve(words) << "\n";
  }
}
