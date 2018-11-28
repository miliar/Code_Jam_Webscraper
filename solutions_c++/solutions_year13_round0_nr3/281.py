#include <iostream>
#include <vector>
#include <cstdio> 
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <cmath> 

using namespace std;

#define REP(i, to) for(int i=0; i<to; i++)
typedef long long int LLI; 

string toDigits(LLI n){
  string result;
  while(n>0){
    result += (char)('0' + (n%10)); 
    n /= 10; 
  }
  reverse(result.begin(), result.end());
  return result; 
}

bool isPalindrome(LLI n){
  string D = toDigits(n); 
  REP(i, D.size()/2) if(D[i] != D[D.size()-1-i]) return false;
  return true; 
}

struct classcomp{
  bool operator() (const string& s1, const string& s2) const{
    if(s1.size() != s2.size()) return s1.size() < s2.size(); 
    return s1 < s2; 
  }
};

map<string, int, classcomp> M;

string square(string s){
  reverse(s.begin(), s.end()); 
  string result(s.size()*2 - 1, (char)0); 
  
  REP(i, s.size()){
    REP(j, s.size()){
      result[i+j]+=(s[i]-'0')*(s[j]-'0');
    }
  }
  REP(i, result.size()) result[i] += '0';
  
  reverse(result.begin(), result.end());
  //cout << s << "->" << result << endl;
  
  return result; 
}

void addsquares(const string& act, int ones, bool alsopair, bool force, int pos=0){
//  cout << "addsquares("<<act<<","<<ones<<")"<<endl;
  string rev = act;
  reverse(rev.begin(), rev.end()); 
  if((ones > 0 && alsopair) || force){
    M[square(rev + act)]=M.size();
  }
  if(ones > 0 || act[0]!='0' || force){
    M[square(rev + act.substr(1))]=M.size();
  }
  
  if(ones==0){
    return; 
  }
  
  for(int i=pos; i<act.size();i++){
    if(act[i]=='0'){
      string cop = act;
      cop[i]='1';
      addsquares(cop, ones-1, alsopair, force, i+1); 
    }
  }
}

  
int main()
{
  for(LLI s=1 ; s <= 1234567 ; s++){
    if(isPalindrome(s) && isPalindrome(s*s)){
      if(s<=100){
        M[toDigits(s*s)]=M.size();
      }
      //cout << s << "=>" << s*s << endl;
    }
  }
    
  for(int d=2; d<=50 ; d++){
    //cout << d << endl;
    string s(d,'0');
    s[d-1]='1';
    addsquares(s,4, true, false);
    
    s[d-1]='2';
    s[0]='1'; 
    addsquares(s,0, true, false);
    
    s[d-1]='2';
    s[0]='0'; 
    addsquares(s,0, true, true);
    
    s[0]='2';
    s[d-1]='1';
    addsquares(s,1, false, false);
  }
    
  M["12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"]=M.size(); 

  int id=1;
  for(map<string, int, classcomp>::iterator iter=M.begin(); iter!=M.end() ; iter++){
    //if(iter->first.size() <= 9)
    //cout << id << ": " << iter->first << endl;
    M[iter->first]=id++;
  }

  int T;
  cin >> T;
  REP(t, T){
    string A, B;
    cin >> A >> B;
    cout << "Case #" << t+1 << ": " << M.upper_bound(B)->second - M.lower_bound(A)->second << endl;
  } 

	return 0;
}
