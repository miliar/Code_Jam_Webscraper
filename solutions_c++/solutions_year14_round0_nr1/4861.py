#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <sstream>
#include <iterator>
#include <vector>
#include <map>
#include <algorithm>

/* solves the case in question, and writes the result to the
 * output filestream, where k represents the current case #.
 *   - Output Format -> Case #k: {results}
 *
 * N      - number of wires
 * Ai Bi  - height of left endpoint, height of right endpoint
 *
 * Find # of intersecting points
 * ---------------------------------------------------------------------- */
void solve_case(int k, std::ofstream &ofs, std::ifstream &ifs)
{
  std::map<int, int> m;
  int row; ifs >> row; ifs.get(); // row (1-4)
  int card = 0;

  for (int i = 0; i < 4; ++i)
  {
    for (int j = 0; j < 4; ++j)
    {
      ifs >> card;
      if (i == row - 1)
      {
        if (m.find(card) == m.end())
          m.insert(std::make_pair(card, 1));
        else
          ++m[card];
      }
    }
    ifs.get(); // scrap newline
  }

  ifs >> row; ifs.get(); // row2 (1-4)
  for (int i = 0; i < 4; ++i)
  {
    for (int j = 0; j < 4; ++j)
    {
      ifs >> card;
      if (i == row - 1)
      {
        if (m.find(card) == m.end())
          m.insert(std::make_pair(card, 1));
        else
          ++m[card];
      }
    }
    ifs.get(); // scrap newline
  }

  std::vector<int> v;
  for (const auto &it : m)
  {
    if (it.second > 1) v.push_back(it.first);
  }

  ofs << "Case #" << k << ": ";
  if (v.size() == 0)
  {
    ofs << "Volunteer cheated!";
  }
  else if (v.size() == 1)
  {
    ofs << v.front();
  }
  else
  {
    ofs << "Bad magician!";
  }
  std::endl(ofs);
}

/* ---------------------------------------------------------------------- */

int open_filestreams(const char *input_file, std::ofstream &ofs, std::ifstream &ifs)
{
  std::string output_file(input_file);
  output_file.append("-result.txt");

  ofs.open(output_file, std::ofstream::out);
  if (!ofs.is_open()) return 0;

  ifs.open(input_file, std::ifstream::in | std::ifstream::binary);
  if (!ifs.is_open()) return 0;

  return 1;
}

int main(int argc, char const *argv[])
{
  if (argc < 2) return 1;

  std::ofstream ofs; // open output file for case results
  std::ifstream ifs; // open input file for reading
  if (!open_filestreams(argv[1], ofs, ifs)) return 1;

  int N, k = 0;        // N total cases, k case number
  ifs >> N; ifs.get(); // grab total cases, junk '\n' character
  do { solve_case(++k, ofs, ifs); }
  while (--N);

  ifs.close(); ofs.close(); // close streams
  // std::cin.sync(); std::cin.get();
}