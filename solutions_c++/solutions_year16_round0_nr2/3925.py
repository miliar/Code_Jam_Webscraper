#include<iostream>
#include<list>
#include<string>
#include<cstring>
#include<sstream>
#include<cctype>
#include<string.h>
#include<algorithm>
#include<stack>
#include<fstream>
#include<cstdlib>
#include<vector>
#include<map>
#include<set>
#include<utility>
#include<iomanip>
#include<queue>
#include<math.h>


using namespace std;


typedef long long int ll;
#define For(i, a, b) for(ll i=a; i<b; i++)
//100,000,000 operations


int main() {
	ifstream cin ("B-Small.in");
	ofstream cout ("B-Small.out");
	
	ll T;
	cin >> T;
	For (t, 1, T+1) {
		string in;
		cin >> in;
		int N = in.length();
		int stack[1000];
		For (i, 0, N) {
			if (in[i] == '-') {
				stack[i] = 0;
			}
			if (in[i] == '+') {
				stack[i] = 1;
			}
			//cout << stack[i] << " ";
		}
		//cout << endl;
		
		int out = 0;
		int at = stack[0];
		For (i, 1, N) {
			if (stack[i] != at) {
				out ++;
				at = stack[i];
			}
		}
		if (at == 0) {
			out ++;
		}
		
		cout << "Case #" << t << ": " << out << endl;
	}
	
	
	
	return 0;
}

