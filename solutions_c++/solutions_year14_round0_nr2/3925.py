#include<cstdlib>
#include<cstdio>
#include <iostream>
#include <iomanip>
#include<cmath>
using namespace std;
double solveP2(){
	double c, f, x,rate=2,time=0;
	cin>>c>>f>>x;
	double besttime=(x/rate);

	double  loops=(x/c);
	for(int i=1;i<loops;i++){
		time+=c/rate;
		rate+=f;
	if((time+(x/rate))<besttime){
		besttime=(time+(x/rate));
	}
	else break;
	}	
	return besttime;
}
int main() {
	freopen("B-large-attempt0.out", "wt", stdout);
	freopen("B-large.in", "rt", stdin);
	int cases;
	cin >> cases;
	for (int i = 0; i < cases; i++) {
	double value = solveP2();
	cout.precision(15);
	cout << "Case #" << i + 1 << ": " << value << endl;
	
	}
	return 0;
}
