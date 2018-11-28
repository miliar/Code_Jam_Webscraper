#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <unordered_map>
#include <numeric>
#include <deque>
#include <cmath>


template<typename T>
std::vector<T> space_split_string(std::string& input)
{
  std::stringstream ss(input);
  std::vector<T> return_value;
  T value;
  while (ss >> value)
  {
    return_value.push_back(value);
  }
  return return_value;
}

template<typename T>
std::string print_results(const std::vector<T>& results)
{
  std::stringstream output;
  int case_number = 1;
  for (auto result : results) {
    output << "Case #" << case_number << ": " << result << std::endl;
    case_number++;
  }
  return output.str();
}

template<typename T>
std::string vector_to_string(std::vector<T> input)
{
  std::stringstream output;
  for (int i = 0; i < input.size() - 1; i++) {
    output << input[i] << " ";
  }
  output << input.back();
  return output.str();
}

int main(int argc, char** argv)
{
  if (argc < 2) {
    return -1;
  }
  std::ifstream input_file(argv[1]);
  if (!input_file.is_open()) {
    return -1;
  }
  std::string num_cases_str;
  std::getline(input_file, num_cases_str);
  int num_cases = std::stoi(num_cases_str);

  std::vector<std::string> result;
  for (int i = 0; i < num_cases; i++) {
    std::string input;
    std::getline(input_file, input);
    int num_parties = std::stoi(input);
    std::string senators_str;
    std::getline(input_file, senators_str);
    std::vector<int> senators = space_split_string<int>(senators_str);

    int all_senators = std::accumulate(senators.begin(), senators.end(), 0);
    auto party_count = [](std::vector<int>& senators)
    {
      int count = 0;
      for (auto s : senators)
      {
        if (s > 0)
          count++;
      }
      return count;
    };

    std::string tmp_result;
    for (auto s : senators)
      printf("%d, ", s);
    printf("\n");

    while (all_senators > 3)
    {
      size_t max_party1 = 0;
      size_t max_party2 = 0;
      size_t max_members = 0;
      for (size_t s = 0; s < senators.size(); s++)
      {
        if (senators[s] > max_members)
        {
          max_members = senators[s];
          max_party1 = s;
        }
      }
      senators[max_party1] -= 1;
      max_members = 0;
      for (size_t s = 0; s < senators.size(); s++)
      {
        if (senators[s] > max_members)
        {
          max_members = senators[s];
          max_party2 = s;
        }
      }
      senators[max_party2] -= 1;
      char ab[3];
      ab[0] = max_party1 + 65;
      ab[1] = max_party2 + 65;
      ab[2] = 0;
      printf("%s, ", ab);
      tmp_result += std::string(ab) + " ";
      all_senators = std::accumulate(senators.begin(), senators.end(), 0);
      printf("All senators: %d\n", all_senators);
      for (auto s : senators)
        printf("%d, ", s);
      printf("\n");
    }
    auto max_it = std::max_element(senators.begin(), senators.end());
    if (party_count(senators) == 3 || (party_count(senators) == 2 && all_senators == 3))
    {
      char ab[3];
      int pos = std::distance(senators.begin(), max_it);
      ab[0] = pos + 65;
      senators[pos]--;
      ab[1] = 0;
      tmp_result += std::string(ab) + " ";
      max_it = std::max_element(senators.begin(), senators.end());
      pos = std::distance(senators.begin(), max_it);
      ab[0] = pos + 65;
      senators[pos]--;
      max_it = std::max_element(senators.begin(), senators.end());
      pos = std::distance(senators.begin(), max_it);
      ab[1] = pos + 65;
      senators[pos]--;
      ab[2] = 0;
      tmp_result += std::string(ab);
      printf("%s, ", ab);
    }
    else if (party_count(senators) == 2 && all_senators == 2)
    {
      int pos = std::distance(senators.begin(), max_it);
      char ab[3];
      ab[0] = pos + 65;
      senators[pos]--;
      for (auto s : senators)
        printf("%d, ", s);
      printf("\n");
      
      max_it = std::max_element(senators.begin(), senators.end());
      pos = std::distance(senators.begin(), max_it);
      ab[1] = pos + 65;
      ab[2] = 0;
      senators[pos]--;
      for (auto s : senators)
        printf("%d, ", s);
      printf("\n");
      tmp_result += std::string(ab);
      printf("%s, ", ab);
    }
    printf("\n");
    for (int j = 0; j < senators.size(); j++)
    {
      printf("%d, ", senators[j]);
    }
    printf("\n");

    result.push_back(tmp_result);
  }

  std::string result_str = print_results(result);

  std::ofstream output_file(argv[2]);
  if (output_file.is_open())
  {
    output_file << result_str;
    output_file.close();
  }

  return 0;
}
