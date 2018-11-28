#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <numeric>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <iomanip>
#define pb push_back
#define mp make_pair
#define sz(x) (int)x.size()
using namespace std;

int main(){
	ifstream in("B-large.in");
	ofstream out("out2.txt");
//#define in cin
//#define out cout
	int T;
	in >> T;
	for(int i = 0 ; i < T ; i++){
		double c , f , x , rate = 2.0 , time = 0.0;
		in >> c >> f >> x;
		while(1){
			if( (c/rate + (x/(rate+f))) < x/rate){
				time += c/rate;
				rate += f;
			}else{
				time += x/rate;
				break;
			}
		}
		out.setf(ios::fixed);
		out.precision(7);
		out << "Case #" << i+1 << ": " << time << endl;
	}
}
