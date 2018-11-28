#include <iostream>
#include <string>
#include <vector>
#define sz(x) ((int)((x).size()))
#define pb push_back
using namespace std;

int tn, n, m;
vector<int> a;
int d[4][4] = {{0, 1, 2, 3},
               {1, 0, 3, 2},
               {2, 3, 0, 1},
               {3, 2, 1, 0}};
int p[4][4] = {{1, 1, 1, 1},
               {1,-1, 1,-1},
               {1,-1,-1, 1},
               {1, 1,-1,-1} };

void printqa(int state, int sign) {
  if (sign < 0)
    cout << "-";
  if (state == 0)
    cout << "1";
  if (state == 1)
    cout << "i";
  if (state == 2)
    cout << "j";
  if (state == 3)
    cout << "k";
  cout<< endl;
}

int main(int argc, char *argv[])
{
  cin >> tn;
  for (int ti = 1; ti <= tn; ++ti) {
    cin >> n >> m;
    a.clear();
    string tmp;
    cin >> tmp;
    for (int k = 0; k < m; ++k) {
      for (int i = 0; i < n; ++i) {
        if (tmp[i] == 'i')
          a.pb(1);
        else if (tmp[i] == 'j')
          a.pb(2);
        else if (tmp[i] == 'k')
          a.pb(3);
      }
    }

    n *= m;
    int flag= 0;
    int state = 0;
    int sign = 1;
    for (int i = 0; i < n; ++i) {
      sign *= p[state][a[i]];
      state = d[state][a[i]];
      // printqa(state,sign);
      if (state == 1 && sign == 1) {
        int state2 = 0;
        int sign2 = 1;
        int jflag = 0;
        for (int j = i+1; j < n; ++j) {
          sign2 *= p[state2][a[j]];
          state2 = d[state2][a[j]];
          // cout << "\t";
          // printqa(state2,sign2);
          if (sign2 == 1 && state2 == 2)
            jflag = 1;
        }
        if (state2 == 1 && sign2 == 1 && jflag == 1) {
          flag = 1;
          break;
        }
      }
    }
    if (flag == 1) {
      cout << "Case #" << ti << ": YES" << endl;
    } else {
      cout << "Case #" << ti << ": NO" << endl;
    }

  }
  return 0;
}
