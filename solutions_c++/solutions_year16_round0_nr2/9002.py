#include <iostream>
#include <cstring>
#include <cstdlib>
#include <map>
#include <set>

using namespace std;

int main(){
  char swap;
  char s[101];
  int T, len, resp;
  int S_m[100] ,S_p[100],
      S_m_rev[100], S_p_rev[100];

  cin >> T;
  for( int j = 0; j < T; j++){
    cin >> s;
    len = resp = strlen(s);

    memset( S_m, 0, len);
    memset( S_p, 0, len);
    memset( S_m_rev, 0, len);
    memset( S_p_rev, 0, len);
    
    S_m[0] = (s[0]=='-')?0:1;
    S_p[0] = (s[0]=='+')?0:1;

    // f
    for( int i=1; i < len; i++ ){
      if( s[i] == '+' ){
	S_p[i] = S_p[i-1];
      }else if( s[i-1] == '-' ){
	S_p[i] = S_p[i-1];
      }else{
	S_p[i] = S_m[i-1]+1;
      }
      if( s[i] == '-' ){
	S_m[i] = S_m[i-1];
      }else if( s[i-1] == '+' ){
	S_m[i] = S_m[i-1];
      }else{
	S_m[i] = S_p[i-1]+1;
      }
    }
    
    // b
    for( int i=0; i < len/2; i++ ){
      swap = s[i];
      s[i] = s[len-1-i];
      s[len-1-i] = swap;
    }
    for( int i=0; i < len; i++ ){
      s[i] = (s[i]=='-')?'+':'-';
    }
    
    S_m_rev[0] = (s[0]=='-')?1:2;
    S_p_rev[0] = (s[0]=='+')?1:2;

    for( int i=1; i < len; i++ ){
      if( s[i] == '+' ){
	S_p_rev[i] = S_p_rev[i-1];
      }else if( s[i-1] == '-' ){
	S_p_rev[i] = S_p_rev[i-1];
      }else{
	S_p_rev[i] = S_m_rev[i-1]+1;
      }
      if( s[i] == '-' ){
	S_m_rev[i] = S_m_rev[i-1];
      }else if( s[i-1] == '+' ){
	S_m_rev[i] = S_m_rev[i-1];
      }else{
	S_m_rev[i] = S_p_rev[i-1]+1;
      }
    }

    resp = S_p[len-1];
    for( int i=len-2; i > -1; i-- ){
      if( S_m[i] + S_p_rev[len-i-2] < resp ){
	resp = S_m[i] + S_p_rev[len-i-2] ;
      }
    }
    resp = ( resp < S_m_rev[len-1] )? resp: S_m_rev[len-1];
    cout << "Case #" << j+1 << ": " << resp << endl;
  }
  return 0;
}
