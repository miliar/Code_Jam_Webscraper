#include <iostream>
#include <vector>
#include <map>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stack>
#include <math.h>

using namespace std;

int main(){
	int T;
	bool is_happy_face;
	cin >> T;
	stack<char> S;
	string s;
	char ch;
	cerr << "T: " << T << endl;

	for(int X = 1; X <= T; X++){
		cin >> s;
		cerr << "Original String: " << s << endl;
		
		//Insert the chars into stack
		for(int i = s.length() - 1; i >= 0; i--){
			S.push(s[i]);
		}

		for(int moves = 0; moves < 1000 ; moves++){
			stack<char> flipped;
			//Check if stack is already all happy face
			is_happy_face = true;
			cerr << "String before move # " << moves << ": " ;
			for(int i = 0; i < s.length(); i++){
				ch = S.top();
				cerr << ch ;
				if(ch == '-'){
					is_happy_face = false;
				}
				flipped.push(ch);
				S.pop();
			}
			cerr << endl;
			//If all are not happy faces then move
			if(is_happy_face){
				cout << "Case #" << X << ": " << moves << endl;
				break;
			}else{
				//Copy the elements back to original stack
				for(int i = 0; i < s.length(); i++){
                	ch = flipped.top();
                	S.push(ch);
					flipped.pop();
            	}

				//Find the top elements to flip
				cerr << "Top elements to flip: ";
				char firstElement = S.top();
				stack<char> temp;
				int elements_moved = 0;
				for(int i = 0; i < s.length(); i++){
					if(ch != S.top()){
						break;
					}
					cerr << S.top();
                	temp.push(S.top());
					S.pop();
					elements_moved++;
            	}
				cerr << ", S Size: "<< S.size() << ", temp Size: " << temp.size() << endl;
				
				//Copy the pan cakes back to original stack after flipping the faces
				cerr << "Copying back to the original stack" << endl;
				for(int i = 0; i < elements_moved; i++){
					temp.top() = (temp.top() == '+') ? '-' : '+';
					S.push(temp.top());
					temp.pop();
				}
				cerr << "Size at the end of move # "<< moves <<": S Size: " << S.size() << ", temp Size: " << temp.size() << endl;
			}
		}
	}
	return 0;
}
