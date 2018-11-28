#include <iostream>
#include <string>

using namespace std;



int main(int argc, char* argv[]) 
{


	int cases, sLength, pointer, flip;
	bool isHappy;
	string s;
	cin >> cases;
	for(int i=1; i<=cases; i++) {
		cin >> s;
		sLength = s.length();

		pointer = 0;
		flip = 0;
		isHappy = (s[0] == '+') ? true : false;

		while(pointer != sLength) {
			if(s[pointer] == '-' && !isHappy) {
				pointer++;
			} else if(s[pointer] == '+' && !isHappy) {
				
				flip++;
				pointer++;

				isHappy = true;

			} else if(s[pointer] == '+' && isHappy) {
				pointer++;
				
			} else if(s[pointer] == '-' && isHappy) {
				flip++;
				pointer++;
				isHappy = false;
			}
			
		}

		if(!isHappy) {
			flip++;
		}

		cout << "Case #" << i << ": " << flip << "\n";
	}
	

}