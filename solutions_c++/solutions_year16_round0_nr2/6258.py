#include <iostream>
#include <vector>

unsigned int min;

void switch_chars(std::string& path, int beg, int end)
{
  int mid = (end + beg) / 2;
  char tmp;
  for (int i = beg; i <= mid; ++i)
  {
    tmp = path[end - i] == '+' ? '-' : '+';
    path[end - i] = path[beg + i] == '+' ? '-' : '+';
    path[beg + i] = tmp;
  }
}

int ex2(std::string path, char cur, int nb, int n)
{
  if (n < 0)
    return nb;
  if (path[n] == cur)
    return ex2(path, cur, nb, n - 1);
  else
  {
    if (path[0] == path[n])
    {
      switch_chars(path, 0, n);
      return ex2(path, cur, nb + 1, n - 1);
    }
    else
      return ex2(path, cur == '-' ? '+' : '-', nb + 1, n - 1);
  }
}

int main(int argc, char* argv[])
{
  int n;
  std::string res;
  std::cin >> n;
  for (int i = 1; i <= n; ++i)
  {
    std::cin >> res;
    std::cout << "Case #" + std::to_string(i) + ": " + std::to_string(ex2(res, res[res.length() - 1], (res[res.length() - 1] == '-' ? 1 : 0), res.length() - 1)) + "\n";
  }
} 
