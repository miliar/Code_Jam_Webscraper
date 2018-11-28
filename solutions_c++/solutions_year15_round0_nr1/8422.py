#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <cassert>
#include <complex>
#include <map>
#include <stdio.h>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <queue>
#include <set>
#include <string>
#include <vector>
#include <cstring>
#include <stack>
#include <iostream>
#include <bitset>
using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define SZ 150
#define ii pair<int, int>
#define ll long long
#define vi vector<int>
// vector.assing(n, vi())

int t;
int smax;
string in;
int main() {
	ofstream myfile;
	myfile.open ("/Users/ahmedhagii/Desktop/out.txt");
    ifstream filein ("/Users/ahmedhagii/Downloads/A-large.in.txt");
	filein >> t;
	for(int T=1;T<=t;T++) {
		int audience = 0;
		int more = 0;
		filein >> smax;
		filein >> in;
		for(int i=0;i<=smax;i++) {
			int num = in[i] - '0';
			printf("au %d %d %d %d\n", audience, num, more, i);
			if(audience < i) {
				more += (i - audience);
				audience = i;
			}
			audience += num;
		}
		myfile << "Case #" << T << ": " << more << endl;
		// printf("Case #%d: %d\n", T, more);
	}
}











