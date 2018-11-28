	#include <iostream>
#include <map>
#include <vector>

int main()
{
  int num_cases;
  std::cin >> num_cases;
  std::vector<std::vector<int> > outputs;
  for (int a = 0; a < num_cases; a++) {
    std::map<int, int> counts;
    int size;
    std::cin >> size;
    for (int i = 0; i < 2*size-1; i++) {
      for(int j = 0; j < size; j++) {
        int input;
        std::cin >> input;
        if (counts.count(input) == 0) counts[input] = 1;
        else counts[input]++;
      }
    }

    std::vector<int> _outputs;
    for (std::map<int, int>::iterator it = counts.begin(); it != counts.end(); it++) {
      if (it->second%2 == 1) _outputs.push_back(it->first);
    }
    outputs.push_back(_outputs);
  }

  for (int a = 0; a < num_cases; a++) {
    std::cout << "Case #" << a+1 << ":";
    for (int b = 0; b < outputs[a].size(); b++) {
      std::cout << " " << outputs[a][b];
    }
    std::cout << std::endl;
  }
}

