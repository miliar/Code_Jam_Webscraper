#include <iostream>
#include <string>

using namespace std;


int main ()
{
	int T;
	string s;
	
	cerr << "Hello Ominos!!" << endl;

	cin >> T;
	cerr << T << " test cases" << endl;
	
	
	for (int i=1; i<=T; i++){
		int x, r, c;
		string s("blah");
		cin >> x >> r >> c;
		
		cerr << "#" << i << " = " << x << r << c << endl;
		
		switch (x) {
			case 1 : s = "GABRIEL";
				break;
			case 2 : 	if ( (r*c)%2 == 1 )
									s = "RICHARD";
								else
									s = "GABRIEL";
				break;
			case 3 : 	if ( (r==3 && c >= 2) || 
			 							 (c==3 && r >= 2) )
										s = "GABRIEL";
								else
										s = "RICHARD";
				break;
			case 4 : 	if ( (r==3 && c == 4) || 
				 						 (r==4 && c == 3) || 
										 (r==4 && c == 4))
											s = "GABRIEL";
									else
											s = "RICHARD";
				break;
			default:
								cerr << "X OUT OF BOUNDS!!" << endl;
				break;
		}
		
		
		cout << "Case #" << i << ": " << s << endl;
	}
	

	return 0;
}
