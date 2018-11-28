#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstdlib>
#include <stack>
#include <cstdio>
#include <fstream>
#include <ctime>
#include <cassert>

using namespace std;

void swapa(char s[], int i, int j){
  --j;
  while(i<=j){
    char c;
    c=s[j];
    s[j]=s[i];
    s[i]=c;
    ++i;
    --j;
  }
  return;
}

void flip(char s[], int i, int j){
  for(int k=i;k<j;++k){
    if(s[k]=='-')
      s[k]='+';
    else
      s[k]='-';
  }
  return;
}

int main(){
  int t,m;
  cin >> t;
  m=t;
  while(t--){
    string ss;
    cin >> ss;
    char s[ss.size()];
    for(int ij=0;ij<ss.size();++ij)
      s[ij]=ss[ij];
    int flips=0;
    while(1){
      int j,i,k;
      for( j=ss.size()-1;j>=0;--j){
        if(s[j]!='+')
          break;
      }
      ++j;
      if(j==0)
        break;

      if(s[0]=='+'){
        for( k=0;k<j;++k){
          if(s[k]!='+')
            break;
        }
          flip(s,0,k);
          ++flips;
      }
      else{
      //  cout << s << endl;
        swapa(s,0,j);
      //  cout << s << endl;
        flip(s,0,j);
      //  cout << s << endl;
        ++flips;
      }

    }
      cout << "Case #" << m-t << ": " << flips << endl;
  }

}
