#include <fstream>
#include <vector>
#include <queue>

void readData(std::fstream& in, int& numTests,
  std::queue<std::pair<int, std::vector<int>>>& testData);
void solveAndWrite(std::fstream& out, int numTests,
  std::queue<std::pair<int, std::vector<int>>>& testData);
int solveTask1(std::pair<int, std::vector<int>>& testData);
int solveTask2(std::pair<int, std::vector<int>>& testData);

int main() {
  int numTests;
  std::queue<std::pair<int, std::vector<int>>> testData;
  std::fstream in("input.txt", std::ios::in);
  std::fstream out("output.txt", std::ios::out);

  readData(in, numTests, testData);
  solveAndWrite(out, numTests, testData);

  return 0;
}

void readData(std::fstream& in, int& numTests,
  std::queue<std::pair<int, std::vector<int>>>& testData) {
  int eatingTime;
  std::vector<int> data;
  std::pair<int, std::vector<int>> tmpData;

  in >> numTests;

  for (auto i = 0; i < numTests; ++i) {
    if (!data.empty())
      data.clear();

    int tmp;
    
    in >> eatingTime;
    for (auto j = 0; j < eatingTime; ++j) {
      in >> tmp;
      data.push_back(tmp);
    }
    
    tmpData = std::make_pair(eatingTime, data);
    testData.push(tmpData);
  }

  in.close();
}

void solveAndWrite(std::fstream& out, int numTests,
  std::queue<std::pair<int, std::vector<int>>>& testData) {
  std::pair<int, std::vector<int>> tmpData;

  for (auto i = 0; i < numTests; ++i) {
    tmpData = testData.front();
    testData.pop();

    out << "Case #" << i + 1 << ": " << solveTask1(tmpData) << " "
        << solveTask2(tmpData) << "\n";
  }

  out.close();
}

int solveTask1(std::pair<int, std::vector<int>>& testData) {
  int firstCheckpoint, secondCheckpoint, partialResult, result = 0;
  int eatingTime = testData.first;
  std::vector<int> data = testData.second;

  for (auto i = 0; i < data.size() - 1; ++i) {
    firstCheckpoint = data[i];
    secondCheckpoint = data[i + 1];
    partialResult = firstCheckpoint - secondCheckpoint;
    result += ((partialResult > 0) ? (partialResult) : (0));
  }

  return result;
}

int solveTask2(std::pair<int, std::vector<int>>& testData) {
  int firstCheckpoint, secondCheckpoint, checkpoint = 0;
  int partialResult, result = 0;
  int eatingTime = testData.first;
  std::vector<int> data = testData.second;

  for (auto i = 0; i < data.size() - 1; ++i) {
    firstCheckpoint = data[i];
    secondCheckpoint = data[i + 1];
    checkpoint = std::max(checkpoint, firstCheckpoint - secondCheckpoint);
  }

  for (auto i = 0; i < data.size() - 1; ++i) {
    result += std::min(data[i], checkpoint);
  }

  return result;
}