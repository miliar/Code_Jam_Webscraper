/* 
 * in the name of god 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 */ 

#include <iostream> 
#include <fstream> 
#include <sstream> 
#include <cstdio> 
#include <cstring> 
#include <cstdlib> 
#include <cmath> 
#include <ctime> 
#include <algorithm> 
#include <vector> 
#include <queue> 
#include <deque> 
#include <stack> 
#include <set> 
#include <map> 
#include <complex> 
#include <bitset> 
#include <iomanip> 
#include <utility> 

using namespace std; 

typedef long long LL; 
typedef pair<int,int> pii; 
typedef complex<double> point; 

int a[10][10],b[10][10];

void main2(){
	int f0; cin >> f0; f0--;
	for (int i=0; i<4; i++) for (int j=0; j<4; j++) cin >> a[i][j];
	int f1; cin >> f1; f1--;
	for (int i=0; i<4; i++) for (int j=0; j<4; j++) cin >> b[i][j];
	int ret = -1; 
	for (int k=1; k<=16; k++){
		int c = 0;
		for (int j=0; j<4; j++)
			c+= (a[f0][j] == k) + (b[f1][j] == k);
		if (c == 2){
			if (ret != -1){
				cout << "Bad magician!";
				return;
			}
			ret = k;
		}
	}
	if (ret == -1)
		cout << "Volunteer cheated!";
	else
		cout << ret;
}

int main(){
	int T; cin >> T;
	for (int i=1; i<=T; i++){
		cout << "Case #" << i << ": ";
		main2();
		cout << endl;
	}
	return 0;
}
