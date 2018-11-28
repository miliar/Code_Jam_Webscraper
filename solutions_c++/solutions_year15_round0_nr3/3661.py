#include <fstream>
#include <cmath>
using namespace std;

//i=2 j=3 k=4

int eval(int x, int y){
	int sign=1;
	if (x<0) sign=-1;
	x=abs(x);
	if (x==1) return y*sign;
	if (y==1) return x*sign;
	if (x==2){ //i
		if (y==2) return -1*sign;
		if (y==3) return 4*sign;
		if (y==4) return -3*sign;
	}
	if (x==3){ //j
		if (y==2) return -4*sign;
		if (y==3) return -1*sign;
		if (y==4) return 2*sign;
	}
	if (x==4){ //k
		if (y==2) return 3*sign;
		if (y==3) return -2*sign;
		if (y==4) return -1*sign;
	}
}

int conv(char x){
	if (x=='i') return 2;
	if (x=='j') return 3;
	if (x=='k') return 4;
}

int main(){	
	ifstream in("C-small-attempt2.in");
	ofstream out("out.txt");
	int T, L, X, i, j, k, cur, x, y, current;
	char a[10001];
	in >> T;
	for (i=0; i<T; i++){
		in >> L >> X >> a;
		cur=1;
		current=2;
		for (j=0; j<X; j++){
			for (k=0; k<L; k++){
				cur=eval(cur, conv(a[k]));
				if (cur==current&&current<4){
					cur=1;
					current++;
				}
			}
		}
		out << "Case #" << i+1 << ": ";
		if (cur==4&&current==4) out << "YES\n";
		else out << "NO\n";
	}
    return 0;
}
