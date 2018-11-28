#include <bits/stdc++.h>

using namespace std;

int a[26];
int op[100];

int main(){
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int t;
  string s;

  cin >> t;

  for(int j=0;j<t;j++){
    cin >> s;
    fill(a,a+26,0);
    fill(op,op+100,0);
    int k = 0;
    for(int i=0;i<s.size();i++){
      a[s[i] - 'A'] += 1;
    }
    int n = a['Z' - 'A'];
    for(int i=0;i<n;i++){
      op[k++] = 0;
      a['Z' - 'A']--;
      a['E' - 'A']--;
      a['R' - 'A']--;
      a['O' - 'A']--;
    }
    n = a['W' - 'A'];
    for(int i=0;i<n;i++){
      op[k++] = 2;
      a['T' - 'A']--;
      a['W' - 'A']--;
      a['O' - 'A']--;
    }
    n = a['U' - 'A'];
    for(int i=0;i<n;i++){
      op[k++] = 4;
      a['F' - 'A']--;
      a['O' - 'A']--;
      a['U' - 'A']--;
      a['R' - 'A']--;
    }
    n = a['F' - 'A'];
    for(int i=0;i<n;i++){
      op[k++] = 5;
      a['F' - 'A']--;
      a['I' - 'A']--;
      a['V' - 'A']--;
      a['E' - 'A']--;
    }
    n = a['X' - 'A'];
    for(int i=0;i<n;i++){
      op[k++] = 6;
      a['S' - 'A']--;
      a['I' - 'A']--;
      a['X' - 'A']--;
    }
    n = a['V' - 'A'];
    for(int i=0;i<n;i++){
      op[k++] = 7;
      a['S' - 'A']--;
      a['E' - 'A']--;
      a['V' - 'A']--;
      a['E' - 'A']--;
      a['N' - 'A']--;
    }
    n = a['G' - 'A'];
    for(int i=0;i<n;i++){
      op[k++] = 8;
      a['E' - 'A']--;
      a['I' - 'A']--;
      a['G' - 'A']--;
      a['H' - 'A']--;
      a['T' - 'A']--;
    }
    n = a['I' - 'A'];
    for(int i=0;i<n;i++){
      op[k++] = 9;
      a['N' - 'A']--;
      a['I' - 'A']--;
      a['N' - 'A']--;
      a['E' - 'A']--;
    }
    n = a['O' - 'A'];
    for(int i=0;i<n;i++){
      op[k++] = 1;
      a['O' - 'A']--;
      a['N' - 'A']--;
      a['E' - 'A']--;
    }
    n = a['T' - 'A'];
    for(int i=0;i<n;i++){
      op[k++] = 3;
      a['T' - 'A']--;
      a['H' - 'A']--;
      a['R' - 'A']--;
      a['E' - 'A']--;
      a['E' - 'A']--;
    }
    sort(op,op+k);
    cout << "Case #" << j+1 << ": ";
    for(int i=0;i<k;i++)
      cout << op[i];
    cout << '\n';
  }

  return 0;
}
