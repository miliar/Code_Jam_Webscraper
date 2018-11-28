#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <sstream>
using namespace std;

//const int M = 1000 * 1000 * 10 + 1;
const int M = 1000;
int D[M];

bool isPal(int n) {
	stringstream out;
	out << n;

	string s = out.str();
	string rs = s;
	reverse(rs.begin(), rs.end());
	return s == rs;
}

bool check(int n) {
	return isPal(n) && isPal(n*n);
}

void preCalc(){
	memset(D, 0, sizeof(D));

	int len = sizeof(D)/sizeof(int);
	for(int i = 1 ; i < len ; i++) {
		D[i] = D[i-1] + (check(i)?1:0);
	}
}

int main() {

	preCalc();

	int N ;
	cin>>N ;

	for(int T = 1 ; T <= N ; T++) {
		long long a,b;
		cin>>a>>b ;

		int ra = sqrt((double)a-1);
		int rb = sqrt((double)b);
		//cout<<a<<" "<<b<<" -> "<<ra<<" "<<rb<<endl;
		//cout<<D[rb]<<" "<<D[ra]<<endl;
		cout<<"Case #"<<T<<": "<<(D[rb] - D[ra])<<endl;
	}
	return 0;
}