#include <algorithm>
#include <array>
#include <bitset>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
typedef long long ll;

using namespace std;

const string kInputFilename = "input.txt";
const string kOutputFilename = "output.txt";

ifstream in("input.txt");
ofstream out("output.txt");

int main() {
  int T;
  in >> T;
  for (int ti=0;ti<T;ti++){
    string s;
    in>>s;
    int k;
    in>>k;
    int flips=0;
    int len=s.length();
    for (int i=0;i<len-k+1;i++){
        if (s[i]=='-'){
            flips++;
            for (int j=0;j<k;j++){
                if (s[i+j]=='-'){
                    s[i+j]='+';
                }
                else{
                    s[i+j]='-';
                }
            }
        }
    }
    bool check=true;
    for (int i=0;i<len;i++){
        if (s[i]=='-'){
            check=false;
        }
    }
    if (check){
        out<<"Case #"<<ti+1<<": "<<flips<<endl;
    }
    else{
        out<<"Case #"<<ti+1<<": IMPOSSIBLE"<<endl;
    }
  }
  out.close();
  return(0);
}
