#include <cstdint>
#include <iostream>
#include <deque>
#include <string>
#include <stdexcept>
#include <algorithm>

using Stack = std::deque<bool>;

Stack createStack(std::string const &s)
{
  Stack stack;
  for (auto c : s)
  {
    switch (c)
    {
      case '+':
        stack.push_back(true);
        break;
      case '-':
        stack.push_back(false);
        break;
      default:
        throw std::runtime_error("bad character");
    }
  }
  return stack;
}

template<typename It>
void flip(It b, It e)
{

  while (b != e)
  {
    //std::cout << "flip " << std::distance(b, e) << std::endl;
    --e;
    if (b == e)
    {
      *b = !*b;
      return;
    }

    auto tmp(!*b);
    *b = !*e;
    *e = tmp;

    ++b;
  }
}

void printStack(Stack const &s)
{
  for (auto p : s)
    std::cout << (p ? '+' : '-');
}

uint32_t makeTopSad(Stack &pancakes)
{
  if (!pancakes.front())
    return 0; // top is already sad

  auto i(std::find(pancakes.begin(), pancakes.end(), false));
  flip(pancakes.begin(), i);
  return 1;
}

void handle(std::string const &s)
{
  Stack pancakes(createStack(s));

  uint32_t flips(0);

  // we keep the top sad so that any flip actually makes the bottem happy
  auto end(pancakes.rend());
  for(auto i = pancakes.rbegin(); i != end; ++i)
  {
    if (!*i)
    {
      flips += makeTopSad(pancakes);
      flip(i, end);
      ++flips;
    }
  }

  //printStack(pancakes);
  std::cout << flips << std::endl;
}

int main()
{
  uint32_t t;
  std::cin >> t;
  if (t < 1 || t > 100)
  {
    std::cerr << "invalid t: " << t << std::endl;
    exit(1);
  }

  uint32_t i = 1;
  std::string s;
  while (std::cin >> s)
  {
    std::cout << "case #" << i << ": ";
    handle(s);
    ++i;
  }
}

