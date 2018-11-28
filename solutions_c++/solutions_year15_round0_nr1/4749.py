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

int func(){
  int k;
  cin >> k;
  int ret = 0;
  int sum = 0;

  string str;
  cin >> str;

  for(int i = 0 ; i <= k ; i++){
    int num = str[i]-'0';
    if(sum < i && num){
      ret += (i - sum);
      sum = i;
    }
    sum += num;
  }
  return ret;
}

int main(int argc, char *argv[])
{
  int T;
  cin >> T;
  for(int i = 1 ; i <= T ; i++){
    cout << "Case #" << i << ": " << func() << endl;
  }
  return 0;
}
