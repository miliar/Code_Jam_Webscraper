#include <vector>
#include <iostream>
#include <math.h>
#include <iomanip>
#include <fstream>
#include <stack>
#include <queue>
#include <set>
#include <string>
#include <iomanip>
#include <deque>

using namespace std;

#define PI 3.14159265358979323846

using namespace std;

void main()
{
	ifstream inp("E:\\Note\\Input.txt");
	cin.rdbuf(inp.rdbuf());
	ofstream outp("E:\\Note\\Output.txt");
	cout.rdbuf(outp.rdbuf());
	int t;
	cin >> t;
	for (int k = 0; k < t; k++){
		double c, f, x;
		double p = 2;
		cin >> c >> f >> x;
		int i = 0;
		double mintime = 100001;
		double time = 100000;
		double ttime=0;
		while (time<mintime){
			mintime = time;			
			time = 0;
			if (i != 0){
				ttime += c / p;
				p += f;
			}			
			time += x / p+ttime;	
			i++;
		}
		cout << fixed << setprecision(7) << "Case #" << k+1 << ": " << mintime<<endl;
	}
}