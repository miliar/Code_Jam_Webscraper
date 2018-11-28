/**
 * @file main.cpp
 * @brief Code jam problem solution.
 * @author apollyon <alejandro.claro@gmail.com>
 * @copyright 2014 Alejandro Claro.
 */

/* PRAGMAS *******************************************************************/

// #pragma comment (linker, "/STACK:256000000")

/* INCLUDES ******************************************************************/

#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

/* DECLARATIONS **************************************************************/

struct Input
{
  long x;
  long r;
  long c;
};

struct Output
{
  std::string winner;
};

/* PROTOTYPES ****************************************************************/

void solve(const Input& input, Output& output);
void readInput(Input& input);
void writeOutput(const Output& output);

/* IMPLEMENTATION ************************************************************/

int
main(int argc, char** argv)
{
  size_t casesCount = 0;

  if (argc > 1)
    std::freopen(argv[1], "r", stdin);

  if (argc > 2)
    std::freopen(argv[2], "w", stdout);

  std::cin >> casesCount;

  for(size_t i = 1; i <= casesCount; ++i)
  {
    Input  input;
    Output output;

    readInput(input);

    std::cout << "Case #" << i << ": ";

    solve(input, output);
    //std::cout << input.x << " " << input.r << "x" << input.c << " ";
    writeOutput(output);

    std::cout << std::endl;
  }

  return 0;
}

void
solve(const Input& input, Output& output)
{
  long minSide = std::min(input.r, input.c);
  long maxSide = std::max(input.r, input.c);
  long cells   = input.r * input.c;
  long free    = cells - input.x;

  if (free % input.x != 0 || input.x > 6 || input.x > maxSide || (input.x / 2.0) > minSide || (input.x - minSide) > (maxSide - 1))
  {
    output.winner = "RICHARD";
    return;
  }

  if (input.x > 3)
  {
    long width  = 2;
    long height = input.x - 1;

    for (; width * height >= input.x; --height, ++width)
    {
      if ((width == input.c) && (height >= (input.r - 1)))
      {
        output.winner = "RICHARD";
        return;
      }

      if ((height == input.c) && (width >= (input.r - 1)))
      {
        output.winner = "RICHARD";
        return;
      }
    }
  }

  output.winner = "GABRIEL";
}

void
readInput(Input& input)
{
  std::cin >> input.x >> input.r >> input.c;
}

void
writeOutput(const Output& output)
{
  std::cout << output.winner;
}
