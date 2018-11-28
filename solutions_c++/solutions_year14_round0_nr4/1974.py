#include <iostream>
#include <algorithm>
#include <iterator>
#include <list>
#include <vector>
#include <cmath>

using namespace std;

int opti_dec_war(const vector<double>& naomi, const vector<double>& ken)
{
  int r = 0;
  list<double> naomi_l;
  list<double> ken_l;
  copy(naomi.cbegin(), naomi.cend(), back_insert_iterator<list<double>>(naomi_l));
  copy(ken.cbegin(), ken.cend(), back_insert_iterator<list<double>>(ken_l));
  while (!ken_l.empty() && !naomi_l.empty())
  {
    if (ken_l.back() < naomi_l.back())
    {
      ++r;
      ken_l.pop_back();
    }
    else
      ken_l.pop_front();
    naomi_l.pop_back();
  }
  return r;
}

int opti_war(const vector<double>& naomi, const vector<double>& ken)
{
  int r = 0;
  auto it_n = naomi.cbegin();
  auto it_k = ken.cbegin();
  while (it_n != naomi.cend() && it_k != ken.cend())
  {
    if (*it_k < *it_n)
      ++it_n;
    else
      ++it_k;
    r = max(r, static_cast<int>(distance(naomi.cbegin(), it_n)-distance(ken.cbegin(), it_k)));
  }
  return r;
}

int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i)
  {
    int N;
    cin >> N;
    vector<double> naomi;
    vector<double> ken;
    copy_n(istream_iterator<double>(cin), N, back_insert_iterator<vector<double>>(naomi));
    copy_n(istream_iterator<double>(cin), N, back_insert_iterator<vector<double>>(ken));
    sort(naomi.begin(), naomi.end(), greater<double>());
    sort(ken.begin(), ken.end(), greater<double>());
    cout << "Case #" << i << ": " << opti_dec_war(naomi, ken) << " " << opti_war(naomi, ken) << endl;
  }
  return 0;
}
