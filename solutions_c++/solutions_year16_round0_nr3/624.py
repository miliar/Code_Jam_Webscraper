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

int len;

bool isdeler(long long s, int b, int d){
  long long val=0;
  long long power=1;
  for(int i=0;i<len;i++){
    if(s&(1<<i))
      val=(val+power)%d;
    power=(b*power)%d;
  }
  return val==0;
}

string bitstr(long long s){
  string out="";
  while(s){
    out=((s&1)?'1':'0')+out;
    s/=2;
  }
  return out;
}
int main(){
	int run, runs;
	scanf("%d",&runs);
	for(run=1;run<=runs;run++){
	  printf("Case #%d:\n", run);
	  int need,have=0;
	  scanf("%d %d",&len,&need);
	  for(long long s=(1ll<<(len-1))+1;s<(1ll<<len)&&have<need;s+=2) if(__builtin_popcountll(s)%6==0){
      vi res;
      bool isok=true;
      for(int b=2;b<=10;b++){
        if(b%2){
          res.pb(2); continue;
        } else if((b%3)==1){
          res.pb(3); continue;
        }
        bool found=false;
        for(int d=3;d<100;d+=2){
          if(isdeler(s,b,d)) {
            res.pb(d); found=true; break;
          }
        }
        if(!found) { isok=false; break; }
      }
      if(isok){
        have++;
        printf("%s",bitstr(s).c_str());
        for(int i=0;i<sz(res);i++){
          printf(" %d",res[i]);
        }
        printf("\n");
      }
    }
	  
	  
	  
  }
	
	
	
	
}

