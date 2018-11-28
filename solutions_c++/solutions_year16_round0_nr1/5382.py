#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <sstream>
#include <string>
#include <array>

using namespace std;

int length(int N) {
	int length = 0;
	while (N > 0) {
		length++;
		N /= 10;
	}
	return length;
}

int des(int n) {
	int des = 1;
	if (n > 0)
		for (int i = 1; i <= n; i++) {
			des *= 10;
		}
	return des;
}

int invert(int num) {
	int res = 0;
	while (num > 0)
	{
		res = res * 10 + (num % 10);
		num = num / 10;
	}
	return res;
}

bool check(array<bool, 10>& n) {
	for each (bool b in n) {
		if (b == false)
			return false;
	}
	return true;
}

int main()
{
	//ifstream in("input.in");
	ifstream in("A-large.in");
	ofstream out("output.out");
	
/*
			in >> R;
			in >> C;
			in >> W;
			x = C / W;
			z = C % W;
			y = 0;
			if (z > 0) y++;
			result = W + x - 1 + y;

			result += (R - 1) * x;
	*/
	///*unsigned long*/ int T, R, C, W, x, z, y, result;
	/*unsigned long*/ long int T, N, n;
	string number, result;
	bool ins;
	array<bool, 10> num;
	if (in.is_open()){
		in >> T;
		
		for (int i = 1; i <= T; i++){
			
			ins = 0;
			in >> N;
			if (N == 0) {
				result = "INSOMNIA";
			}
			else {
				n = N;
				num = { { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 } };
				for (;;) {
					number = to_string(n);
					for each (char c in number) {
						switch (c) {
						case '0': num[0] = 1;
							break;
						case '1': num[1] = 1;
							break;
						case '2': num[2] = 1;
							break;
						case '3': num[3] = 1;
							break;
						case '4': num[4] = 1;
							break;
						case '5': num[5] = 1;
							break;
						case '6': num[6] = 1;
							break;
						case '7': num[7] = 1;
							break;
						case '8': num[8] = 1;
							break;
						case '9': num[9] = 1;
							break;
						}
						if (check(num))
							break;
					}
					result = number;
					if (check(num))
						break;
					n += N;
				}
			}
			out << "Case #" << i << ": " << result << endl;
		}
		in.close();
	}
	out.close();
	return 0;
}