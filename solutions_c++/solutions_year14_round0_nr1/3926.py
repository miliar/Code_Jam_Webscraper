#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<sstream>
#include<cmath>
#include<ctime>
#include<algorithm>
#include<vector>
#include<set>
#include<stack>
#include<queue>
#include<map>

#define rep(i, s, n) for(i = (s); i < (n); i++)
#define LIM 1000000000

using namespace std;

ostringstream op;

void pv(vector<int> v){
	op << "[";
	for(int i = 0; i < v.size(); i++)
		op << v[i] << " ";
	op << "]" << endl;
}

void printarr(int *a, int n){
	int i;
	rep(i, 0, n)
		op << a[i]<< " ";
	op << endl;
}

int main(int argc, char** argv){
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(0);
	//clock_t t_start, t_end;
	//t_start = clock();
	int t;
	cin >> t;
	for(int k = 1; k <= t; k++){
		int init[4];
		int fin[17];
		int ctr = 0;
		int ictr = 0;
		int a1, x, a2;
		cin >> a1;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				cin >> x;
				if(i+1 == a1)
					init[ctr++] = x;
			}
		}
		ictr = 0;
		cin >> a2;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				cin >> x;
				if(i+1 == a2)
					fin[ictr++] = x;
			}
		}
		int c = 0;
		int ans = 0;
		for(int i = 0; i < ctr; i++){
			for(int j = 0; j < ictr; j++){
				if(init[i] == fin[j]){
					c++;
					ans = init[i];
				}
			}
		}
		if(c == 1)
			op << "Case #" << k << ": " << ans << endl;
		else if(c == 0)
			op << "Case #" << k << ": " << "Volunteer cheated!" << endl;
		else op << "Case #" << k << ": " << "Bad magician!" << endl;
	}
	//t_end = clock();
	//op << (double)(t_end - t_start)/CLOCKS_PER_SEC << "s" << endl;
	cout << op.str();
	return 0;
}

