// first.cpp: определяет точку входа для консольного приложения.
//

#include <iostream>
#include <fstream>
using namespace std;

int sleepB(long long Num){
	bool a[10] = { 0 };
	bool flag = true;
	int n = 0;
	int j = 1;
	while (flag){
		if (Num == 0) flag = false;
		long long N = Num * j;
		while (N){
			for (int i = 0; i < 10; ++i){
				if (!a[i] && N % 10 == i) {
					a[i] = true;
				}
			}
			N /= 10;
		}
		for (int i = 0; i < 10; ++i){
			if (a[i]) n++;
		}
		n == 10 ? flag = false : n = 0;
		j++;
	}
	return Num*(j-1);
}

int main()
{
	int T = 0;
	long long N = 0;
	ifstream f("D:\\A-large.in", ios_base::in);
	ofstream out("D:\\output.txt", ios_base::out);
	f >> T;
	for (int i = 0; i < T; ++i){
		f >> N;
		N = sleepB(N);
		N == 0 ? out << "Case #" << i + 1 << ": INSOMNIA" << endl : out << "Case #" << i + 1 << ": " << N << endl;
	}
	f.close();
	out.close();
	return 0;
}

