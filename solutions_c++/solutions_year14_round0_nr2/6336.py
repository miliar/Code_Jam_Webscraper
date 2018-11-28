#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <iomanip>
#include <cfloat>

#define INITIAL_VELOCITY (2.0)

struct Configuration
{
  double c;
  double f;
  double x;
};

void
readLine(std::istream& stream, std::istringstream& parser)
{
  std::string line;

  std::getline(stream, line);
  parser.str(line);
}

Configuration
readConfiguration(std::istream& stream)
{
  std::istringstream lineParser;
  Configuration      configuration;

  readLine(stream, lineParser);
  lineParser >> configuration.c >> configuration.f >> configuration.x;

  return configuration;
}

std::vector<Configuration>
parseInput(std::ifstream& fileStream)
{
  std::vector<Configuration> result;
  std::istringstream         lineParser;
  short casesCount = 0;

  readLine(fileStream, lineParser);
  lineParser >> casesCount;

  for (short i = 0; i < casesCount && fileStream.eof() == false; ++i)
  {
    Configuration configuration;

    configuration = readConfiguration(fileStream);

    result.push_back(configuration);
  }

  return result;
}

double
computeTotalTime(const Configuration& configuration)
{
  double velocity        = INITIAL_VELOCITY;
  double farmTime        = configuration.c / velocity;
  double targetTime      = configuration.x / velocity;
  double minTotalTime    = targetTime;
  double accumulatedTime = 0.0;

  while (accumulatedTime <= minTotalTime)
  {
    accumulatedTime += farmTime;

    velocity  += configuration.f;
    farmTime   = configuration.c / velocity;
    targetTime = configuration.x / velocity;

    minTotalTime = std::min(minTotalTime, accumulatedTime + targetTime);
  }

  return minTotalTime;
}

std::vector<double>
solve(const std::vector<Configuration>& configurations)
{
  std::vector<double> result;

  for (size_t i = 0; i < configurations.size(); ++i)
    result.push_back(computeTotalTime(configurations[i]));

  return result;
}

void
save(const std::vector<double>& results, const std::string& filename)
{
  std::ofstream stream(filename.c_str(), std::ofstream::out | std::ofstream::trunc);

  for (size_t i = 0; i < results.size(); ++i)
    stream << "Case #" << i + 1 << ": " << std::setprecision(10) << results[i] << std::endl;
}

int
main(int argc, char** argv)
{
  if (argc < 3)
    return -1;

  std::ifstream fileStream(argv[1]);

  if (fileStream.is_open() == false)
    return -2;

  std::vector<Configuration> configurations = parseInput(fileStream);
  std::vector<double>        results        = solve(configurations);

  save(results, argv[2]);

  return 0;
}
