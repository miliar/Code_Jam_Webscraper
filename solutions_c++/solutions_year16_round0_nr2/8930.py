#include <iostream>
#include <string>

using namespace std;

int main ()
{
	int T;
	string s;
	
	cerr << "Hello Revange of Pancakes!!" << endl;

	cin >> T;
	cerr << T << " Test Cases" << endl;
	
	for (int i=1; i<=T; i++){
		cin >> s;
		cerr << "s = " << s << endl;
		
		int count = 0;
		for(int k=1; k < s.size(); k++){
			if ( s[k] != s[k-1] ) 
				count++;
		}
		if ( s[s.size()-1] == '-') 
			count++;
		
			cout << "Case #" << i << ": " << count << endl;
	}
	

	return 0;
}
