#include <iostream>

using namespace std;

bool solve(int x, int r, int c){
	if((r*c)%x != 0) 
		return false;
	if(x > 2 && (r == 1 || c == 1))
		return false;
	if(x==4 && (r==2 || c==2))
		return false;
	return true;	
}


int main(){
	int t;
	int * x, * r, * c;
	
	cin >> t;
	x = new int[t];
	r = new int[t];
	c = new int[t];
	
	for(int i=0; i<t; i++)
		cin >> x[i] >> r[i] >> c[i];
	
	for(int i=0; i<t; i++){
		cout << "Case #" << i+1 << ": ";
		if(solve(x[i], r[i], c[i]))	
			cout << "GABRIEL" << endl;
		else
			cout << "RICHARD" << endl;
	}

return 0;
}