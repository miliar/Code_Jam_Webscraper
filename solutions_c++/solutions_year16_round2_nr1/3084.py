#include <cstdlib>
#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <stack>
#include <utility>
#include <queue>
#include <list>
#include <sstream>

#define PI 3.14159265

using namespace std;

void fill_chars(map<char, int>& m)
{
  m['Z'] = 0;
  m['E'] = 0;
  m['R'] = 0;
  m['O'] = 0;
  m['N'] = 0;
  m['T'] = 0;
  m['W'] = 0;
  m['H'] = 0;
  m['F'] = 0;
  m['U'] = 0;
  m['I'] = 0;
  m['V'] = 0;
  m['X'] = 0;
  m['G'] = 0;
}

bool all_leters_used(map<char,int> &m)
{
  if ((m['O'] == 0) && (m['N'] == 0) && (m['E'] == 0) && 
      (m['R'] == 0) && (m['H'] == 0) && (m['T'] == 0) && 
      (m['F'] == 0) && (m['I'] == 0) && (m['V'] == 0) && (m['S'] == 0))
    return true;
  else
    return false;
}

int min(int a, int b)
{
  return a < b ? a : b;
}



void print_answer(int* numbers)
{
  for (int i = 0; i < 10; ++i)
    for (int j = 0; j < numbers[i]; ++j)
      cout << i;
}



int main(int argc, const char *argv[])
{
  ios::sync_with_stdio(false);
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i)
  {
    string s;
    cin >> s;
    map<char, int> m;
    fill_chars(m);
    for (int j = 0; j < s.size(); ++j)
      m[s[j]] += 1;
    int numbers[10] = { 0,0,0,0,
                        0,0,0,0,
                        0,0};
    // now remove all this letters

    numbers[0] = m['Z'];
    m['E'] -= m['Z'];
    m['R'] -= m['Z'];
    m['O'] -= m['Z'];
    m['Z'] = 0;

    numbers[2] = m['W'];
    m['T'] -= m['W'];
    m['O'] -= m['W'];
    m['W'] = 0;

    numbers[4] = m['U'];
    m['F'] -= m['U'];
    m['O'] -= m['U'];
    m['R'] -= m['U'];
    m['U'] = 0;

    numbers[6] = m['X'];
    m['S'] -= m['X'];
    m['I'] -= m['X'];
    m['X'] = 0;

    numbers[8] = m['G'];
    m['E'] -= m['G'];
    m['I'] -= m['G'];
    m['H'] -= m['G'];
    m['T'] -= m['G'];
    m['G'] = 0;
    // now try to distribute letters amongst  other digits
    // we now know that one's letter are unique amongst odd digits
    numbers[1] = m['O'];
    m['N'] -= m['O'];
    m['E'] -= m['O'];
    m['O'] = 0;
    // now 3
    numbers[3] = m['T'];
    m['E'] -= 2*m['T'];
    m['T'] = 0;
    m['H'] = 0;
    m['R'] = 0;
    // now 5
    numbers[5] = m['F'];
    m['I'] -= m['F'];
    m['V'] -= m['F'];
    m['E'] -= m['F'];
    // now 7
    numbers[7] = m['S'];
    m['E'] -= 2*m['S'];
    m['V'] -= m['S'];
    m['N'] -= m['S'];

    // now 9
    numbers[9] = m['E'];
    cout << "Case #" << (i+1) << ": ";
    print_answer(numbers);
    cout << endl;
  }
  return 0;
}


