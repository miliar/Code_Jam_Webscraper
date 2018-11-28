#include <iostream>
#include <string>
#include <vector>

enum Q {
  one, i, j, k, minus_one, minus_i, minus_j, minus_k
};

#define RESULT(x,y,c) if (a == x && b == y) return c

const std::vector<std::vector<Q>> product_table = {
  {one, i, j, k, minus_one, minus_i, minus_j, minus_k},
  {i, minus_one, k, minus_j, minus_i, one, minus_k, j},
  {j, minus_k, minus_one, i, minus_j, k, one, minus_i},
  {k, j, minus_i, minus_one, minus_k, minus_j, i, one},
  {minus_one, minus_i, minus_j, minus_k, one, i, j, k},
  {minus_i, one, minus_k, j, i, minus_one, k, minus_j},
  {minus_j, k, one, minus_i, j, minus_k, minus_one, i},
  {minus_k, minus_j, i, one, k, j, minus_i, minus_one}
};

Q product(Q a, Q b)
{
  return product_table[a][b];
}

void print_Q(Q q)
{
  switch (q) {
    case one: std::cout << 1; break;
    case minus_one: std::cout << -1; break;
    case i: std::cout << "i"; break;
    case minus_i: std::cout << "-i"; break;
    case j: std::cout << "j"; break;
    case minus_j: std::cout <<  "-j"; break;
    case k: std::cout << "k"; break;
    case minus_k: std::cout << "-k"; break;
  }
}

Q parse(char s)
{
  switch (s) {
    case 'i': return i;
    case 'j': return j;
    case 'k': return k;
  }
  return one;
}

bool is_j(Q a, Q b)
{
  if (product(a, j) == b) return true;
  return false;
}

bool is_k(Q a, Q b)
{
  if (product(a, k) == b) return true;
  return false;
}

std::string solve()
{
  int x, l;
  std::string s;
  std::cin >> l >> x >> s;
  if (x*l < 3) return "NO";
  std::vector<Q> cp(x*l);
  for (int a = 0; a < x; a++) {
    for (int b = 0; b < l; b++) {
      if (a*l+b) {
        cp[a*l+b] = product(cp[a*l+b-1], parse(s[b]));
      } else {
        cp[a*l+b] = parse(s[b]);
      }
    }
  }
  std::vector<int> ipos;
  for (int a = 0; a < cp.size()-2; a++) {
    if (cp[a] == i) {
      ipos.push_back(a);
    }
  }
  for (int a = 1; a < cp.size()-1; a++) {
    if (is_k(cp[a], cp[cp.size()-1])) {
      for (int b = 0; b < ipos.size() && ipos[b] <= a; b++) {
        if (is_j(cp[ipos[b]], cp[a])) {
          return "YES";
        }
      }
    }
  }
  return "NO";
}

int main()
{
  int cases;
  std::cin >> cases;
  for (int a = 0; a < cases; a++) {
    std::cout << "Case #" << a+1 << ": " << solve() << std::endl;
  }
}
