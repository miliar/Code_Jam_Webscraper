#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{

	short T;
	cin>>T;
	for(short t = 1; t<= T;t++){
		int X,R,C;
		cin>>X>>R>>C;
		if (R > C) 
			swap (R, C);
		bool test = false;
		if((R*C)%X == 0)
		{
			if(X <=2)
				test = true;
			else{
				if (X == 3) {
					if ( (R == 2 && C == 3) || (R == 3 && C >= 3))
						test = true;
				}
				else {
					if (R + C >= 7) 
						test = true;
				}
			}
		}
		cout << "Case #" << t << ": ";
		if (test)
			cout << "GABRIEL";
		else 
			cout << "RICHARD";
		cout << endl;
	}
	return 0;
}