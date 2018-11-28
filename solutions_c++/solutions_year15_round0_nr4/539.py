#include <stdio.h>
#include <algorithm>
#include <assert.h>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#include <queue>
#include <cmath>
#include <ctime>
#include <climits>
#include <iomanip>
#include <sstream>
using namespace std;

typedef long long LL;
#define tr(container, it)for(__typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define PB push_back
#define MP make_pair
#define REP(i,a,b) for (int i = (a); i < (int)(b); i++)

int GCD (int a, int b) { if (!a) return b; return GCD(b%a, a);}

int main() {
  clock_t startTime = clock();
  ios_base::sync_with_stdio(false);

  int t; cin>>t;
  string gg = "GABRIEL", rr = "RICHARD";
  for (int test = 1; test <= t; test ++) {
  	cout<<"Case #"<<test<<": ";
  	int x, r, c; cin>>x>>r>>c;
  	if (r > c) swap(r, c);
  	if (x == 1) {
  		cout<<gg<<"\n";
  	} else if (x == 2) {
  		if (r * c % 2 == 0) {
  			cout<<gg<<"\n";
  		} else cout<<rr<<"\n";
  	} else if (x == 3) {
  		if ((r % 3 == 0 && c > 1) || (c % 3 == 0 && r > 1)) {
  			cout<<gg<<"\n";
  		} else cout<<rr<<"\n";
  	} else if (x == 4) {
  		int area = r * c;
  		bool pos = false;
  		if ((r % 4 == 0 && c >= 3) || (c % 4 == 0 && r >= 3)) pos = true;
  		if (pos) cout<<gg<<"\n";
  		else cout<<rr<<"\n";
  	} else if (x == 5) {
  		bool pos = false;
  		if (r % 6 == 0 && c % 10 == 0) pos = true;
  		if (c % 6 == 0 && r % 10 == 0) pos = true;
  		if (r % 5 == 0 && c % 12 == 0) pos = true;
  		if (r % 4 == 0 && c % 15 == 0) pos = true;  		
  		if (r % 3 == 0 && c % 20 == 0) pos = true;
  		if (pos) cout<<gg<<"\n";
  		else cout<<rr<<"\n";
  	} else if (x > 5) {
  		cout<<rr<<"\n";
  	}
  }

  clock_t endTime = clock();
  cerr<<"\nTime:"<< double(endTime - startTime) / CLOCKS_PER_SEC <<" seconds\n" ;
  return 0;
}