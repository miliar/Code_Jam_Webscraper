#include <fstream>
#include <sstream>
#include <string>
#include <vector>

#define BAD_MAGICIAN      "Bad magician!"
#define VOLUNTEER_CHEATED "Volunteer cheated!"
#define GRID_SIZE         (4)

struct TrickRound
{
  short selection;
  short grid[GRID_SIZE][GRID_SIZE];
};

struct MagicTrick
{
  TrickRound rounds[2];
};

void
readLine(std::istream& stream, std::istringstream& parser)
{
  std::string line;

  std::getline(stream, line);
  parser.str(line);
}

short
readVolunteerSelection(std::istream& stream)
{
  std::istringstream lineParser;
  short result = 0;

  readLine(stream, lineParser);
  lineParser >> result;

  return result;
}

void
readGridRow(std::istream& stream, short* row)
{
  std::istringstream lineParser;

  readLine(stream, lineParser);
  lineParser >> row[0] >> row[1] >> row[2] >> row[3];
}

TrickRound
readRound(std::istream& stream)
{
  TrickRound result;

  result.selection = readVolunteerSelection(stream);

  for (size_t i = 0; i < GRID_SIZE; ++i)
    readGridRow(stream, result.grid[i]);

  return result;
}

std::vector<MagicTrick>
parseInput(std::ifstream& fileStream)
{
  std::vector<MagicTrick> result;
  std::istringstream      lineParser;
  short tricksCount = 0;

  readLine(fileStream, lineParser);
  lineParser >> tricksCount;

  for (short i = 0; i < tricksCount && fileStream.eof() == false; ++i)
  {
    MagicTrick trick;

    trick.rounds[0] = readRound(fileStream);
    trick.rounds[1] = readRound(fileStream);

    result.push_back(trick);
  }

  return result;
}

std::string
doMagic(const MagicTrick& trick)
{
  std::string        result = VOLUNTEER_CHEATED;
  std::vector<short> presentCards;

  size_t row0 = trick.rounds[0].selection - 1;
  size_t row1 = trick.rounds[1].selection - 1;

  for (size_t i = 0; i < GRID_SIZE; ++i)
  {
    short candidate = trick.rounds[0].grid[row0][i];

    for (size_t j = 0; j < GRID_SIZE; ++j)
    {
      if (trick.rounds[1].grid[row1][j] == candidate)
        presentCards.push_back(candidate);
    }
  }

  if (presentCards.empty())
    result = VOLUNTEER_CHEATED;
  else if (presentCards.size() > 1)
    result = BAD_MAGICIAN;
  else
  {
    std::ostringstream stream;

    stream << presentCards.front();
    result = stream.str();
  }

  return result;
}

std::vector<std::string>
solveTricks(const std::vector<MagicTrick>& tricks)
{
  std::vector<std::string> results;

  for (size_t i = 0; i < tricks.size(); ++i)
    results.push_back(doMagic(tricks[i]));

  return results;
}

void
save(const std::vector<std::string>& results, const std::string& filename)
{
  std::ofstream stream(filename.c_str(), std::ofstream::out | std::ofstream::trunc);

  for (size_t i = 0; i < results.size(); ++i)
    stream << "Case #" << i + 1 << ": " << results[i] << std::endl;
}

int
main(int argc, char** argv)
{
  if (argc < 3)
    return -1;

  std::ifstream fileStream(argv[1]);

  if (fileStream.is_open() == false)
    return -2;

  std::vector<MagicTrick>  tricks  = parseInput(fileStream);
  std::vector<std::string> results = solveTricks(tricks);

  save(results, argv[2]);

  return 0;
}
