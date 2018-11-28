#include <iostream>
#include <vector>
#include <map>
#include <cstdio>
#include <stack>
#include <math.h>
#include <stdlib.h>
#include <queue>
#include <string>
#include <algorithm>
#include <stack>
#include <list>
using std::priority_queue;
using std::cin;
using std::cout;
using std::map;
using std::endl;
using std::vector;
using std::string;
using std::stack;
using std::list;

int maxWidth(int size){
	if (size == 4){
		return 2;
	}
	else if (size == 3){
		return 2;
	}
	else if (size == 2){
		return 2;
	}
	else {
		return 1;
	}
}

int main(){
	int tests;
	cin >> tests;

	for (int i = 0; i < tests; ++i){
		int X, R, C;
		cin >> X >> R >> C;
		bool p = true;
		if (R < X && C < X){
			p = false;
		}
		if (R == 1){
			if (C % X != 0){
				p = false;
			}
			else if (maxWidth(X) > C){
				p = false;
			}
		}
		if (C == 1){
			if (R % X != 0){
				p = false;
			}
			else if (maxWidth(X)  > R){
				p = false;
			}
		}
		if ((C == 3 || R == 3) && X == 3){
			if (C == 3){
				if (R < 2){
					p = false;
				}
			}
			else if (C < 2){
				p = false;
			}
		}
		if ((C == 4 || R == 4) && X == 4){
			if (C == 4){
				if (R < 3){
					p = false;
				}
			}
			else if (C < 3){
				p = false;
			}
		}
		int area = R*C;
		if (area % X != 0){
			p = false;
		}
		
		cout << "Case #" << i + 1 << ": ";
		if (p){
			cout << "GABRIEL";
		}
		else {
			cout << "RICHARD";
		}
		cout << endl;
	}
}