#include <iostream>
#include <string>
using namespace std;

#define LIM
#define MOD
#define INF

typedef long long int ll;


int N, R, P, S;



string answers[4][13];
int numbers[4][13][4];

int convert(char ch) {
  if(ch == 'P') return 0;
  if(ch == 'R') return 1;
  if(ch == 'S') return 2;
  return 3;
}

void populateNumbers(string s, int a, int n) {
  int s_count, p_count, r_count;
  s_count = p_count = r_count = 0;
  for(int i = 0; i < (int) s.length(); i++) {
    if(s[i] == 'P') p_count++;
    if(s[i] == 'S') s_count++;
    if(s[i] == 'R') r_count++;
  }
  numbers[a][n][0] = p_count;
  numbers[a][n][1] = r_count;
  numbers[a][n][2] = s_count;
}

void clearNumbers() {
  int i, j, k;
  for(i = 0; i < 4; i++) {
    for(j = 0; j < 13; j++) {
      for(k = 0; k < 4; k++) {
	numbers[i][j][k] = 0;
      }
    }
  }
}

void work(int index) {

  cin >> N >> R >> P >> S;

  int i, j;
  int flag = 0;
  for(i = 0; i < 3; i++) {
    if(numbers[i][N][0] == P && numbers[i][N][1] == R && numbers[i][N][2] == S) {
      flag = 1;
      break;
    }
  }
  

  
  cout << "Case #" << index << ": ";
  if(flag == 0) {
    cout << "IMPOSSIBLE";
  }
  else {
    cout << answers[i][N];
  }
  cout << endl;
}

int main() {

  int i, j;
  clearNumbers();
  answers[0][0] = "P";
  numbers[0][0][0] = 1;
  answers[1][0] = "R";
  numbers[1][0][1] = 1;
  answers[2][0] = "S";
  numbers[2][0][2] = 1;

  answers[0][1] = "PR";
  numbers[0][1][0] = 1;
  numbers[0][1][1] = 1;

  answers[1][1] = "RS";
  numbers[1][1][1] = 1;
  numbers[1][1][2] = 1;

  answers[2][1] = "PS";
  numbers[2][1][0] = 1;
  numbers[2][1][2] = 1;

  char c1, c2;
  int n1, n2;
  for(i = 2; i < 13; i++) {
    for(j = 0; j < 3; j++) {
      c1 = answers[j][1][0];
      c2 = answers[j][1][1];
      n1 = convert(c1);
      n2 = convert(c2);
      if(answers[n1][i - 1].compare(answers[n2][i - 1]) > 0) {
	answers[j][i] = answers[n2][i - 1] + answers[n1][i - 1];
      }
      else {
	answers[j][i] =  answers[n1][i - 1] + answers[n2][i - 1];
      }
      populateNumbers(answers[j][i], j, i);
      //cout << "answers " << i << " " << j << " " << answers[j][i] << endl;
    }
    
  }
  
  
  
  
  
  int T;
  cin >> T;

  for(i = 1; i <= T; i++) work(i);
  return 0;
}
