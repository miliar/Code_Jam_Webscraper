#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;
int main(int argc, char* argv[]) {
  ifstream ifile(argv[1]);
  int N;
  ifile >> N;
  string line;
  getline(ifile, line);
  for(int C = 1; C <= N; ++C) {
    int num_friends = 0;
    int num_people_standing = 0;
    vector<int> shyness;
    getline(ifile, line);
    stringstream ss;
    ss << line;
    int max_shyness;
    ss >> max_shyness;
    size_t st = line.find_first_of(" ");
    for(int i = st + 1; i <= max_shyness + st + 1; ++i) {
      shyness.push_back(line[i] - '0');
    }
    for(int i = 0; i < shyness.size(); ++i) {
      if(num_people_standing < i && shyness[i] != 0) {
        int added_friends = i - num_people_standing;
        num_people_standing += added_friends;
        num_friends += added_friends;
      }
      num_people_standing += shyness[i];
    }
    cout << "Case #" << C << ": ";
    printf("%d\n", num_friends);
  }
  return 1;
}