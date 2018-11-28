#include <iostream>
#include <vector>


unsigned int count_needed()
{
  std::vector< unsigned int > people;
  unsigned int min_num_needed = 0;
  unsigned int shyness_levels = 0;
  unsigned int num_standing = 0;
  std::string all_people;

  std::cin >> shyness_levels;
  std::cin >> all_people;
  people.reserve(shyness_levels + 1);

  for (char& c : all_people)
    {
      people.push_back(c - '0');
    }

  for (size_t i = 0; i < people.size(); ++i)
    {
      if (num_standing < i)
        {
          unsigned int to_add = i - num_standing;
          num_standing += to_add;
          min_num_needed += to_add;
        }
      num_standing += people.at(i);
    }

  return min_num_needed;
}

int main()
{
  unsigned int num_cases = 0;

  std::cin >> num_cases;

  for (unsigned int i = 1; i <= num_cases; ++i)
    {
      std::cout << "Case #" << i << ": " << count_needed() << std::endl;
    }

  return 0;
}
