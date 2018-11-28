#include <iostream>
#include <vector>

bool full(int numbers[10])
{ 
  for (int i = 0; i < 10; ++i)
    if (!numbers[i])
      return false;
  return true;
}

std::string ex1(unsigned long long first)
{
  if (!first)
    return "INSOMNIA";
  std::vector<unsigned long long> numbers;
  int digits[10];
  unsigned long long last;
  for (int i = 0; i < 10; ++i)
    digits[i] = 0;
  int n = 1;
  std::string digit_word;
  do
  {
    last = n * first;
    digit_word = std::to_string(last);
    for (int i = 0; i < digit_word.size(); ++i)
      digits[digit_word[i] - '0'] = 1;
    numbers.push_back(last);
    ++n;
  } while (!full(digits));
  return std::to_string(last);
}

int main(int argc, char* argv[])
{
  int n, N;
  std::cin >> n;
  for (int i = 1; i <= n; ++i)
  {
    std::cin >> N;
    std::cout << "Case #" + std::to_string(i) + ": " + ex1(N) + "\n";
  }
} 
