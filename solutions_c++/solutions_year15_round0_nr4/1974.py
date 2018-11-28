#include<iostream>

using namespace std;

int main() {
	int i,j,k,t,x,r,c;
	cin >> t;
	for(k=1;k<=t;k++) {
		cin >> x >> r >> c;
		if(x==1 || x==2)
		{
			if((r*c)%x)	cout << "Case #" << k << ": RICHARD\n";
			else	cout << "Case #" << k << ": GABRIEL\n";
		}
		if(x==3)
		{
			if(r*c == 6 || r*c == 9 || r*c == 12)	cout << "Case #" << k << ": GABRIEL\n";
			else	cout << "Case #" << k << ": RICHARD\n";
		}
		if(x==4)
		{
			if(r*c==12 || r*c==16)	cout << "Case #" << k << ": GABRIEL\n";
			else	cout << "Case #" << k << ": RICHARD\n";
		}
	}
	return 0;
}
