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
		double c, f, x, r, tot;
		cin >> c >> f >> x;
		r = 2.0;
		tot = 0;
		double time = 0;
		while(tot < x){
			double t1 = (x-tot)/r;//500
			double t2 = (c-tot)/r + x/(r+f);//250 + 
			if(t1 > t2){
				time += c/r;
				r += f;
				//cout << "Bought farm at " << time << endl;
			}
			else {
				time += t1;
				tot += x;
			}
		}
		printf("Case #%d: %0.7lf\n", k, time);
	}
	//t_end = clock();
	//op << (double)(t_end - t_start)/CLOCKS_PER_SEC << "s" << endl;
	//cout << op.str();
	return 0;
}

