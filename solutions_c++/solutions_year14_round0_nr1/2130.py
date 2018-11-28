#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <climits>
#include <vector>
#include <iterator>
#include <set>
#include <bitset>
#include <ctime>
#include <iomanip>
#include <map>

using namespace std;

const int K = 1e5;
int a[K + 10][10];

int main() {
	ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int test=1; test<=t; test++) {
		int p, q;
		int a[4][4];
		int b[4][4];
		cin>>p;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				cin>>a[i][j];
		cin>>q;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				cin>>b[i][j];
		bool x, y, z;
		x = y = z = false;
		int match = 0;
		int magic = 0;
		for(int i=0; i<4; i++) {
			for(int j=0; j<4; j++) {
				if(b[q-1][i] == a[p-1][j]) {
					match++;
					magic = a[p-1][j];
				}
			}
		}
		cout<<"Case #"<<test<<": ";
		if(match == 1)
			cout<<magic<<"\n";
		else if(match > 1)
			cout<<"Bad magician!\n";
		else
			cout<<"Volunteer cheated!\n";
	}
	return 0;
}