#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;
int n_macchine=0;
double C, F, X, t1, t2;

int main(int argc, char **argv)
{
	fstream in, out; int ncase;
	in.open("B-large.in", ios::in); // A-small-attempt0.in
	out.open("output.txt", ios::out);
	
	in >> ncase;
	for(int i=1; i<=ncase; i++) {
		
		in >> C >> F >> X;
		
		t1 = X/2;
		while(1) {
			t2 = t1 + (C - X)/(2+n_macchine*F) + X/(2+(n_macchine+1)*F);
			n_macchine++;
			
			if(t2>t1) // vuol dire che prima diminuiva, ma poi è aumentato, quindi prendere il t1
				break;
			else
				t1 = t2;
		}
		
		out << "Case #" << i << ": " << fixed << setprecision(7) << t1 << endl;
		n_macchine = 0;
		t1 = 0;
		t2 = 0;
	}
	
	
	return 0;
}
