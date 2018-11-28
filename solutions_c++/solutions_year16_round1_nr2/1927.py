#include <bits/stdc++.h>

using namespace std;

class Comparator {
public:
  int position;
  Comparator(int position) {
    this->position = position;
  }
  bool operator()(const vector<int>& lhs, const vector<int>& rhs) const
  {
    return lhs[position] < rhs[position];
  }
};

void solveCase()
{
  int N;
  cin >> N;

  vector<vector<int> > data;
  data = vector<vector<int> >(N*2-1);
  for (int i=0; i<N*2-1; i++) {
    data[i] = vector<int>(N);
    for (int j=0; j<N; j++) {
      cin >> data[i][j];
    }
  }

  vector<pair<vector<int>, vector<int> > > pairs;
  vector<int> first[50];
  vector<int> second[50];
  int missing;

  for (int i=0; i<N; i++) {
    sort(data.begin(), data.end(), Comparator(i));
    if (data.size() < 2 || data[0][i] != data[1][i]) {
      missing = i;
      first[i] = *data.begin();
      data.erase(data.begin());
    } else {
      first[i] = *data.begin();
      second[i] = *(data.begin()+1);
      data.erase(data.begin());
      data.erase(data.begin());
    }
  }

  for (int i=0; i<N; i++) {
    if (i == missing) {
      printf("%d ", first[i][i]);
    } else {
      printf("%d ", first[missing][i] == first[i][missing] ? second[i][missing] : first[i][missing]);
    }
  }
  printf("\n");
}

int main ()
{
  int T;
  cin >> T;
  for (int i=1; i<=T; i++) {
    printf("Case #%d: ", i);
    solveCase();
  }
  return 0;
}
