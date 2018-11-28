#include<iostream>
#include<fstream>
#include<iomanip>

using namespace std;

int main(){
	int T;
	int idx = 0;
	cout << setiosflags(ios::fixed) << setprecision(7);
	ofstream fout;
	fout.open("cookie.out", ios::app);
	fout << setiosflags(ios::fixed) << setprecision(7);
	cin >> T;
	while(idx < T){
		idx ++;
		double C, F, X;
		cin >> C >> F >> X;
		double left = X;
		double step = 2;
		double res = 0;
		while(true){
			if(X / step < (C / step + X / (step + F)))
				break;
			res += C / step;
			left -= C;
			step += F;
		}
		res += X/ step;
		cout << "Case #" << idx << ": " << res <<endl;
		fout << "Case #" << idx << ": " << res <<endl;
	}
}
