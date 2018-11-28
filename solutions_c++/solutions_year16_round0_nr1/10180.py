#include <iostream>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

bool checkVec(map<int,int>count);
long long countSheep(int N, map<int, int> count);
long long countSheep(int N, map<int, int> count){
  bool notDone = true;
  string str;
  long long ret = N;
  //cout << ret << endl;
  int j=0;
  if (N == 0){
    return -1;
  }
    while(notDone){
      map<int,int>::iterator it;
      str = to_string(ret);
      int pos = 0;
      string str2;
      //cout << str << " , ";
      for(int i = 0; i < str.length(); ++i){
        str2 =str[i];
        pos = stoi(str2);
        //cout << pos << endl;
          it = count.find(pos);
          //cout << it << endl;
          if (it != count.end()){
            //cout << count[i] << " , ";
            count[pos] = count[pos] + 1;
            //cout << count[i] << " , ";
          }
      }
      notDone = checkVec(count);
      if(!notDone){
        break;
      }
      ++j;
      //cout << j << endl;
      ret = N * j;
      //cout << ret << endl
      if (j > 50000){
        return -1;
      }
    }
    return ret;
}
bool checkVec(map<int,int> count){
  int sum =0;
  bool keepGoing = false;
  //cout << keepGoing << endl;
  for(int i=0;i<10;++i){
    if(count[i] == 0){
      //cout << count[i] << endl;
      keepGoing = true;
    }
    //cout << count[i] << endl;
}
  //cout << keepGoing << endl;
  return keepGoing;
}
int main(){
  map<int,int > count;
  int N = 0;
  int testCases = 0;
  long long val = 0;
  for(int i=0;i < 10;++i){
    //cout << i;
    count[i] = 0;
    //cout << count[i] << endl;
  }
  cin >> testCases;
    for(int i = 1; i < testCases+1;++i){
        cin >> N;
        //cout << N << endl;
          val = countSheep(N,count);
          if (val == -1){
            cout << "Case #" << i << ": INSOMNIA" << endl;
          }else{
            cout << "Case #" << i << ": " << val << endl;
          }
    }
}
