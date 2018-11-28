#include<bits/stdc++.h>
using namespace std ;
int modulo(int a,int b,int c) {
  long long res = 1;
  for(int i=0; i<b; i++) {
    res *= a;
    res %= c;
  }
  return res%c;
}
long long mulmod(long long a,long long b,long long c) {
  long long x = 0,y=a%c;
  while(b > 0) {
    if(b%2 == 1) {
      x = (x+y)%c;
    }
    y = (y*2)%c;
    b /= 2;
  }
  return x%c;
}
long long isPrime(long long p,int iteration=18) {
  if(p<=2) {
    return -1;
  }
  if( p%2==0 ) {
    return 2;
  }
  long long s=p-1;
  while(s%2==0) {
    s/=2;
  }
  for(int i=0; i<iteration; i++) {
    long long a=rand()%(p-1)+1,temp=s;
    long long mod=modulo(a,temp,p);
    while(temp!=p-1 && mod!=1 && mod!=p-1) {
      mod=mulmod(mod,mod,p);
      temp *= 2;
    }
    if(mod!=p-1 && temp%2==0) {
      for( long long i = 2 ; i*i < p ; i++ ) {
        if( p%i==0 && i != p ) {
          return i ;
        }
      }
    }
  }
  return -1;
}
long long m[11][17] ;
void genPow() {
  for( long long i = 2 ; i <=10 ; i++ ) {
    long long tmp = i ;
    m[i][0] = 1 ;
    for( int j = 1 ; j < 17 ; j++ ) {
      m[i][j] = tmp ;
      tmp *= i ;
    }
  }
}

int J , N ;
map<string,vector<long long> > mp ;

void backTrack(int pos,string s) {
  if( mp.size() == N )return ;
  if( pos == J ) {
    cerr << s << "\n" ;
    vector<long long> t ;
    for( int i = 2 ; i <= 10 ; i++ ) {
      long long val = 0 ;
      for( int j = 0 ; j < J ; j++ ) {
        if( s[j] == '1' ) {
          val += m[i][j] ;
        }
      }
      //cerr << val << "\n" ;
      //long long num =  isPrime(val) ;
      bool f = 0 ;
      long long num ;
      for( long long j = 2 ; j*j < val ; j++ ){
        if( val%j==0 && j!=val ){
          f = 1 ;
          num = j ;
          break ;
        }
      }
      if( f ) t.push_back(num) ;
      else return ;
    }
    mp[s] = t ;
    cerr << mp.size() << "\n" ;
    return ;
  }
  if( pos > 0 && pos < J-1 )backTrack(pos+1,s+'0') ;
  backTrack(pos+1,s+'1') ;
}
int main() {
  freopen("out.txt","w",stdout) ;
  genPow() ;
  int cases , caseno = 1 ;
  cin >> cases ;
  cin >> J >> N ;
  backTrack(0,"") ;
  cout << "Case #" << caseno++ << ":\n" ;
  for( auto i = mp.begin() ; i!=mp.end() ; i++ ) {
    string s = i->first ;
    reverse( s.begin() , s.end() ) ;
    cout << s ;
    vector<long long> t = i->second ;
    for( int i = 0 ; i < t.size() ; i++ ) {
      cout << " " << t[i] ;
    }
    cout << "\n" ;
  }
  return 0 ;
}

