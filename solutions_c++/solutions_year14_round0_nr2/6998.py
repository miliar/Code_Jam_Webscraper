#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>

using namespace std;

#define FOR(i, n) for(int i = 0 ; i < n ; ++i)
#define FORE(i, n) for(int i = 0 ; i <= n ; ++i)

struct problem {
  double cost, extra, mark; //C, F, X
};

struct option {
  int farm_number;
  vector<double> times;
};

vector<problem> readProblem() {
  ifstream fin("B-large.in");
  vector<problem> problems;
  int t;

  fin >> t;

  FOR(i, t) {
    problem p;
    fin >> p.cost >> p.extra >> p.mark;
    problems.push_back(p);
  }

  fin.close();
  return problems;
}

double totaltime(option o) {
  int size = o.times.size();
  double total = 0.0f;
  
  FOR(i, size) {total += o.times[i];}

  return total;
}

double solve(problem p) {
  option base, next;

  next.farm_number = 0;
  next.times.push_back((double) (p.mark / 2));

  double cookies_per_second;
  do {
    base = next;
    cookies_per_second = 2;

    next.farm_number = base.farm_number + 1;
    next.times.clear();

    FOR(i, next.farm_number) {
      next.times.push_back((double) (p.cost / cookies_per_second));
      cookies_per_second += p.extra;
    }

    next.times.push_back((double) (p.mark / cookies_per_second));
  } while(totaltime(next) < totaltime(base));

  return totaltime(base);
}


int main() {
  vector<problem> problems = readProblem();
  int size = problems.size();
  ofstream fout("B-large.out");
  
  fout.setf( ios::fixed, ios::floatfield );

  FOR(i, size) {
    fout << "Case #" << i + 1 << ": " << setprecision(7) << solve(problems[i]) << endl;
  }

  fout.close();
}