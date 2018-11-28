#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <iomanip>
#include <sstream>
#include <bitset>
#include <fstream>
#include <queue>
#include <math.h>
#include <set>
#include <stdlib.h>
#include <time.h>
#include <list>

#define For(i,a,b) for(int i=(a);i<(b);++i)
#define rep(i,n)  For(i,0,n)

//clear memory
#define CLR(a) memset((a), 0 ,sizeof(a))
#define check(a) rep(i, a.size()) cout << a[i] << endl
#define SORT(c) sort((c).begin(),(c).end())
#define ll long long
#define vi vector<int>
#define all(it,a) for(auto it = a.begin(); it!=a.end(); it++)
using namespace std;


int main(void) {
	int n;
	cin >> n;

	rep(i, n){
		int inp;
		cin >> inp;

		if (inp == 0){
			cout << "Case #" << (i + 1) << ": " << "INSOMNIA" << endl;
			continue;
		}

		set<int> s;
		int sikou = 1;
		while (s.size() < 10){
			stringstream ss;
			ss << sikou * inp;
			sikou++;
			string str = ss.str();
			rep(k, str.length()){
				s.insert(str[k]);
			}
		}



		int result = (sikou - 1) * inp;


		cout << "Case #" << (i+1) << ": " << result << endl;
	}
	
	
	return 0;
}
