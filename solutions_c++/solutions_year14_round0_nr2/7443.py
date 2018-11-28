#include<iostream>
#include<sstream>
#include<map>
#include<vector>
#include<queue>
#include<stack>

using std::cin;using std::cout;using std::endl;
using std::string;using std::stringstream;
using std::map;using std::make_pair;
using std::vector;
using std::queue;
using std::stack;
using std::fixed;

#define FOR(i,s,e) for (int i = int(s); i != int(e); ++i)
#define FORIT(i,c) for (typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
stringstream ssin;
void getline2ss(stringstream& ssin)
{
  string line;ssin.clear();
  getline(cin,line);ssin.str(line);
}
//getline2ss(ssin);

int main()
{
  int T;
  getline2ss(ssin);
  ssin >> T;
  FOR(i,0,T) {
    double C,F,X;
    double prev_cnt = 100000000.0;
    int buy = 0;
    getline2ss(ssin);
    ssin >> C >> F >> X;
    while(1) {
      double cnt = 0;
      FOR(j,0,buy) {
        cnt+=C/(2+j*F);
      }
      cnt+=X/(2+buy*F);
      if (cnt >= prev_cnt) {
        //cout.precision(6);
        cout << "Case #" << i+1 << ": " <<fixed<< prev_cnt<< endl;
        break;
      }
      prev_cnt = cnt;
      buy++;
    }
  }

}
