#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <cmath>
using namespace std;
typedef long long i64;
#define fu(i,m,n) for(int i=m; i<n; i++)
#define fr(i,m,n) for(typeof(m) i=m; i!=n; i++)
#define fa(i,c) fr(i,(c).begin(),(c).end())

int main(void) {
	int T;
	cin >> T;
	for(int ts=1; ts<=T; ts++) {
		cout << "Case #" << ts << ":";
		int r,c;
		int data[2][4][4];
		cin >> r;
		fu(i,0,4) fu(j,0,4) cin >> data[0][i][j];
		cin >> c;
		fu(i,0,4) fu(j,0,4) cin >> data[1][i][j];
		int valid1=0,valid2=0;
		fu(i,0,4) valid1|=(1<<data[0][r-1][i]);
		fu(i,0,4) valid2|=(1<<data[1][c-1][i]);
		int valid = (valid1 & valid2);
		bool done=false;
		if(valid==0) {
			cout << " Volunteer cheated!" << endl;
			done=true;
		}
		fu(i,0,20) if(valid==(1<<i)) {
			cout << " " << i << endl;
			done=true;
		}
		if(!done) {
			cout << " Bad magician!" << endl;
		}
        }
}
