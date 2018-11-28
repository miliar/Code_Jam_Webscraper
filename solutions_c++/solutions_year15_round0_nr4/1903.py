#include <iostream>
#include <string>

#define TEST(l,w,s) \
  if ((c == l && r == w) || (c == w && r == l)) return #s

std::string solve()
{
  int x,r,c;
  std::cin >> x >> r >> c;
  switch (x) {
    case 1: {
      return "GABRIEL";
    }
    case 2: {
      TEST(1,1,RICHARD);
      TEST(1,2,GABRIEL);
      TEST(1,3,RICHARD);
      TEST(1,4,GABRIEL);
      TEST(2,2,GABRIEL);
      TEST(2,3,GABRIEL);
      TEST(2,4,GABRIEL);
      TEST(3,3,RICHARD);
      TEST(3,4,GABRIEL);
      TEST(4,4,GABRIEL);
    }
    case 3: {
      TEST(1,1,RICHARD);
      TEST(1,2,RICHARD);
      TEST(1,3,RICHARD);
      TEST(1,4,RICHARD);
      TEST(2,2,RICHARD);
      TEST(2,3,GABRIEL);
      TEST(2,4,RICHARD);
      TEST(3,3,GABRIEL);
      TEST(3,4,GABRIEL);
      TEST(4,4,RICHARD);
    }
    case 4: {
      TEST(1,1,RICHARD);
      TEST(1,2,RICHARD);
      TEST(1,3,RICHARD);
      TEST(1,4,RICHARD);
      TEST(2,2,RICHARD);
      TEST(2,3,RICHARD);
      TEST(2,4,RICHARD);
      TEST(3,3,RICHARD);
      TEST(3,4,GABRIEL);
      TEST(4,4,GABRIEL);
    }
    default: {
      std::cerr << "ERROR";
      return "ERR";
    }
  }
}

int main()
{
  int cases;
  std::cin >> cases;
  for (int i = 0; i < cases; i++) {
    std::cout << "Case #" << i+1 << ": " << solve() << std::endl;
  }
}
