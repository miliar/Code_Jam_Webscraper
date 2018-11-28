#include <iostream>
#include <algorithm>
#include <string>


using namespace std;

int main(){

	int t, x, c, r, grid[20][20];
	string result;
	cin >> t;

	for(int tt = 1; tt <= t; tt++){	

		cin >> x >> c >> r;

		if((r*c)%x != 0) result = "RICHARD";
		else
			if(x <= 2) result = "GABRIEL";
			else
				if(x == 3){
					if((r == 1)or(c == 1)) result = "RICHARD";
					else result = "GABRIEL";
				}
				if(x == 4){
					if(((r < 4)and(c < 4))or(r <= 2)or(c <= 2)) result = "RICHARD";
					else result = "GABRIEL";
					
				}
		cout << "Case #" << tt << ": " << result << endl;
	}

	return 0;
}