// Standard Includes
#include <algorithm>
#include <fstream>
#include <iostream>
#include <iterator>
#include <map>
#include <math.h>
#include <set>
#include <stack>
#include <string>
#include <vector>

// Defines
//#define VERBOSE

// Constants
//const std::string FILE_NAME = "test";
const std::string FILE_NAME = "C-small-attempt0";
//const std::string FILE_NAME = "C-large";
const std::string FILE_NAME_IN = FILE_NAME + ".in";
const std::string FILE_NAME_OUT = FILE_NAME + ".out";

struct TestCase
{
  size_t repeat;
  std::string ijk;

  std::string execute() const;
};

void executeTests(const std::vector<TestCase>& testCases);
std::vector<TestCase> readTestCases();

int main()
{
  auto tests = readTestCases();
  executeTests(tests);

  return 0;
}

void executeTest(const TestCase& test, std::ofstream& fout, size_t total)
{
  static int number = 1;
  static double lastPer = 0;

#ifdef VERBOSE
  std::cout << "Executing test case " << number << ": ";
#endif

  auto result = test.execute();

#ifdef VERBOSE
  std::cout << result << std::endl;
#endif

  fout << "Case #" << number << ": " << result << std::endl;

  double per = number * 100.0 / total;

  if (per >= lastPer + 1)
  {
    std::cout << static_cast<int>(per) << "% complete\n";
    lastPer = per;
  }

  number++;
}

void executeTests(const std::vector<TestCase>& tests)
{
  std::ofstream fout(FILE_NAME_OUT);
  auto count = tests.size();
  for (const auto& test : tests)
    executeTest(test, fout, count);
  fout.flush();
  fout.close();
}

TestCase readTestCase(std::ifstream& fin)
{
  TestCase test;
  size_t count = 0;

  fin >> count >> test.repeat >> test.ijk;

  return test;
}

std::vector<TestCase> readTestCases()
{
  std::vector<TestCase> cases;
  std::ifstream fin(FILE_NAME_IN);

  int caseCount = 0;
  fin >> caseCount;
  std::cout << "Reading in " << caseCount << " test cases.\n";

  std::generate_n(std::back_inserter(cases), caseCount, [&] { return readTestCase(fin); });

  fin.close();

  return cases;
}

int index(char c)
{
  switch (c)
  {
  default:
  case '1': return 0;
  case 'i': return 1;
  case 'j': return 2;
  case 'k': return 3;
  case '-': return 4;
  case 'I': return 5;
  case 'J': return 6;
  case 'K': return 7;
  }
}

char multiply(char c1, char c2)
{
  char LUT[8][8] = {
    { '1', 'i', 'j', 'k', '-', 'I', 'J', 'K' },
    { 'i', '-', 'k', 'J', 'I', '1', 'K', 'j' },
    { 'j', 'K', '-', 'i', 'J', 'k', '1', 'I' },
    { 'k', 'j', 'I', '-', 'K', 'J', 'i', '1' },
    { '-', 'I', 'J', 'K', '1', 'i', 'j', 'k' },
    { 'I', '1', 'K', 'j', 'i', '-', 'k', 'J' },
    { 'J', 'k', '1', 'I', 'j', 'K', '-', 'i' },
    { 'K', 'J', 'i', '1', 'k', 'j', 'I', '-' }
  };

  return LUT[index(c1)][index(c2)];
}

bool has(std::string& rStr, char c, bool useAll = false)
{
  char product = '1';
  while (!rStr.empty())
  {
    char back = rStr.back();
    rStr.pop_back();

    product = multiply(back, product);
    if (!useAll && product == c)
      return true;
  }
  return useAll && product == c;
}

bool isIjk(const std::string& str, size_t repeat)
{
  std::string ijk;
  for (int i = 0; i < repeat; i++)
    ijk += str;
  return has(ijk, 'k') && has(ijk, 'j') && has(ijk, 'i', true);
}

std::string TestCase::execute() const
{
  return isIjk(ijk, repeat) ? "YES" : "NO";
}
