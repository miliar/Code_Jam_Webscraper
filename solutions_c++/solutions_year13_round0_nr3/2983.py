#include <iostream>
#include <vector>
#include <set>
#include <cmath>

using namespace std;

typedef long long lint;

vector<lint> p10;

int digits_number(lint v)
{
  return (lint)floor(log10((double)(v))) + 1;
}

bool is_parlin(lint v)
{
  if (v < 10) return true;

  if (p10.empty()) {
    int t = 1;
    for (int i = 0; i < 16; ++i) {
      p10.push_back(t);
      t *= 10;
    }
  }

  lint digits = digits_number(v);
  //cout << v << " is " << digits << " digits" << endl;
  for (int i = 0; i*2+1 < digits; ++i) {
    int low = (v / p10[i]) % 10;
    int high = (v / p10[digits - i - 1]) % 10;
    //cout << "high: " << high << " and low: " << low << endl;
    if (low != high) return false;
  }

  return true;
}

lint gen_parlin(lint v, int d)
{
  if (v < 0) { // 挟む数字がない
    return d*10 + d;
  }
  
  // d v d
  lint digits = digits_number(v);
  return (d * pow(10.0, (double)(digits)) + v) * 10 + d;
}

int main()
{
  int T;
  cin >> T;

  set<int> parlin;
  set<int> parlin_cur;
  set<int> parlin_p;
  set<int> parlin_pp;
  for (int i = 0; i < 10; ++i) {
    parlin_p.insert(i);
    if (i) {
      parlin.insert(i);
      parlin_cur.insert(i*10+i);
      parlin.insert(i*10+i);
    }
  }
  
  for (int i = 1; i < 6; ++i) { // 10^i
    parlin_pp = parlin_p;
    parlin_p = parlin_cur;
    parlin_cur.clear();
    for (int j = 1; j < 10; ++j) {
      for (set<int>::iterator it = parlin_pp.begin();
	   it != parlin_pp.end(); ++it) {
	lint tmp = gen_parlin(*it, j);
	//cout << "gen: " << *it << " -> " << tmp << endl;
	parlin_cur.insert(tmp);
      }
    }
    for (set<int>::iterator it = parlin_cur.begin();
	   it != parlin_cur.end(); ++it)
      parlin.insert(*it);
  }

  // for (set<int>::iterator it = parlin.begin();
  //      it != parlin.end(); ++it) {
  //   cout << *it << endl;
  // }

  vector<lint> fsq;
  for (set<int>::iterator it = parlin.begin();
       it != parlin.end(); ++it) {
    const lint p = *it;
    //cout << p*p << endl;
    if (is_parlin(p*p)) {
      // cout << p << " -> " << p*p << endl;
      fsq.push_back(p*p);
    }
  }

  // for (vector<lint>::iterator it = fsq.begin();
  //      it != fsq.end(); ++it) {
  //   cout << *it << endl;
  // }

  // cout << "!!!" << endl;
  
  for (int cs = 1; cs <= T; ++cs) {
    lint A, B;
    cin >> A >> B;

    vector<lint>::iterator it1 = lower_bound(fsq.begin(), fsq.end(), A);
    vector<lint>::iterator it2 = upper_bound(fsq.begin(), fsq.end(), B);
    cout << "Case #" << cs << ": " << distance(it1, it2) << endl;
  }
  
  return 0;
}
