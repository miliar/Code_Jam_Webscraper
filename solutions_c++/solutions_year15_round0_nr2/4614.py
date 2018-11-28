#include <iostream>
#include <fstream>
#include <vector>
#include <climits>

using namespace std;

void PrintVector(const vector<int> &v) {
  cout << '[';
  for (int i = 0; i < v.size(); i++) {
    cout << v[i] << ", ";
  }
  cout << ']' << endl;
}

int NextHighest(const vector<int> &a, int tail) {
  while (tail > 0) {
    tail--;
    if (a[tail] != 0) {
      return tail;
    }
  }
  return 0;
}

int Cost(vector<int> a, int tail, int amount, int cost);

int MinCost(const vector<int>& a, int tail, int cost) {
  int rest = (tail)/2;
  int sol = cost + tail;
  for (int i = 2; i <= rest; ++i) {
    sol = min(sol, Cost(a, tail, i, cost));
  }
  return sol;
}

int pc(int v, int p) {
  cout << "cost @ " << p << ": " << v << endl;
  return v;
}

int Cost(vector<int> a, int tail, int amount, int cost) {
  PrintVector(a);
  cout << "tail: " << tail << "; amount: " << amount << "; cost: " << cost << endl;
  if (tail < 4) {
    return pc(tail + cost,1);
  }
  int rest = tail - amount;
  if (rest <= 0) {
    return pc(cost + tail,2);
  }
  a[amount] += a[tail];
  a[rest] += a[tail];  
  int mv = a[tail];
  a[tail] = 0;
  int next_highest = NextHighest(a, tail);
  int move_cost = MinCost(a, next_highest, cost + mv);
  return pc(move_cost,3);
}

int main(int argc, char **argv) {

  ifstream in(argv[1]);
  ofstream out(argv[2]);

  int num_cases = 0;
  in >> num_cases;

  for (int c = 1; c <= num_cases; ++c) {
    int num_pan_people = 0;
    in >> num_pan_people;
    // cout << num_pan_people << endl;
    vector<int> a;
    while (num_pan_people-- > 0) {
      int num_pancakes = 0;
      in >> num_pancakes;
      if (num_pancakes >= a.size()) {
        a.resize(num_pancakes + 1, 0);
      }
      a[num_pancakes]++;
    }
    int m = MinCost(a, a.size()-1, 0);
    out << "Case #" << c << ": " << m << endl;
  }

  return 0;
}
