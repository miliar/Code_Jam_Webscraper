#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#include<cmath>
#include<fstream>
#include <iostream>

using namespace std;

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	int T, i;
	in >> T;

	for (i = 1; i <= T; i++){
		int x, r, c;
		string ans = "RICHARD";
		in >> x >> r >> c;

		if (x == 2){
			if ((r*c) % 2 == 0) ans = "GABRIEL";
			else ans = "RICHARD";
		}
		else if (x == 3){
			if ((r*c) == 6){
				if (r == 1 || c == 1) ans = "RICHARD";
				else ans = "GABRIEL";
			}
			else if ((r*c) == 9){
				if (r == 1 || c == 1) ans = "RICHARD";
				else ans = "GABRIEL";
			}		
			else if ((r*c) == 12){
				if (r == 1 || c == 1) ans = "RICHARD";
				else ans = "GABRIEL";
			}
			else if ((r*c) == 15){
				if (r == 1 || c == 1) ans = "RICHARD";
				else ans = "GABRIEL";
			}
			else{
				ans = "RICHARD";
			}
		}
		else if (x == 4){
			if ((r*c) == 4){
				ans = "RICHARD";				
			}
			else if ((r*c) == 8){
				if (r == 1 || c == 1) ans = "RICHARD";
				else if (r == 2 || c == 2) ans = "RICHARD";
				else ans = "GABRIEL";
			}
			else if ((r*c) == 12){
				if (r == 1 || c == 1) ans = "RICHARD";
				else if (r == 2 || c == 2) ans = "RICHARD";
				else ans = "GABRIEL";
			}
			else if ((r*c) == 16){
				if (r == 1 || c == 1) ans = "RICHARD";
				else if (r == 2 || c == 2) ans = "RICHARD";
				else ans = "GABRIEL";
			}
		}
		else{
			ans = "GABRIEL";
		}
		
		out << "Case #"<<i<<": "<<ans<< endl;

	}

	in.close();
	out.close();
	return 0;
}