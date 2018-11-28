#include <cstdio>
#include <cctype>
#include <cmath>
#include <cstdlib>

#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>

#define pb push_back
#define fi(it, v) for (typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define fit(v) fi(it, v)
#define f(i,n) for(int i = 0; i < (n); ++i)

#define fs first
#define sc second
#define mp make_pair

#define all(v) (v).begin(), (v).end()
#define ll long long int
#define vi vector<int>
#define vii vector<vi >
using namespace std;

bool pal(int x){
	stringstream ss; 
	ss << x;
	string s = ss.str();
	int n = s.size()-1;
	f(i, n/2+1) if (s[i] != s[n-i]) return false;
	return true;
}

int main(){
	
	ofstream output;
	output.open("problemC.out");
	ifstream input;
	input.open("problemC.in");
	
	int t; input >> t;
	for(int c = 1; c <= t; ++c){
		
		int a,b, sol = 0; input >> a >> b;

		for (int i = a; i <= b; ++i){

			int k = (int)sqrt(i);
			if (i == k*k && pal(i) && pal(k))  { cout << i << " " << k << endl;
			sol++;}
		}
		
		output << "Case #" << c << ": " << sol;
		
		output << endl;
	}
	input.close();
	output.close();
	return 0;
}
