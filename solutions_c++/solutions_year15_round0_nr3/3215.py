#include <iostream>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int ml(int a, int b){
	if (a == 1 || b == 1 || a  == -1 || b == -1) return a*b;
	else if (a == 2){
		if (b == 2) return -1;
		else if(b == 3) return 4;
		else if(b == 4) return -3;
	}
	else if (a == 3){
		if (b == 2) return -4;
		else if(b == 3) return -1;
		else if(b == 4) return 2;
	}
	else if (a == 4){
		if (b == 2) return 3;
		else if(b == 3) return -2;
		else if(b == 4) return -1;
	}
	else if (a == -2){
		if (b == 2) return 1;
		else if(b == 3) return -4;
		else if(b == 4) return 3;
	}
	else if (a == -3){
		if (b == 2) return 4;
		else if(b == 3) return 1;
		else if(b == 4) return -2;
	}
	else if (a == -4){
		if (b == 2) return -3;
		else if(b == 3) return 2;
		else if(b == 4) return 1;
	}
	return 0;
}

int main(){

	int n, l, x, res1, res2, res3, mult, j;
	char aux;
	cin >> n;
	vector<int> inteiros(10200);

	for (int i = 0; i < n; i ++){
		cin >> l >> x;
		for (int j = 0; j < l; j ++){
			cin >> aux;
			if (aux == 'i') inteiros[j] = 2;
			else if(aux == 'j') inteiros[j] = 3;
			else if(aux == 'k') inteiros[j] = 4;
		}

		res1 = 0, res2 = 0, res3 = 0, mult = 1;
		for (j = 0; j < l*x; j++){
			if (res1 == 0){
				mult = ml(mult, inteiros[j%l]);
				if (mult == 2){ res1 = 1; mult = 1;}
			}
			else if(res2 == 0){
				mult = ml(mult, inteiros[j%l]);
				if (mult == 3){ res2 = 1; mult = 1;}
			}
			else if(res3 == 0){
				mult = ml(mult, inteiros[j%l]);
				if (mult == 4){ res3 = 1; mult = 1;}
			}
			else if (res3 == 1){
				mult = ml(mult, inteiros[j%l]);
			}

		}
		if (res3 == 1 and mult == 1){
			cout << "Case #" << i+1 << ": " << "YES" << endl;
		}
		else cout << "Case #" << i+1 << ": " << "NO" << endl;
	}

	return 0;
}
