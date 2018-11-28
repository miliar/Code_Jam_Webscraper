#include<iostream>
#include<sstream>
#include<string>
#include<algorithm>
using namespace std;

string tos( long long  a){
	stringstream ss;
	ss << a;
	return ss.str();
}

bool pal( long long n ){
	string a = tos( n );
	string b = a;
	reverse( b.begin(),b.end());
	return a == b ;
}

int main(){
  int t;
  cin >> t;
  long long a , b;
  for( int i = 1 ; i <= t; ++i ){
    cout << "Case #"<<i<<": ";
    cin >> a >> b;
	long long ans = 0;
	for( long long j = 1 ; j * j <= b ; ++ j ){
	  long long num = j * j;
	  if( num >= a && pal( j )&& pal( num ) )
		  ++ans;
	} 
    cout << ans <<endl;
  }
}
