#include<iostream>
#include<sstream>
#include<algorithm>
#include<map>
#include<set>
#include<queue>
#include<complex>
#include<cstdio>
#include<cstdlib>
#include<cstring>
// #define DEBUG

using namespace std;

// typedef pair<int,int>P;
// typedef complex<double>P;

typedef long long int ll;
typedef unsigned long long int ull;

const int INF = 1e9;
const double EPS=1e-9;

const int ONE = 1;
const int I = 2;
const int J = 3;
const int K = 4;

const int table[5][5] = {{0,   0,    0,    0,     0},
			 {0, ONE,    I,    J,     K},
			 {0, I  , -ONE,    K,    -J},
			 {0, J  ,   -K, -ONE,     I},
			 {0, K  ,    J,   -I,  -ONE},};

const int check_list[3] = {I,K,-ONE};

bool func(){
  int L,X;
  cin >> L >> X;
  string str;
  cin >> str;
  
  int state = 0;
  int num = ONE;
  
  for(int i = 0 ; i < X ; i++){
    for(int j = 0 ; j < L ; j++){
      bool minus_flag = (num < 0);
      num = abs(num);
      int id;
      if(str[j] == 'i')id = I;
      else if(str[j] == 'j')id = J;
      else if(str[j] == 'k')id = K;
      num = table[num][id] * (minus_flag?-1:1);
      if(state < 2 && num == check_list[state])state++;

      //      cout << "state = " << state << " num = " << num << endl;

    }
  }
  return state == 2 && num == check_list[state];
}

int main(int argc, char *argv[])
{
  int T;
  cin >> T;
  for(int i = 1 ; i <= T ; i++){
    cout << "Case #" << i << ": " << (func()?"YES":"NO") << endl;
  }
  return 0;
}
