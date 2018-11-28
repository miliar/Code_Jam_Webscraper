#include<fstream>
#include<vector>
using namespace std;
int main()
  {
  int T;
  ifstream f("B-large.in");
  ofstream g("output.txt");
  f >> T;
  vector<int> rmax, cmax, res(T);
  vector<vector<int>> field;
  int M, N;
  for(int i = 0 ; i < T ; ++i)
    {
    
    f >> N >> M;
    rmax.resize(N);
    cmax.resize(M);

    field.resize(N);
    for(int j = 0; j < N; ++j)
      {
      field[j].resize(M);
      rmax[j] = -1;
      }

    for(int j = 0; j < M; ++j)
      cmax[j] = -1;

    for(int j = 0; j < N; ++j)
      for(int k = 0; k < M; ++k)
        {
        f >> field[j][k];

        if(field[j][k] > rmax[j])
          rmax[j] = field[j][k];

        if(field[j][k] > cmax[k])
          cmax[k] = field[j][k];
        }
    
    for(int j = 0; j < N; ++j)
      for(int k = 0; k < M; ++k)
        if(field[j][k] < rmax[j] && field[j][k] < cmax[k])
          res[i] = 1;
    }

  for(int i = 0 ; i < T ; ++i)
    {
    g << "Case #" << i + 1 << ": ";
    if(res[i] == 0)
      g << "YES\n";
    else
      g << "NO\n";
    }

  return 0;
  }