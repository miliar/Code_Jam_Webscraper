#include<fstream>
#include<iostream>
#include<map>
using namespace std;

void showMapContent(map<int, int>& dict, char endOfLine = '\n')
{
  for (map<int, int>::iterator it = dict.begin();
      it != dict.end(); ++ it)
  {
    cout << '(' << it->first << ',' << it->second << ')' << '\t';
  }
  cout << endOfLine;
}

int getMinimalMinutes(map<int, int>& dict)
{
  showMapContent(dict);

//  cin.get();

  int ret = dict.rbegin()->first;

  if (ret == 1) return ret;
/*  
  map<int, int> dictAfterEat;
  dictAfterEat.clear();
  for (map<int, int>::iterator it = dict.begin();
      it != dict.end(); ++ it)
  {
    if (it->first > 1)
      dictAfterEat[it->first - 1] = it->second;
  }

  cout << "eat one" << endl;
  showMapContent(dict, '>');
  int eat_ret = getMinimalMinutes(dictAfterEat) + 1;
  if (ret > eat_ret)  ret = eat_ret;
 
  cout << "split the max" << endl;
  showMapContent(dict, '>');
*/
  // key = p + q.
  int key = dict.rbegin()->first;
  int val = dict.rbegin()->second;
  int p, q;

  for (p = 1; p <= key / 2; p ++)
  {
    q = key - p;
    map<int, int> tmpdict(dict);
    tmpdict.erase(key);
    tmpdict[p] += val;
    tmpdict[q] += val;

    int split_ret = getMinimalMinutes(tmpdict) + val;
    cout << split_ret << endl;
    if (ret > split_ret)  ret = split_ret;
  }

  return ret;

}

int main()
{
  ifstream fin("pB.in");
  ofstream fout("pB.out");

  map<int, int> dict;

  int T, t;

  fin >> T;
 
  for (t = 1; t <= T; t ++)
  {
    dict.clear();
    
    int D;
    fin >> D;
    for (int i = 0; i < D; i ++)
    {
      int p;
      fin >> p;
      dict[p] ++;
    }

    int ans = getMinimalMinutes(dict);

    fout << "Case #" << t << ": " << ans << endl;

  }

  return 0;
}
