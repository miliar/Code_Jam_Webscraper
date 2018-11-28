#include <iostream> 
#include <fstream>
using namespace std;

int main() {
	ifstream in("B-large.in");
	ofstream out("B-large.out");
	int n;
	in >> n;
	out.precision(20);
	for (int k = 0; k < n; k++) {
		double cost, factory, finish;
		in >> cost >> factory >> finish;
		double min = finish / 2;
		int kol = 0;
		while (true) {
			double profit = 2;
			double tmp = cost / profit;
			for (int i = 0; i < kol; i++) {
				profit += factory;
				tmp += cost / profit;
			}
			kol++;
			tmp += finish / (profit + factory);
			if (min > tmp)
				min = tmp;
			else
				break;
		}
		out << "Case #" << k + 1 << ": " << min << endl;
	}
	return 0;
}