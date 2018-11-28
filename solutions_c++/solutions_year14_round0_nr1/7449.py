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
    map<int,int> mapii;
    int rlt = 0;
    int a;
    getline2ss(ssin);
    ssin >> a; 
    FOR(j,0,4) {
      int tmp;
      getline2ss(ssin);
      if (j == a-1){
        FOR(k,0,4){
          ssin >> tmp;
          mapii.insert(make_pair(tmp, 0));
        }
      }
    }
    getline2ss(ssin);
    ssin >> a; 
    FOR(j,0,4) {
      int tmp;
      getline2ss(ssin);
      if (j == a-1){ 
        FOR(k,0,4){
          ssin >> tmp;
          if (mapii.find(tmp) != mapii.end()) {
            if (rlt != 0) {
             rlt = -1;
            } else {
             rlt = tmp;
           }
          }
        }
      }
    }
    cout << "Case #" << i+1 << ": ";
    if (rlt == -1) cout << "Bad magician!"<< endl;
    else if (rlt == 0) cout << "Volunteer cheated!" << endl;
    else cout << rlt<< endl;
  }
}
