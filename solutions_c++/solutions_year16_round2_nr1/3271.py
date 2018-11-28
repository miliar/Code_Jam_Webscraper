#include<cstdio>
#include<map>
#include<string>
#include<cstring>
#include<algorithm>

using namespace std;

//           0    6    7    5   4     2    1   8    3    9
char x[] = {'Z', 'X', 'S', 'V', 'F', 'W', 'O', 'G', 'R', 'I'};
map<char, string> xx;
map<char, char> yy;

int main()
{
  xx['Z'] = "ZERO";
  xx['X'] = "SIX";
  xx['S'] = "SEVEN";
  xx['V'] = "FIVE";
  xx['F'] = "FOUR";
  xx['W'] = "TWO";
  xx['O'] = "ONE";
  xx['G'] = "EIGHT";
  xx['R'] = "THREE";
  xx['I'] = "NINE";
  yy['Z'] = '0';
  yy['X'] = '6';
  yy['S'] = '7';
  yy['V'] = '5';
  yy['F'] = '4';
  yy['W'] = '2';
  yy['O'] = '1';
  yy['G'] = '8';
  yy['R'] = '3';
  yy['I'] = '9';

  int t = 0;
  scanf("%d", &t);
  for (int i = 1; i <= t; i++) {
    map<char, int> mymap;
    char buf[2010] = {0};
    scanf("%s", buf);
    int len = strlen(buf);
    for (int j = 0; j < len; j++) {
      mymap[buf[j]]++;
    }

    string res;
    for (int j = 0; j < 10; j++) {
      char ch = x[j];
      int count = mymap[ch];
      if (count > 0) { 
        for (int k = 0; k < count; k++)
          res += yy[ch];
      
        int len = xx[ch].length();
        for (int k = 0; k < len; k++) {
          mymap[xx[ch][k]] -= count;
        }
      }
    }

    sort(res.begin(), res.end());
    printf("Case #%d: %s\n", i, res.c_str());
  }
}
