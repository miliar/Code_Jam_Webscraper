#include <cstdlib>
#include <vector>
#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

char mult(char a, char b) {
	short sgn=1;
	if (a=='e' || a=='f' || a=='g' || a=='h') {
		sgn*=-1;
		a+=4;
	}
	if (b=='e' || b=='f' || b=='g' || b=='h') {
		sgn*=-1;
		b+=4;
	}
	//cout << a << b << sgn;
	char r;
	if (a=='l') {
		if (b=='l') {
			r='l';
		}
		if (b=='i') {
			r='i';
		}
		if (b=='j') {
			r='j';
		}
		if (b=='k') {
			r='k';
		}
	}
	if (a=='i') {
		if (b=='l') {
			r='i';
		}
		if (b=='i') {
			r='h';
		}
		if (b=='j') {
			r='k';
		}
		if (b=='k') {
			r='f';
		}
	}
	if (a=='j') {
		if (b=='l') {
			r='j';
		}
		if (b=='i') {
			r='g';
		}
		if (b=='j') {
			r='h';
		}
		if (b=='k') {
			r='i';
		}
	}
	if (a=='k') {
		if (b=='l') {
			r='k';
		}
		if (b=='i') {
			r='j';
		}
		if (b=='j') {
			r='e';
		}
		if (b=='k') {
			r='h';
		}
	}
	//cout << r;
	if (sgn == 1) return r;
	else if (r<'i') return r+4; else return r-4;
}


int main(int argc, char** argv) {
	int T;
	cin >> T;
	for (int n=0;n<T;n++) {
		int l,x;
		string L;
		cin >> l >> x;
		cin >> L;
		vector <char> rl (x,'l');
		/*
		for (int i=0;i<l;i++) {
			for (int j=0;j<l;j++) {
				rl[i] = mult(rl[i],L[j%l]);
			}
		}*/
		char r1='l';
		for (int i=0;i<=l*4 && i<l*x;i++) {
			r1=mult(r1,L[i%l]);
			if (r1=='i') {
				char r2='l';
				for (int j=i+1;j<=i+1+l*4 && i<l*x;j++) {
					r2=mult(r2,L[j%l]);
					if (r2=='j') {
						char r3='l';
						for (int k=j+1;k<l*x;k++) {
							r3 = mult(r3,L[k%l]);
						}
		//printf("%d %d %d\n",r1,r2,r3);
						if (r3=='k') {
							printf("Case #%d: YES\n",n+1);
							goto brk;
						}
					}
				}
			}
		}
		printf("Case #%d: NO\n",n+1);
		brk:;
	}

	return 0;
}

