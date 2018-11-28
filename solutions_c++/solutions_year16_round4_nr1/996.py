#include<bits/stdc++.h>
using namespace std;

int N,R,P,S;

string getp(char c){
  if( c == 'R' ){
    return "RS";
  } else if( c=='P' ){
    return "PR";
  } else {
    return "SP";
  }
}
string make(char c){
  string s = ""; s+=c;
  for(int i=1;i<=N;i++){
    string ns = string( (1<<i),' ' );
    for(int j=0;j<(int)s.size();j++){
      int a = 2*j, b = a+1;
      string x = getp( s[j] );
      ns[a] = x[0]; ns[b] = x[1];
    }
    s = ns;
  }
  return s;
}

void sort( string &s,int l,int r){
  if( r - l == 1 ) return;
  int h = (r+l)/2;
  sort( s, l, h );
  sort( s, h, r );
  string sb1 = s.substr( l, h-l );
  string sb2 = s.substr( h, r-h );
  if( sb1 > sb2 ) swap( sb1, sb2 );
  for(int i=l;i<h;i++) s[i] = sb1[i-l];
  for(int i=h;i<r;i++) s[i] = sb2[i-h];
}

bool check(string &str){
  int r=0,p=0,s=0;
  for(int i=0;i<(int)str.size();i++){
    if( str[i] == 'R' ) r++;
    if( str[i] == 'P' ) p++;
    if( str[i] == 'S' ) s++;
  }
  return r == R && p == P && s == S;
}

int main(){
  int T;
  cin >> T;
  for(int ttt=1;ttt<=T;ttt++){
    cout << "Case #"<< ttt << ": ";

    cin >> N >>  R >> P >> S;
    string res = "z";
    string A = make( 'R' );
    if( check(A) ){
      sort( A, 0, (1<<N) );
      res = min( res, A );
    }
    A = make( 'S' );
    if( check(A) ){
      sort( A, 0, (1<<N) );
      res = min( res, A );
    }
    A = make( 'P' );
    if( check(A) ){
      sort( A, 0, (1<<N) );
      res = min( res, A );
    }
    
    if( res == "z" ) cout << "IMPOSSIBLE" << endl;
    else cout << res << endl;
  }
}
