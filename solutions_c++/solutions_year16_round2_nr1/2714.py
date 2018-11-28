#include<bits/stdc++.h>
using namespace std;

const char *str[10] = {"ZERO","ONE","TWO",
		       "THREE","FOUR","FIVE",
		       "SIX","SEVEN","EIGHT","NINE"};
const char uni[10] = {'Z','O','W',
		      'R','U','F',
		      'X','S','G','E'};

int check[30];
int res[10];

void solve(string s){
  fill(check,check+30,0);
  fill(res,res+10,0);
  for(int i = 0;i < (int)s.size();++i){
    ++check[s[i]-'A'];
  }
  for(int i = 0;i < 10;i += 2){
    res[i] += check[uni[i] - 'A'];
    for(int j = 0;str[i][j] != '\0';++j){
      check[str[i][j] - 'A'] -= res[i];
    }
  }
  for(int i = 1;i < 10;i += 2){
    res[i] += check[uni[i] - 'A'];
    for(int j = 0;str[i][j] != '\0';++j){
      check[str[i][j] - 'A'] -= res[i];
    }
  }
}

int main(void){
  int n ;
  cin >> n;
  for(int i = 0;i < n;++i){
    string s;
    cin >> s;
    solve(s);
    cout << "Case #" << i+1 << ": ";
    for(int i = 0;i < 10;++i){
      for(int j = 0;j < res[i];++j){
	cout << i;
      }
    }
    cout << endl;
  }
  return 0;
}
