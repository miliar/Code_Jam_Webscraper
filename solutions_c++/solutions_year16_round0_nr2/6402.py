#include <algorithm>
#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <string>
using namespace std;
typedef long long ll;
typedef pair<int, int> P;

void show(vector<char> ps){
    for(int i = 0; i < ps.size(); i++){
      cout << ps[i];
    }
    cout << endl;

}
int main(){
  int T;
  cin >> T;
  for(int c = 1; c <= T; c++){
    string ps_;
    cin >> ps_;
    vector<char> ps;
    char pre = '.';
    for(int i = 0; i < ps_.size(); i++){
      if( pre != ps_[i] ){
	pre = ps_[i];
	ps.push_back( pre );
      }
    }
    //show(ps);
    int flip = 0;
    for(int i = ps.size() - 1; i >= 0; i--){
      if( ps[i] == '-' ){
	//cout << "i=" << i << endl;
	if( ps[0] != '-' ){
	  ps[0] = '-';
	  flip++;
	}
	vector<char>::iterator it = ps.begin();
	it += i + 1;
	reverse(ps.begin(), it);
	for(int j = 0; j <= i; j++){
	  if(ps[j] == '-') ps[j] = '+';
	  else ps[j] = '-';
	}
	flip++;
	//show(ps);
      }
    }
    cout << "Case #" << c << ": " << flip << endl;
  }
}
