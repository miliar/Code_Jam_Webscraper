#include <iostream>
#include <string>
#include <deque>

using namespace std;


int main ()
{
	int T;
	string s;
	
	//cerr << "Hello World!!" << endl;

	cin >> T;
	//cerr << T << " Test Cases" << endl;
	
	for (int i=1; i<=T; i++){
		cin >> s;
		//cerr << "s = " << s << endl;
		
		deque<char> res;
		
		res.push_back(s[0]);
		
		for (int k=1; k < s.size(); k++){
			if(s[k] >= res.front()){
				res.push_front(s[k]);
			}
			else{
				res.push_back(s[k]);
			}
		}
		
		cout << "Case #" << i << ": ";
		for(int k = 0; k<res.size(); k++) cout << res[k];
		cout << endl;
		
	}
	

	return 0;
}
