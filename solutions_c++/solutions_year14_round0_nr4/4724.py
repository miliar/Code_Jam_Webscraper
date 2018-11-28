#include <iostream>
#include <iomanip>
#include <string>
#include <fstream>
#include <algorithm>
#include <set>

/*
 * Weight Limits: 0.0kg <= X < 1.0kg
 *
 * T
 * N
 * {Naomi's block mass's}
 * {Ken's block mass's}
 *
 * OUTPUT:
 * Case #x: y z
 * y = deceitful war points
 * z = optimal war points
 * ---------------------------------------------------------------------- */

void get_blocks(std::set<double> &block_container, const int max_blocks, std::ifstream &ifs)
{
  double value;
  for (int i = 0; i < max_blocks; ++i)
  {
    ifs >> value; ifs.get();
    block_container.insert(value);
  }
}

std::set<double>::iterator find_next_highest(const std::set<double> &block_container, double value)
{
  for (std::set<double>::iterator it = block_container.begin();
       it != block_container.end(); ++it)
  {
    if (*it > value) return it;
  }
  return block_container.end();
}

int get_optimal_results(std::set<double> kens_blocks, std::set<double> naomis_blocks)
{
  int points = 0;
  while (kens_blocks.size() != 0)
  {
    auto chosen = kens_blocks.begin();
    auto block_iter = find_next_highest(naomis_blocks, *chosen);
    if (block_iter != naomis_blocks.end())
    {
      naomis_blocks.erase(block_iter);
    }
    else
    {
      ++points;
      naomis_blocks.erase(naomis_blocks.begin());
    }
    kens_blocks.erase(chosen);
  }
  return points;
}

int get_deceitful_results(std::set<double> kens_blocks, std::set<double> naomis_blocks)
{
  int points = 0;
  while (naomis_blocks.size() != 0)
  {
    auto naomis_highest = std::max_element(naomis_blocks.begin(), naomis_blocks.end());
    auto kens_block = find_next_highest(kens_blocks, *naomis_highest);
    if (kens_block == kens_blocks.end())
    {
      kens_blocks.erase(kens_blocks.begin());
    }
    else
    {
      ++points;
      kens_blocks.erase(kens_block);
    }
    naomis_blocks.erase(naomis_highest);
  }
  return points;
}

void solve_case(int k, std::ofstream &ofs, std::ifstream &ifs)
{
  std::set<double> kens_blocks;
  std::set<double> naomis_blocks;

  int max_blocks; ifs >> max_blocks; ifs.get();
  get_blocks(kens_blocks, max_blocks, ifs);
  get_blocks(naomis_blocks, max_blocks, ifs);

  int points_deceitful = get_deceitful_results(kens_blocks, naomis_blocks);
  int points_optimal = get_optimal_results(kens_blocks, naomis_blocks);

  ofs << "Case #" << k << ": " << points_deceitful << ' ' << points_optimal;
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
  ifs >> N;
  ifs.get(); // grab total cases, junk '\n' character
  do { solve_case(++k, ofs, ifs); }
  while (--N);

  ifs.close(); ofs.close(); // close streams
  // std::cin.sync(); std::cin.get();
}