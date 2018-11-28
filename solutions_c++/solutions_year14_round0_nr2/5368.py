#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <vector>
#include <string>
#include <cassert>
#include <fstream>
#include <iomanip>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int ntests;
	cin>>ntests;
	for(int testnum=0; testnum<ntests; testnum++){
		double c, f, x;
		cin>>c>>f>>x;
		double speed = 2.0;
		double best = x/speed;
		double elapsed = 0.0;
		while(elapsed<best){
			double time_to_end = x/speed;
			best = min(best,elapsed+time_to_end);
			double time_to_factory = c/speed;
			speed+=f;
			elapsed+=time_to_factory;
		}
		cout<<"Case #"<<testnum+1<<": "<<setprecision(7)<<setiosflags(ios::showpoint|ios::fixed)<<best<<endl;
	}
	return 0;
}
