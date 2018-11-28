#include <iostream>
#include <string>
#include <map>
#include <climits>

using namespace std;

int main(){
  int T;
  cin>>T;
  cin.clear();
  cin.ignore(INT_MAX,'\n');
  string result="";
  for(int i = 0;i<T;i++){
    int s_max = 0;
    cin>>s_max;
    int rval=0;
    string t;
    cin>>t;
    int agg = t.at(0) - '0';
    for(int j = 1;j<=s_max;j++){
      if(agg<j){
         rval++;
        agg++;
      }
      agg = agg + (t.at(j) - '0');
    }
    result = result + "Case #"+to_string(i+1)+": "+to_string(rval)+"\n";
    cin.clear();
    cin.ignore(INT_MAX,'\n');
  }
  cout<<result;
  return 0;
}

