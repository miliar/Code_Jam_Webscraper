#include <iostream>
#include <iomanip>
#include <string>
#include <fstream>
#include <cfloat>

/*
 * Default cookies/sec: 2.00
 * Default cookies: 0.00
 *
 * C - cookies required to buy farm
 * F - extra cookies/sec from buying farm
 * X - target cookies
 * ----------------------------------------------------------------------- */

void solve_case(int k, std::ofstream &ofs, std::ifstream &ifs)
{
  double seconds;
  double min_seconds = DBL_MAX;
  const double default_cookies_per_second = 2.0; // default cookies per second
  double cookies_per_second = default_cookies_per_second; // cookies per second
  
  double C; ifs >> C; ifs.get(); // cost to buy cookie farm
  double F; ifs >> F; ifs.get(); // extra cookies per second after buying farm
  double X; ifs >> X; ifs.get(); // target

  int farms_bought = 1;
  do
  {
    cookies_per_second = default_cookies_per_second;
    seconds = 0.0;
    for (int i = 0; i < farms_bought - 1; ++i)
    {
      seconds += C / cookies_per_second;
      cookies_per_second += F;
    }
    seconds += X / cookies_per_second;
    if (seconds < min_seconds) min_seconds = seconds;
    ++farms_bought;
  }
  while (seconds <= min_seconds);

  ofs << "Case #" << k << ": ";
  ofs << std::fixed << std::setprecision(7);
  ofs << min_seconds << std::endl;
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