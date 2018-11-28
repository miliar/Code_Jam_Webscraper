#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

using namespace std;


int main(){
	int nt;
	cin >> nt;
	for(int t=0;t<nt;t++){
		double c,f,x, n;
		n=2;
		cin >> c >> f >> x;
		double totalTime = 0;
		while(f*x > c*(n+f)){
			totalTime += c/n;
			n += f;
		}
		totalTime += x/n;
		
		cout << "Case #" << t+1 << ": " << fixed << setprecision(7) << totalTime << endl;
	}
	return 0;
}