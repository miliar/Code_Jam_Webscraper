#include <iostream>
#include <cmath>
#include <algorithm>
#include <fstream>
#include <vector>
#include <set>
#include <stack>
#include <iomanip>
#include <queue>
#include <list>
#include <utility>
#include <map>

using namespace std;
ifstream fin;
ofstream fout;
double c,f,x,sum=0,minx=1000000;
int t;
double ff;
int main(){
	std::ios_base::sync_with_stdio(false);
	fout.open("ss.txt");
	fin.open("B-large.in");
	fin.tie(NULL);
	fin >> t;
	 fout << std::setprecision(7) << std::fixed;
	for(int l = 0; l < t; l++){
		minx = 10000000;
		fin >> c >> f >> x;
		sum = 0;
		ff = 2;
		while(sum < minx && sum <= x){
			if(sum + (x/ff) < minx)
				minx = sum + (x/ff);
			sum+=(c/ff);
			ff+=f;
		}
		fout << "Case #" << l+1 << ": " << minx << "\n";
	}
	return 0;
}