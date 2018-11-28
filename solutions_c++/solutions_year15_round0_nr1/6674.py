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
const std::string FILE_NAME = "A-small-attempt0";
//const std::string FILE_NAME = "A-large";
const std::string FILE_NAME_IN = FILE_NAME + ".in";
const std::string FILE_NAME_OUT = FILE_NAME + ".out";

struct TestCase
{
  std::map<size_t, size_t> levels;

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
  std::string levels;

  fin >> count;
  fin >> levels;
  
  for (int i = 0; i <= count; i++)
  {
    size_t level = levels[i] - '0';
    if (level > 0)
      test.levels.insert(std::make_pair(i, level));
  }

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

std::string TestCase::execute() const
{
  size_t count = 0;
  size_t needed = 0;

  for (const auto& pair : levels)
  {
    if (pair.first > count)
      needed += pair.first - count;
    count += needed + pair.second;
  }

  return std::to_string(needed);
}
