#include <bits/stdc++.h>
using namespace std;
char inverse(char c){
  if(c == '+')return '-';
  else return '+' ;
}
void print(string& s){
  for(int i=0;i<s.size();i++)cout << s[i] ;
  cout << endl;
}
bool check(string& s){
  for(int i=0;i<s.size();i++){
    if(s[i]=='-')return false ;
  }
  return true ;
}
bool changestart(string& s){
  int i = 0 ;
  while(i < s.size()){
    if(s[i]=='+'){s[i]='-' ;i++;}
    else break;
  }
  return i != 0 ;
}
int findlast(string& s ,int l){
  for(int i=l;i>=0;i--){
    if(s[i]=='-')return i ;
  }
  return -1;
}
void flip(string& s , int last){
  string tmp = s;
  for(int i=0;i<=last;i++){
    tmp[i] = inverse(s[last-i]) ;
  }
  s = tmp ;
  //print(s);
  return  ;
}

void solve(int x ,string& s){
    int last = s.size()-1 ;
    int first = 0 ;
    int count = 0  ;
    while(last >= first){
        //print(s) ;
        if(check(s))break ;
        if(changestart(s))count++ ;
        last = findlast(s ,last);
        if(last == -1)break ;
        flip(s,last);
        count++ ;
    }
    cout << "Case #"<<x <<": "<<count << endl;
}
main(){
  ios::sync_with_stdio(false) ;
  int t;
  int x = 1;
  cin >> t ;
  while(t--){
    string s ;
    cin >> s ;
    solve(x,s) ;
    x++ ;
  }
}
