#include <iostream>
#include <algorithm>
#include <sstream>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <set>
#include <map>
#include <list>
#include <unordered_set>
#include <unordered_map>
#include <limits>
#include <stdexcept>

#include "prettyprint.hpp"

using namespace std;

typedef long long int ll;

bool isVowel(char c)
{
  switch (c) {
    case 'a':
    case 'e':
    case 'i':
    case 'o':
    case 'u':
      return true;
    default:
      return false;
  }
}

int cost(int travel, int n) {
  int rv = 0;
  for (int i = 1; i <= travel; ++i) {
    rv += n - i;
  }
  return rv;
}

struct passenger
{
  int id;
  int fel;
  int le;
};

ostream&operator<<(ostream&o, const passenger&p) 
{
  o << "id:"<<p.id<< ",fel:"<<p.fel<<"le:"<<p.le;
  return o;
}

struct VarComp
{
  bool operator()(const passenger& p1, const passenger& p2)
  {
    return p1.fel < p2.fel
      ||
      (p1.fel == p2.fel && p1.id < p2.id);
  }
};
struct FentComp
{
  bool operator()(const passenger& p1, const passenger& p2)
  {
    return p1.le < p2.le
      ||
      (p1.le == p2.le && p1.id < p2.id);
  }
};

int koltsegszamol(const vector<passenger> &v, int n) {
  int koltseg = 0;
  for (auto &p:v) {
    koltseg += cost(p.le-p.fel, n);
    koltseg %= 1000002013;
  }
  return koltseg;
}

int main() {

  int tn;
  cin >> tn;

  for (int ti = 0; ti < tn; ti++) {

    int n = -1;
    int m = -1;
    cin >> n >> m;

    if (-1 == n || -1 == m) {
      cerr << "ERROR" << endl;
      exit(1);
    }

    vector<passenger> v;
    vector<passenger> utazott;

    int id = 0;
    for (int i = 0; i < m; ++i) {
      passenger p;
      int count;
      cin >> p.fel >> p.le >> count;
      for (int j = 0; j < count; ++j) {
        p.id = id++;
        v.push_back(p);
      }
    }

    set<passenger, VarComp> varakozik;
    for (auto &p: v) {
      varakozik.insert(p);
    }

    //cerr << v << endl;
    //cerr << varakozik << endl;

    std::set<passenger, FentComp> fentvan;
    for (int s = 0; s <= n; ++s) {
      //cerr << "station " << s << endl;
      {
      //felszallas
      auto it = varakozik.begin();
      while (it != varakozik.end() && it->fel == s) {
        //cerr << "  felszall " << it->id << " le: " << it->le << endl;

        //felszall
        fentvan.insert(*it);

        varakozik.erase(it);
        it = varakozik.begin();
      }
      }
      //cerr << "  fentvan:" << fentvan << endl;

      //leszallas
      {
      auto it = fentvan.begin();
      while (it != fentvan.end() && it->le == s) {
        //cerr << "  leszall " << it->id << endl;
        //cserel
        //aki a legkesobb szallt fel
        int maxfelszall = it->fel;
        auto maxfelszallhely = it;
        for (auto itt = fentvan.begin();itt!=fentvan.end();++itt) {
          if (maxfelszall < itt->fel) {
            maxfelszall = itt->fel;
            maxfelszallhely = itt;
          }
        }
        swap(
            const_cast<passenger&>(*maxfelszallhely).fel,
            const_cast<passenger&>(*it).fel
            );

        //leszall
        utazott.push_back(*it);

        fentvan.erase(it);
        it = fentvan.begin();
      }
      }
    }

    int x = koltsegszamol(v, n);
    int y = koltsegszamol(utazott, n);
    //cerr << "  utazott:" << utazott << endl;
    int result = (1000002013 + x - y) % 1000002013;

    cout << "Case #" << ti+1 << ": " << result << endl;
    cerr << "Case #" << ti+1 << ": " << result << endl;

  }
}

