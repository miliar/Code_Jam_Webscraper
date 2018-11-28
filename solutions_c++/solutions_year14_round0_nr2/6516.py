#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;

int main(){
    int T;
    cin >> T;
    for(int i=0; i<T; ++i){
	double C, F, X, cps=2.0, time=0;
	cin >> C >> F >> X;
	while(1){	    
	    double now = X/cps;
	    double next = X/(cps+F) + C/cps;
	    if(now<next)
		break;
	    double second = C/cps;
//	    cerr << "second;" << second << endl;
	    time += second;
	    cps += F;
	}
//	cerr << "second;" << X/cps << endl;
	double second = X/cps;
	time += second;
	cout << "Case #" << i+1 << ": ";
	printf("%.7f\n", time);
	time = 0; cps =2;
    }
}
