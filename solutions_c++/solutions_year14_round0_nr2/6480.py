#include <fstream>
#include <iomanip>


double calc(double c, double f, double x, int n);

int main(){
	double c, f, x;
	int n;
	double pre;
	double temp;
	std::ifstream fin("2.in");
	std::ofstream fou("2.out");

	fin >> n;
	for (int i = 1; i <= n; i++){
		fin >> c >> f >> x;
		pre = calc(c, f, x, 0);
		temp = calc(c, f, x, 1);
		int k = 2;
		while (pre > temp){
			pre = temp;
			temp = calc(c, f, x, k);
			k++;
		}

		fou << "case #" << i << ": ";
		fou << std::fixed << std::setprecision(7);
		fou << pre << std::endl;
	}


	return 0;
}

double calc(double c, double f, double x, int n){
	double v = 2;
	double t = 0;
	for (int i = 0; i < n; i++){
		t += c / v; 
		v += f;
	}
	t += x / v;
	return t;
}