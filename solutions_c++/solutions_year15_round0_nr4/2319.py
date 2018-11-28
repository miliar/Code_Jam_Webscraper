#include <iostream>
using namespace std;
void gw(){
	cout << "GABRIEL" << endl;
	}

void rw(){
	cout << "RICHARD" << endl;
}
int main()

{
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);
	int t,x, r, c;
	cin >> t;
	for (int cases = 1; cases <= t; cases++){
				cin >> x >> r >> c;
				cout << "Case #" << cases << ": ";
				if ( (r*c)%x!=0)	rw();
				else{
					if (x == 1 || x == 2 ) gw();
					else if (x < 7){
						if (r >=x-1 && c>= x-1) gw();
						else rw();
					}
					else rw();
					
				}
				
	}
		return 0;
}