// AlienTimetoDoom.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"

#include <fstream>
#include <iostream>
#include <math.h>
#include <string>
#include <algorithm>
#include <sstream>
#include <array>

#define ffor(a,b,c)  for(int a=b;a<c;a++)

std::string stemp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";



int main()
{


	int T;

	std::ifstream infile("a.txt");
	std::ofstream outfile("b.txt");


	infile >> T;

	for (int iy = 1; iy <= T; iy++) {
		if (iy == 4) {
			iy = iy;

		}
		int N;
		infile >> N;
		std::array<int, 28> p;
		int order[1000];

		int sens = 0;
		ffor(i, 0, N) { infile >> p[i];
					sens += p[i];

		}

		std::string output= "";
		while (sens > 0) {
			int mmax = 0;			int maxid = -1;
			int mmax2 = 0;		int maxid2 = -1;
			ffor(i, 0, N) {
				if (p[i] > mmax) { mmax = p[i]; maxid = i; }
			}
			ffor(i, 0, N) {
				if (i != maxid) {
					if (p[i] > mmax2) { mmax2 = p[i]; maxid2 = i; }
				}}
			if (p[maxid] >= 1) {
				p[maxid]--;
				sens--;
	
				output = output + stemp[maxid];
				bool viol = false;
				ffor( j,0, N) {
					if (p[j] > (sens >> 1)) viol = true;
				}

				if(viol){
					p[maxid2]--;
					sens--;

					output = output + stemp[maxid2];}
				output = output + " ";
			}
		}
		std::cout << iy << ": " << output << std::endl;
		outfile << "case #" << iy << ": " << output << std::endl;


	}


	getchar();
	getchar();

	return 0;
}

