#include <iostream>

void exec()
{
  size_t shy_max;
  std::cin >> shy_max;
  std::string shy_k;
  std::cin >> shy_k;

  size_t invite_count = 0;
  size_t up_count = 0;
  for (int i = 0; i < shy_k.size(); ++i)
  {
    size_t k_pop = shy_k[i] - '0';
    if (up_count < i)
    {
      size_t to_invite = i - up_count;
      invite_count += to_invite;
      k_pop += to_invite;
    }
    up_count += k_pop;
  }
  std::cout << invite_count;
}

int main()
{
  size_t case_count;
  std::cin >> case_count;

  for (size_t i = 1; i <= case_count; ++i)
  {
    std::cout << "Case #" << i << ": ";
    exec();
    std::cout << std::endl;
  }
  return 0;
}
