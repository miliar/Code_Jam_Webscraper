#include<iostream>
#include<fstream>

using namespace std;

int isFlag(int flag[]){
	for (int i = 0; i < 10; i++){ if (flag[i] == 0) return 0; }
	return 1;
}

void main(){
	ifstream in;
	ofstream out;
	in.open("A-large.in");
	out.open("p_1.out");
	int t;
	in >> t;
	for (int i = 1; i <= t;i++){
		int n, flag[10] = { 0 };
		in >> n;
		if (n != 0){
			int j;
			for (j = 1; !isFlag(flag);j++){
				int temp = n * j;
				while (temp > 0){
					flag[temp % 10] = 1;
					temp /= 10;
				}
			}
			out << "Case #" << i << ": " << n*(j-1) << endl;
		}
		else out << "Case #" << i << ": INSOMNIA" << endl;
	}
	in.close();
	out.close();
}