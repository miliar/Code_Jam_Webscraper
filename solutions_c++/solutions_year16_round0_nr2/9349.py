#include<iostream>
#include<string>
#include<vector>
using namespace std;

class Solver{
public:
  int getAns( string s ){
    vector<char> c;
    vector<int> n;
    for( int i=0; i<s.length(); ){
      char start = s[i];
      ++i;
      int cnt = 1;
      while( i<s.length() && s[i]==start ){
	++i;
	++cnt;
      }
      c.push_back( start );
      n.push_back( cnt );
    }
    return calcAns( c, n, s.length() );
  }
private:
  void show( int nn, vector<char>& c, vector<int>& n ){
    for( int i=nn; i<c.size(); ++i ){
      cout << c[i] << " ";
    }
    cout << endl;
    for( int j=nn; j<c.size(); ++j ){
      cout << n[j] << " ";
    }
    cout << endl;
  }
  int getMaxIndex( char ch, int index, vector<char>& c, vector<int>& n ){
    int maxIndex;
    int maxNum = -1;
    int i;
    for( i=index; i<c.size(); ++i ){
      if( c[i]==ch ){
	if( maxNum < n[i] ){
	  maxNum = n[i];
	  maxIndex = i;
	}
      }
    }
    return (maxNum==-1)?c.size():maxIndex;
  }
  int calcAns( vector<char>& c, vector<int>& n, int len ){
    for( int i=0; i<c.size(); ++i ){
      if( n[i]==len ){
	if( c[i]=='-' )
	  return i+1;
	else
	  return i;
      }
      
      //show( i, c, n );
      int index = getMaxIndex( (c[i]=='-')?'+':'-', i+1, c, n );
      if( index==c.size() )
	return i+1;
      n[index] += n[i];
      reverse( i+1, index-1, c, n );
    }
    return -1;
  }
  char rev( char ch ){
    return (ch=='-')?'+':'-';
  }
  void reverse( int f, int t, vector<char>& c, vector<int>& n ){
    while( f<t ){
      swap( n[f], n[t] );
      char ch = c[f];
      c[f] = rev( c[t] );
      c[t] = rev( ch );
      ++f; --t;
    }
  }
};
      

int main(){
  int n; cin >> n;
  for( int i=1; i<=n; ++i ){
    string str; cin >> str;
    cout << "Case #" << i << ": ";
    Solver s;
    cout << s.getAns( str ) << endl;
  }
  return 0;
}
