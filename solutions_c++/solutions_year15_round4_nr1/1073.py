#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm>
#include <math.h>
#include <set>
using namespace std;
ifstream in("in.txt");
ofstream out("out.txt");
int t;
int r,c;
int g;
vector <string> s;
int main() {
	out.setf(ios::fixed);
	out.precision(6);
	in >> t;
	for (int i=1;i<=t;i++) {
		g = 0;
		bool z = true;
		in >> r >> c;
		s.resize(r);
		for (int j=0;j<r;j++) {
			in >> s[j];
		}
		for (int j=0;j<r;j++) for (int k=0;k<c;k++) if (s[j][k]=='>' || s[j][k]=='v' || s[j][k]=='^' || s[j][k]=='<') {
			if (s[j][k]=='>') {
				bool f = true;
				for (int l=k+1;f && l<c;l++) {
						if (s[j][l]=='>' || s[j][l]=='v' || s[j][l]=='^' || s[j][l]=='<') {
							f = false;
						}
					}
				if (f) {
					g++;
					for (int l=k+1;f && l<c;l++) {
						if (s[j][l]=='>' || s[j][l]=='v' || s[j][l]=='^' || s[j][l]=='<') {
							f = false;
						}
					}
					for (int l=k-1;f && l>=0;l--) {
						if (s[j][l]=='>' || s[j][l]=='v' || s[j][l]=='^' || s[j][l]=='<') {
							f = false;
						}
					}
					for (int l=j+1;f && l<r;l++) {
						if (s[l][k]=='>' || s[l][k]=='v' || s[l][k]=='^' || s[l][k]=='<') {
							f = false;
						}
					}
					for (int l=j-1;f && l>=0;l--) {
						if (s[l][k]=='>' || s[l][k]=='v' || s[l][k]=='^' || s[l][k]=='<') {
							f = false;
						}
					}
					if (f) z = false;
				}
			} else if (s[j][k]=='v') {
				bool f = true;
				for (int l=j+1;f && l<r;l++) {
						if (s[l][k]=='>' || s[l][k]=='v' || s[l][k]=='^' || s[l][k]=='<') {
							f = false;
						}
					}
				if (f) {
					g++;
					for (int l=k+1;f && l<c;l++) {
						if (s[j][l]=='>' || s[j][l]=='v' || s[j][l]=='^' || s[j][l]=='<') {
							f = false;
						}
					}
					for (int l=k-1;f && l>=0;l--) {
						if (s[j][l]=='>' || s[j][l]=='v' || s[j][l]=='^' || s[j][l]=='<') {
							f = false;
						}
					}
					for (int l=j+1;f && l<r;l++) {
						if (s[l][k]=='>' || s[l][k]=='v' || s[l][k]=='^' || s[l][k]=='<') {
							f = false;
						}
					}
					for (int l=j-1;f && l>=0;l--) {
						if (s[l][k]=='>' || s[l][k]=='v' || s[l][k]=='^' || s[l][k]=='<') {
							f = false;
						}
					}
					if (f) z = false;
				}
			} else if (s[j][k]=='^') {
				bool f = true;
				for (int l=j-1;f && l>=0;l--) {
						if (s[l][k]=='>' || s[l][k]=='v' || s[l][k]=='^' || s[l][k]=='<') {
							f = false;
						}
					}
				if (f) {
					g++;
					for (int l=k+1;f && l<c;l++) {
						if (s[j][l]=='>' || s[j][l]=='v' || s[j][l]=='^' || s[j][l]=='<') {
							f = false;
						}
					}
					for (int l=k-1;f && l>=0;l--) {
						if (s[j][l]=='>' || s[j][l]=='v' || s[j][l]=='^' || s[j][l]=='<') {
							f = false;
						}
					}
					for (int l=j+1;f && l<r;l++) {
						if (s[l][k]=='>' || s[l][k]=='v' || s[l][k]=='^' || s[l][k]=='<') {
							f = false;
						}
					}
					for (int l=j-1;f && l>=0;l--) {
						if (s[l][k]=='>' || s[l][k]=='v' || s[l][k]=='^' || s[l][k]=='<') {
							f = false;
						}
					}
					if (f) z = false;
				}
			} else if (s[j][k]=='<') {
				bool f = true;
				for (int l=k-1;f && l>=0;l--) {
						if (s[j][l]=='>' || s[j][l]=='v' || s[j][l]=='^' || s[j][l]=='<') {
							f = false;
						}
					}
				if (f) {
					g++;
					for (int l=k+1;f && l<c;l++) {
						if (s[j][l]=='>' || s[j][l]=='v' || s[j][l]=='^' || s[j][l]=='<') {
							f = false;
						}
					}
					for (int l=k-1;f && l>=0;l--) {
						if (s[j][l]=='>' || s[j][l]=='v' || s[j][l]=='^' || s[j][l]=='<') {
							f = false;
						}
					}
					for (int l=j+1;f && l<r;l++) {
						if (s[l][k]=='>' || s[l][k]=='v' || s[l][k]=='^' || s[l][k]=='<') {
							f = false;
						}
					}
					for (int l=j-1;f && l>=0;l--) {
						if (s[l][k]=='>' || s[l][k]=='v' || s[l][k]=='^' || s[l][k]=='<') {
							f = false;
						}
					}
					if (f) z = false;
				}
			}
		}
		if (z) out << "Case #" << i << ": " << g << "\n";
		else out << "Case #" << i << ": " << "IMPOSSIBLE" << "\n";
	}
	return 0;
}
