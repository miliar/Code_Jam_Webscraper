#include<iostream>
using namespace std;
long long T, maxx, k;
char c;
int main(){
  cin >> T;
  for (long long t = 0;t < T;++t) {
    long long curr = 0, needed = 0;
    cin >> maxx;
    for (long long  i=0; i<=  maxx; ++i) {
	    cin >> c;
	    k = c - '0';
	    if (curr < i) {
		    needed=needed+i-curr;
		    curr=i;
	    };
	    curr+=k;
    };
    cout << "Case #" << t+1 << ": " << needed << endl;
  };

}
