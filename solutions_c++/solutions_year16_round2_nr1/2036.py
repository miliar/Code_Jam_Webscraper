#include <string>
#include <iostream>

using namespace std;

int numbs[10];
int leathers[100];

int main(){
  int ncases;

  cin >> ncases;
  for(int i = 0; i < ncases; i++){
    string cur;

    cin >> cur;
    for(int j = 0; j < 10 ;j++){
     numbs[j] = 0;
    }
    for(int j = 0; j < 100 ;j++){
     leathers[j] = 0;
    }

    for(int j = 0; j < cur.size(); j ++){
      leathers[cur[j] - 'A'] ++;
    }
    leathers['T' - 'A'] -= leathers['W' - 'A'];
    leathers['O' - 'A'] -= leathers['W' - 'A'];
    numbs[2] = leathers['W' - 'A'];
    leathers['I' - 'A'] -= leathers['X' - 'A'];
    leathers['S' - 'A'] -= leathers['X' - 'A'];
    numbs[6] = leathers['X' - 'A'];
    leathers['E' - 'A'] -= leathers['S' - 'A'];
    leathers['V' - 'A'] -= leathers['S' - 'A'];
    leathers['E' - 'A'] -= leathers['S' - 'A'];
    leathers['N' - 'A'] -= leathers['S' - 'A'];
    numbs[7] = leathers['S' - 'A'];
    leathers['F' - 'A'] -= leathers['V' - 'A'];
    leathers['I' - 'A'] -= leathers['V' - 'A'];
    leathers['E' - 'A'] -= leathers['V' - 'A'];
    numbs[5] = leathers['V' - 'A'];
    leathers['E' - 'A'] -= leathers['G' - 'A'];
    leathers['I' - 'A'] -= leathers['G' - 'A'];
    leathers['H' - 'A'] -= leathers['G' - 'A'];
    leathers['T' - 'A'] -= leathers['G' - 'A'];
    numbs[8] = leathers['G' - 'A'];
    leathers['T' - 'A'] -= leathers['H' - 'A'];
    leathers['R' - 'A'] -= leathers['H' - 'A'];
    leathers['E' - 'A'] -= leathers['H' - 'A'];
    leathers['E' - 'A'] -= leathers['H' - 'A'];
    numbs[3] = leathers['H' - 'A'];
    leathers['O' - 'A'] -= leathers['F' - 'A'];
    leathers['U' - 'A'] -= leathers['F' - 'A'];
    leathers['R' - 'A'] -= leathers['F' - 'A'];
    numbs[4] = leathers['F' - 'A'];
    leathers['Z' - 'A'] -= leathers['R' - 'A'];
    leathers['E' - 'A'] -= leathers['R' - 'A'];
    leathers['O' - 'A'] -= leathers['R' - 'A'];
    numbs[0] = leathers['R' - 'A'];
    leathers['N' - 'A'] -= leathers['O' - 'A'];
    leathers['E' - 'A'] -= leathers['O' - 'A'];
    numbs[1] = leathers['O' - 'A'];
    numbs[9] = leathers['I' - 'A'];
    cout << "Case #" << i + 1 << ": "; 
    for(int a = 0; a < 10; a ++){
      for(int b = 0; b < numbs[a]; b++){
        cout << a;
      }
    }
    cout << endl;
    }

}




