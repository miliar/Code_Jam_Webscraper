//============================================================================
// Name        : MagicTrickCodeJam.cpp
// Author      : Angel Castillo.
// Email       : ArcangelZ@gmail.com
// Description : Google Code Jam 2014 problem A - Magic Trick
//============================================================================

#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <vector>

/* DEFINES *******************************************************************/

#define GRID_SIZE      4
#define TEST_cASE_SIZE 10

/* IMPLEMENTATIONS ***********************************************************/

/**
 * @brief Gets a single test case from a given input stream.
 *
 * @param testCase        The output stream where the test case will be written.
 * @param testCasesSource The input source from where the test case will be taken.
 * @param testCaseSize    The size (in lines) of the test case.
 */
void
getTestCase(std::ostream& testCase, std::istream& testCasesSource, size_t testCaseSize)
{
  for (size_t i = 0; i < testCaseSize; ++i)
  {
    std::string line;
    std::getline(testCasesSource, line);

    testCase << line << std::endl;
  }
}

/**
 * @brief Helper function to convert from string to integer.
 *
 * @param number The string that will be converted.
 */
int
toInt(const std::string& number)
{
  int               result = 0;
  std::stringstream stream(number);

  stream >> result;

  return result;
}

/**
 * @brief Helper function to convert from positive integers to string.
 *
 * @param number The number that will be converted.
 */
std::string
toString(size_t number)
{
  std::stringstream stream;

  stream << number;

  return stream.str();
}

/**
 * @brief Helper function that splits a string in tokens given a delimiter character.
 *
 * @param string    The string that needs to be split.
 * @param elements  The vector where the elements will be stored.
 * @param delimiter The delimiter character that will be used for the splitting.
 *
 * @return A reference to the elements vector.
 */
std::vector<std::string>&
split(const std::string& string, std::vector<std::string>& elements, char delimiter)
{
  std::stringstream ss(string);
  std::string item;

  while (std::getline(ss, item, delimiter))
    elements.push_back(item);

  return elements;
}

/**
 * @brief Template method for solving the test cases problems. Each test case will be pass as an argument
 * to the given solver.
 *
 * @param input        The stream from where the test cases will be read.
 * @param output       The output stream where the results will be written.
 * @param testCaseSize The size of the test cases (in lines).
 */
template<typename T>
void solve(std::istream& input, std::ostream& output, size_t testCaseSize)
{
  size_t      testCasesNumber = 0;
  std::string number;

  std::getline(input, number);

  testCasesNumber = toInt(number);

  T solver;

  for (size_t i = 0; i < testCasesNumber; ++i)
  {
    std::stringstream testCase;

    getTestCase(testCase, input, testCaseSize);
    std::string result = solver.solve(testCase.str());

    output << "Case #" << i + 1 << ": " << result << std::endl;
  }
}

/**
 * @brief The magic trick de-serialized structure.
 */
struct MagicTrick
{
  size_t selectedRow;
  size_t grid[GRID_SIZE][GRID_SIZE];
};

/**
 * @brief Parse a magic trick from a vector of strings.
 *
 * @param rows The magic trick in rows.
 *
 * @return The magic trick structure.
 */
MagicTrick
parseMagicTrick(std::vector<std::string>& rows)
{
  MagicTrick trick;

  trick.selectedRow = toInt(rows[0]);

  for (size_t i = 1; i < GRID_SIZE + 1; ++i)
  {
    std::vector<std::string> elements;

    split(rows[i], elements, ' ');

    for (size_t j = 0; j < GRID_SIZE; ++j)
      trick.grid[i-1][j] = toInt(elements[j]);
  }

  return trick;
}

/**
 * @brief Parse the given valid input into a collection of magic trick.
 *
 * @param input The magic trick as a string.
 *
 * @return The magic tricks coillection.
 */
std::vector<MagicTrick>
parseMagicTrickTestCase(const std::string& input)
{
  std::vector<MagicTrick> tricks;

  std::vector<std::string> allTricks;
  std::vector<std::string> firstTrick;
  std::vector<std::string> secondTrick;

  split(input, allTricks, '\n');

  std::copy(allTricks.begin(), allTricks.begin() + 5, std::back_inserter(firstTrick));
  std::copy(allTricks.begin() + 5, allTricks.begin() + 10, std::back_inserter(secondTrick));

  tricks.push_back(parseMagicTrick(firstTrick));
  tricks.push_back(parseMagicTrick(secondTrick));

  return tricks;
}

/**
 * @brief Gets the result message given a collection of found cards.
 */
std::string
getResultMessage(std::vector<size_t>& foundCardsInRow)
{
  std::string result;

  if (foundCardsInRow.size() == 1)
  {
    result = toString(foundCardsInRow[0]);
  }
  else if (foundCardsInRow.size() > 1)
  {
    result = "Bad magician!";
  }
  else
  {
    result = "Volunteer cheated!";
  }

  return result;
}

/**
 * @brief Magic trick solver class.
 */
class MagicTrickProblem
{
  public:

    /**
     * @brief Solves the given set magic trick problem test cases.
     */
    std::string solve(const std::string& testCase)
    {
      std::vector<MagicTrick> tricks = parseMagicTrickTestCase(testCase);

      std::vector<size_t> foundCardsInRow;

      size_t firstTrickSelection  = tricks[0].selectedRow - 1;
      size_t secondTrickSelection = tricks[1].selectedRow - 1;

      for (size_t i = 0; i < GRID_SIZE; ++i)
      {
        size_t firstSelectionCurrentCard = tricks[0].grid[firstTrickSelection][i];

        for (size_t j = 0; j < GRID_SIZE; ++j)
        {
          size_t secondSelectionCurrentCard = tricks[1].grid[secondTrickSelection][j];

          if (secondSelectionCurrentCard == firstSelectionCurrentCard)
            foundCardsInRow.push_back(firstSelectionCurrentCard);
        }
      }

      return getResultMessage(foundCardsInRow);
    }
};

int
main(int argc, char* argv[])
{
  std::fstream  inputFile(argv[1]);
  std::ofstream outputFile(argv[2], std::ofstream::out | std::ofstream::trunc);

  size_t testCaseSize = 10;

  std::stringstream result;

  solve<MagicTrickProblem>(inputFile, result, testCaseSize);

  outputFile << result.str();
  outputFile.close();

  return 0;
}
