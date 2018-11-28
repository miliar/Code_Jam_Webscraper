#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <array>
#include <math.h>
#include <cmath>
#include <iomanip>

using namespace std;

#define For(i,m,n) for(int i=m; i<n; i++)


char mult(char m, char n) {
	if (m == '1') return n;
	if (n == '1') return m;
	if (m == 'i') {
		if (n == 'i') return '1';
		if (n == 'j') return 'k';
		if (n == 'k') return 'j';
	}
	if (m == 'j') {
		if (n == 'i') return 'k';
		if (n == 'j') return '1';
		if (n == 'k') return 'i';
	}
	if (m == 'k') {
		if (n == 'i') return 'j';
		if (n == 'j') return 'i';
		if (n == 'k') return '1';
	}
	
}

int sig(char m, char n) {
	if (m == '1') return 1;
	if (n == '1') return 1;
	if (m == 'i') {
		if (n == 'i') return -1;
		if (n == 'j') return 1;
		if (n == 'k') return -1;
	}
	if (m == 'j') {
		if (n == 'i') return -1;
		if (n == 'j') return -1;
		if (n == 'k') return 1;
	}
	if (m == 'k') {
		if (n == 'i') return 1;
		if (n == 'j') return -1;
		if (n == 'k') return -1;
	}
		
}


int main() {
	bool isSmall = true;
	if (isSmall) {
		//freopen("practice.txt","rt",stdin);
		freopen("C-small-attempt0.in","rt",stdin);
		freopen("C-small.out","wt",stdout);
	}
	else {
		freopen("C-large-practice.in","rt",stdin);
		freopen("C-large.out","wt",stdout);
	}
	
	int T;
	cin >> T;
	
	int L, X;
	string input0, input;
	For(caseNum,1,T+1) {
		printf("Case #%d: ", caseNum);
		cin >> L >> X;
		cin >> input0;
		input = "";
		For(i,0,X) {
			input += input0;
		}
		char prod = '1';
		int sign = 1;
		char p;
		For(i,0,L*X) {
			p = mult(prod,input[i]);
			sign = sign*sig(prod,input[i]);
			prod = p;
		}
		if (sign == 1 || prod != '1') {
			
		}
		else {
			char prodi = '1';
			int signi = 1;
			char pi;
			For(i,0,L*X-2) {
				pi = mult(prodi,input[i]);
				signi = signi*sig(prodi,input[i]);
				prodi = pi;
				if (signi == 1 && prodi == 'i') {
					char prodj = '1';
					int signj = 1;
					char pj;
					For(j,i+1,L*X-1) {
						pj = mult(prodj,input[j]);
						signj = signj*sig(prodj,input[j]);
						prodj = pj;
						if (signj == 1 && prodj == 'j') {
							cout << "YES" << endl;
							goto END;
						}
					}
				}
			}
		}
		cout << "NO" << endl;
		END:;
		
		
	}
	

	return 0;
	
}
