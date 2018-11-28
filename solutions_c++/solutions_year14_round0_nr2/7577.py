#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

#define foreach(i, container) for(auto i=(container).begin(); i!=(container).end(); i++)
#define fortime(i,n) for(auto i=((n)-(n)); i<(n); i++)

int main() {
	ifstream input("input");
	ofstream output("output");
	int T;
	input >> T;
	fortime(i, T)
	{
		double C, F, X;
		input >> C >> F >> X;
		///////////////////////////////
		double result = 0;
		double v = 2.0;

		while (1){
			double t1 = X / v;
			double t2 = X / (v + F) + C / v;
			if (t1 < t2){
				result += t1;
				break;
			}
			else{
				result += C / v;
				v += F;
			}
		}
		///////////////////////////////
		output << fixed << setprecision(7);
		output << "Case #" << i + 1 << ": " << result << "\n";
	}
	return 0;
}