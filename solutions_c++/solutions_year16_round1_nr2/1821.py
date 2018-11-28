
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

void solve(int N, int mat[100][50], ostream& out)
{
  map<int, int> nums;
  vector<int> res;
  for (int i = 0; i < 2*N-1; i++)
  {
    for (int j = 0; j < N; j++)
    {
      nums[mat[i][j]]++;
    }
  }
  for (auto e : nums)
  {
    if (e.second % 2 == 1)
    {
      res.push_back(e.first);
    }
  }
  sort(res.begin(), res.end());
  for (auto n : res) out << n << " ";
}

void run(istream& in, ostream& out)
{
  int T; in >> T;
  for (int t = 1; t <= T; t++)
  {
    int N; in >> N;
    int mat[100][50];
    for (int i = 0; i < 2*N-1; i++)
    {
      for (int j = 0; j < N; j++)
      {
        in >> mat[i][j];
      }
    }
    out << "Case #" << t << ": ";
    solve(N, mat, out);
    out << endl;
  }
}

int main()
{
  ifstream fin("B-large.in");
  ofstream fout("B-large.out");
  run(fin, fout);
}

