#include<iostream>
#include<string>

using namespace std;
int ctoi ( char c ) {
  int res = (int)c;
  res -= '0';
  return res;
}
int main (void) {
  int T; cin >> T;
  for( int k=0; k<T; k++ ) {
    int l; cin >> l;
    string str; cin >> str;
    int n = ctoi(str[0]);
    int res = 0;
    for(  int i=1; i<l+1; i++ ) {
      if( i > n ) {
	res += i-n;
	n = i;
      }
      n += ctoi(str[i]);
    }
    cout << "Case #"<< k+1 << ": " << res << endl;
  }
  return 0;
}
