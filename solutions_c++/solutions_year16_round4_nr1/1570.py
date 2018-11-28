
#include <iostream>
#include <string>
#include <sstream>


std::string ans;

bool check(const std::string& lineup) {
  if (lineup.size() == 1) {
    return true;
  }
  std::string winners;
  for (size_t i = 0; i < lineup.size(); i += 2) {
    if (lineup.at(i+1) == 'U') {
      winners += 'U';
      continue;
    }
    if (lineup.at(i) == lineup.at(i+1)) {
      return false;
    }
    if (lineup.at(i) == 'P') {
      if (lineup.at(i+1) == 'R') {
        winners += ('P');
      }
      else {
        winners += ('S');
      }
    } else if (lineup.at(i) == 'R') {
      if (lineup.at(i+1) == 'P') {
        winners += ('P');
      } else {
        winners += ('R');
      }
    } else { // S
      if (lineup.at(i+1) == 'P') {
        winners += ('S');
      } else {
        winners += ('R');
      }
    }
  }
  return check(winners);
}

bool rec(int p, int r, int s, int next, std::string& lineup) {
  if (p == 0 && r == 0 && s == 0) {
    return true;
  }
  if (p != 0 && r != 0) {
    lineup[next] = 'P';
    lineup[next+1] = 'R';
    if (check(lineup)) {
      if (rec(p-1, r-1, s, next+2, lineup)) {
        return true;
      }
    }
    lineup[next] = 'U';
    lineup[next+1] = 'U';
  }
  if (p != 0 && s != 0) {
    lineup[next] = 'P';
    lineup[next+1] = 'S';
    if (check(lineup)) {
      if (rec(p-1, r, s-1, next+2, lineup)) {
        return true;
      }
    }
    lineup[next] = 'U';
    lineup[next+1] = 'U';
  }
  if (r != 0 && s != 0) {
    lineup[next] = 'R';
    lineup[next+1] = 'S';
    if (check(lineup)) {
      if (rec(p, r-1, s-1, next+2, lineup)) {
        return true;
      }
    }
    lineup[next] = 'U';
    lineup[next+1] = 'U';
  }
  return false;
}

std::string solve(const std::string& problem) {
  int t, r, p, s;
  std::istringstream iss(problem);
  iss >> t;
  iss >> r;
  iss >> p;
  iss >> s;
  std::string lu(r+p+s, 'U');
  if (rec(p, r, s, 0, lu)) {
    return lu;
  } else {
    return std::string("IMPOSSIBLE");
  }
}

int main()
{
  int lineNumber = 0;
  std::string l;
  int problemCount;
  std::getline(std::cin, l);
  {
    std::istringstream ss(l);
    ss >> problemCount;
  }
  while (std::getline(std::cin, l)) {
    std::cout << "Case #" << ++lineNumber << ": " << solve(l) << std::endl;
  }
  return 0;
}
