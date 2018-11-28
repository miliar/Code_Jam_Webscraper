/*
 * Problem-B-Lawnmower.cpp
 *
 *  Created on: 14.04.2013
 *      Author: XStalkerX
 */

#include <fstream>
#include <iostream>

#include <vector>

bool can_exit (std::vector<std::vector<int> > lawn, int x, int y)
{
  bool exit_horizontal = true;
  bool exit_vertical = true;

  for (int col = 0; col < lawn[y].size(); ++col)
  {
    if (lawn[y][col] > lawn[y][x])
      exit_horizontal = false;
  }

  for (int row = 0; row < lawn.size(); ++row)
  {
    if (lawn[row][x] > lawn[y][x])
      exit_vertical = false;
  }

  return (exit_horizontal or exit_vertical);
}

int main (int argc, char* argv[])
{
  if (argc != 2)
  {
    std::cout << "No file" << std::endl;
    return 0;
  }

  std::ifstream input (argv[1], std::fstream::in);
  if (!input.is_open())
  {
    std::cout << "Can't read" << std::endl;
    return -1;
  }

  std::ofstream output ("Lawnmower.out", std::fstream::out);
  if (!output.is_open())
  {
    std::cout << "Can't write" << std::endl;
    return -1;
  }


  int cases_number = 0;
  input >> cases_number;

  for (int case_i = 1; case_i <= cases_number; ++case_i)
  {
    int m = 0;
    int n = 0;

    input >> n >> m;

    std::vector<std::vector<int> > lawn;
    lawn.resize(n);

    int temp;
    for (int y = 0; y < n; ++y)
    {
      for (int x = 0; x < m; ++x)
      {
        input >> temp;
        lawn[y].push_back(temp);
      }
    }

//    for (int y = 0; y < n; ++y)
//    {
//      for (int x = 0; x < m; ++x)
//      {
//        std::cout << lawn[y][x];
//      }
//      std::cout << std::endl;
//    }
//
//    std::cout << std::endl;
    bool possible = true;
    for (int y = 0; y < n; ++y)
    {
      for (int x = 0; x < m; ++x)
      {
        if (!can_exit(lawn, x, y))
          possible = false;
      }
    }

    if (case_i != 1)
      output << std::endl;
    if (possible)
      output << "Case #" << case_i << ": YES";
    else
      output << "Case #" << case_i << ": NO";
  }

  input.close();
  output.close();

}


