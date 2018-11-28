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

ll N, J, j;
ll nums[50];
ll divi[11];
//ifstream cin ("C-small.in");
ofstream fout ("C-small.out");

bool not_prime(ll a) {
	ll use = divi[a];
	ll m = sqrt(use);
	For (i, 2, min(m, use-1)+1 ) {
		if (use%i == 0) {
			divi[a] = i;
			return true;
		}
	}
	return false;
}

void check() {
	bool prll = true;
	
	//Set divi to the number considered in different bases
	For (base, 2, 11) {
		ll out = 0;
		For (j, 0, N) {
			out *= base;
			out += nums[j];
		}
		divi[base] = out;
		cout << divi[base] << " ";
	}
	cout << endl;
	
	For (i, 2, 11) {
		if (not_prime(i) == false) {
			prll = false;
		}
	}
	if (prll) {
		For (i, 0, N) {
			fout << nums[i];
		}
		For (i, 2, 11) {
			fout << " " << divi[i];
		}
		fout << endl;
		j++;
	}
}


bool backtrack(ll pos) {
	if (pos == N) {
		if (nums[0] == 0 || nums[N-1] == 0) {
			return false;
		}
		/*For (i, 0, N) {
			fout << n_bw[i];
		}
		fout << endl;*/
		check();
		return true;
	}
	ll save = nums[pos];
	if (j == J) { return true; }
	nums[pos] = 0;
	backtrack(pos +1); //0 in spot;
	if (j == J) { return true; }
	nums[pos] = 1;
	backtrack(pos +1); //1 in spot;
	nums[pos] = save;
}

int main() {
	//ifstream cin ("C-small.in");
	//ofstream cout ("C-small.out");
	
	ll T;
	cin >> T;
	For (t, 1, T+1) {
		fout << "Case #" << t << ": " << endl;
		cin >> N >> J;
		j = 0;
		For(i, 0, N) {
			nums[i] = 0;
		}
		//To loop through every possibility...
		backtrack(0);
	}
	
	
	
	return 0;
}

