#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <list>
#include <numeric>
#include <algorithm>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;
#define pb push_back
#define sz(v) ((int)(v).size())

string s; int n;
string best;

bool can(string pref){
  int pos=sz(pref)-1;
  string suf="";
  int i;
  for(i=0;i<n&&pos>=0;i++){
    if(s[i]==pref[pos])
      pos--;
    else suf+=s[i];
  }
  
  if(pos==-1){
    //printf("%s:%s:%s\n",pref.c_str(), suf.c_str(),s.substr(i).c_str());
    best=pref+suf+s.substr(i);
  }
  return pos==-1;
}


int main(){
  int run, runs;
  scanf("%d\n",&runs);
  for(run=1;run<=runs;run++){
    char buf[10000];
    scanf("%s",buf);
    s=buf; n=sz(s); best=s;
    //printf("(%s)\n",s.c_str());
    string ans="";
    for(int i=0;i<n;i++){
      for(char c='Z'; c>='A';c--){
        if(can(ans+c)){
          ans+=c;
          break;
        }
      }    
    }

    printf("Case #%d: %s\n", run, best.c_str());

  }
  return 0;
}

