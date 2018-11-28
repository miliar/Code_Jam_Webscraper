#include <iostream>
#include <vector>

#define SQUARE_SIZE 4

static std::vector<int>* get_array()
{
  std::vector<int>* array = new std::vector<int>(0);

  for (int i = 0; i < SQUARE_SIZE * SQUARE_SIZE; i++)
  {
    int tmp = 0;
    std::cin >> tmp;
    array->push_back(tmp);
  }

  return array;
}

// r1, r2 in range of [0...3].
static int get_answer(std::vector<int>* a1,
                      std::vector<int>* a2,
                      int r1,
                      int r2)
{
  int common_elements = 0;
  int answer = 0;
  for (int i = r1 * SQUARE_SIZE; i < (r1 + 1) * SQUARE_SIZE; i++)
    for (int j = r2 * SQUARE_SIZE; j < (r2 + 1) * SQUARE_SIZE; j++)
    {
      if ((*a1)[i] == (*a2)[j])
      {
        common_elements++;
        answer = (*a1)[i];
      }
    }

  if (common_elements == 0)
    return -2;
  if (common_elements > 1)
    return -1;

  return answer;
}

int main()
{
  // Retrieves number of test case.
  int n;
  std::cin >> n;

  for (int i = 1; i <= n; i++)
  {
    int r1 = 0;
    int r2 = 0;

    std::cin >> r1;
    std::vector<int>* a1 = get_array();

    std::cin >> r2;
    std::vector<int>* a2 = get_array();

    int answer = get_answer(a1, a2, r1 - 1, r2 - 1);

    std::cout << "Case #" << i << ": ";
    if (answer == -1)
      std::cout << "Bad magician!" << std::endl;
    else if (answer == -2)
      std::cout << "Volunteer cheated!" << std::endl;
    else
      std::cout << answer << std::endl;
  }

  return 0;
}
