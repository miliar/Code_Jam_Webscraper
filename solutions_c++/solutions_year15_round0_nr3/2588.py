#include<cmath>
#include<cstdlib>
#include<string>
#include<sstream>
#include<vector>
#include<iostream>
#include<queue>
#include<deque>
#include<map>
#include<set>
#include<stack>
#include<list>
#include<algorithm>
using namespace std;

void calc(char a, char b, char &c, int sa, int sb, int &sc){
  sc = 1;
  if(a=='l' && b=='l') c = 'l';
  if(a=='l' && b=='i') c = 'i';
  if(a=='l' && b=='j') c = 'j';
  if(a=='l' && b=='k') c = 'k';
  if(a=='i' && b=='l') c = 'i';
  if(a=='i' && b=='i'){
    c = 'l';
    sc = -1;
  }
  if(a=='i' && b=='j') c = 'k';
  if(a=='i' && b=='k'){
    c = 'j';
    sc = -1;
  }
  if(a=='j' && b=='l') c = 'j';
  if(a=='j' && b=='i'){
    c = 'k';
    sc = -1;
  }
  if(a=='j' && b=='j'){
    c = 'l';
    sc = -1;
  }
  if(a=='j' && b=='k') c = 'i';
  if(a=='k' && b=='l') c = 'k';
  if(a=='k' && b=='i') c = 'j';
  if(a=='k' && b=='j'){
    c = 'i';
    sc = -1;
  }
  if(a=='k' && b=='k'){
    c = 'l';
    sc = -1;
  }
  sc *= sa * sb;
}

bool calcs(string s, int n){
  char a = s[0];
  int sa = 1;
  char c;
  int sc;
  for(int i=1; i<s.size(); i++){
    calc(a,s[i],c,sa,1,sc);
    a = c;
    sa = sc;
  }
  char b = a;
  int sb = sa;
  for(int i=0; i<n-1; i++){
    calc(a,b,c,sa,sb,sc);
    a = c;
    sa = sc;
  }
  if(a=='l' && sa==-1) return true;
  else return false;
}

int main(){
  int T;
  cin >> T;
  for(int t=1; t<=T; t++){
    bool ans = false;
    int L,X;
    cin >> L >> X;
    string s;
    cin >> s;
    if(calcs(s,X)){
      char a = s[0];
      int sa = 1;
      bool iok = false;
      bool jok = false;
      for(int i=1; i<L*X; i++){
	char c;
	int sc;
	if(!iok && a=='i' && sa==1){
	  iok = true;
	  a = s[i%L];
	  sa = 1;
	}
	else if(iok && !jok && a=='j' && sa==1){
	  jok = true;
	  break;
	}
	else{
	  calc(a,s[i%L],c,sa,1,sc);
	  a = c;
	  sa = sc;
	}
      }
      if(iok && jok) ans = true;
    }
    
    if(ans) cout << "Case #" << t << ": YES" << endl;
    else cout << "Case #" << t << ": NO" << endl;
  }
}

