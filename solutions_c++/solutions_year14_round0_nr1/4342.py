#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void readLine(vector<int>& out, int r)
{
  int tmp;
  out.resize(4,0);
  for (int i = 0; i < 4 * (r-1); ++i)
    cin >> tmp;

  for (int i = 0; i < 4; ++i)
    cin >> out[i];

  for (int i = 0; i < 4 * (4-r); ++i)
    cin >> tmp;

  sort(out.begin(), out.end());
}

int main()
{
  int C = 1;
  int N;

  cin >> N;

  while ( C <= N ) {
    int row;
    vector<int> line1, line2, intersect(4,0);

    cin >> row;
    readLine(line1, row);
    cin >> row;
    readLine(line2, row);
    std::vector<int>::iterator it = set_intersection(line1.begin(), line1.end(),
        line2.begin(), line2.end(), intersect.begin());
    intersect.resize(it - intersect.begin());
    cout << "Case #" << C << ": ";
    if ( intersect.size() == 1 )
      cout << intersect[0];
    else if ( intersect.size() == 0)
      cout << "Volunteer cheated!";
    else
      cout << "Bad magician!";
    cout << endl;
    ++C;
  }
}
