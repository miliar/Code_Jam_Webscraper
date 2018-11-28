// countSheep.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int T, N;
	ifstream in;
	in.open("./A-large.in");
	ofstream out;
	out.open("./A-large.out");
	in >> T;
	for (int i = 0; i < T; i ++) {
		in >> N;
		if (N == 0) {
			out << "Case #" << i + 1 << ": INSOMNIA" << endl;
		} else {
			int hitCount = 0;
			int flag[10] = {0};
			for (int j = 1; ; j ++) {
				long tmp = abs(N * j);
				while (tmp != 0) {
					if (flag[tmp%10] == 0) {
						hitCount ++;
						flag[tmp%10] = 1;
					}
					tmp = tmp / 10;
				}
				if (hitCount == 10 ) {
					out << "Case #" << i + 1 << ": " << N * j << endl;
					break;
				}
			}
		}
	}
	in.close();
	out.close();
	return 0;
}

