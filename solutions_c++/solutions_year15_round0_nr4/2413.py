#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;

int main(){
	ifstream in("C:\\Users\\Mohammad\\Desktop\\CodeJam\\D-small-attempt2.in");
	ofstream out("C:\\Users\\Mohammad\\Desktop\\CodeJam\\output.txt");
	
	int T;
	in >> T;

	for (int i = 1; i <= T; i++){
		int x,r,c;
		in >> x;
		in >> r;
		in >> c;
		int flag = 0, half;
		int area = r*c, Max = max(r, c), Min = min(r, c);

		if (x % 2 == 0)
			half = x / 2;
		else
			half = x / 2 + 1;

		if (x>Max || (x + 1) / 2>Min || area%x != 0 || (x == 4 && 3>Min))
			flag = 1;

		if (flag)
			out << "Case #" << i << ": RICHARD" << endl;
		else
			out << "Case #" << i << ": GABRIEL" << endl;
	}
}