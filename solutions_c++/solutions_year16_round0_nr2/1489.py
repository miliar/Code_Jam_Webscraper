#include <iostream>
#include <iomanip>
#include <sstream>
#include <cstdlib>
#include <cstdio>

#include <vector>
#include <queue>
#include <map>
#include <set>
#include <stack>
#include <algorithm> //max...
#include <utility> //pair
#include <complex>
#include <climits> //int, ll...
#include <limits> //double...
#include <cmath> //abs, atan...

#include <cstring> //memset
#include <string>

using namespace std;

typedef long long ll;

typedef pair<int,int> ii;
typedef pair<ll, ll> ll_ll;
typedef vector<int> vi;
typedef map<int, int> mii;
typedef vector<ii> vii;
typedef vector<ll> vll;
typedef vector<vi> vvi;


int main (){
	int t;
	string n;
	bool est;
	int cont;
	cin >> t;
	for (int i =0 ; i<t; i++){
		cin >> n;
		est = true;
		cont =0;
		for (int j=n.size()-1; j>=0; j--){
			if ((n[j] == '+' && !est) || (n[j]=='-' && est)){
				est = !est;
				cont++;
			}
		}
		cout << "Case #" << i+1 <<": " << cont << endl;
	}
	return 0;
}
