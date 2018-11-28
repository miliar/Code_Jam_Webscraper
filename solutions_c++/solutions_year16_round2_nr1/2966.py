#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

inline int letterToNum(char c){
	return c - 'A';
}

inline char intToChar(int i){
	return i + 'A';
}


int main(){
	//ifstream in("in.txt");
	ifstream in("A-large.in");
	//ifstream in("A-small-attempt1.in");
	ofstream out("out.txt");
	
	unsigned cases(0), size(0), n(0);
	in >> cases;
	for(int c = 1; c <= cases; ++c){
		vector<int> letters(26,0);
		vector<int> answ;
		int letterCount = 0;
		string s;
		in >> s;
		for(size_t i = 0; i < s.length(); ++ i){
			letters[letterToNum(s[i])]++;
			letterCount++;
		}

		out << "Case #" << c << ": " ;

		while(letterCount > 0){
			if (false){}

			else if(letters[letterToNum('Z')] > 0 && letters[letterToNum('E')] > 0 && letters[letterToNum('R')] > 0 && letters[letterToNum('O')] > 0){
				letters[letterToNum('Z')]--;
				letters[letterToNum('E')]--;
				letters[letterToNum('R')]--;
				letters[letterToNum('O')]--;
				letterCount -= 4;
				answ.push_back(0);
				continue;
			} 

			else if(letters[letterToNum('F')] > 0 && letters[letterToNum('O')] > 0 && letters[letterToNum('R')] > 0 && letters[letterToNum('U')] > 0){
				letters[letterToNum('F')]--;
				letters[letterToNum('U')]--;
				letters[letterToNum('R')]--;
				letters[letterToNum('O')]--;
				letterCount -= 4;
				answ.push_back(4);
				continue;
			}

			else if(letters[letterToNum('S')] > 0 && letters[letterToNum('I')] > 0 && letters[letterToNum('X')] > 0 ){
				letters[letterToNum('S')]--;
				letters[letterToNum('I')]--;
				letters[letterToNum('X')]--;
				letterCount -= 3;
				answ.push_back(6);
				continue;
			}

			else if(letters[letterToNum('E')] > 0 && letters[letterToNum('I')] > 0 && letters[letterToNum('G')] > 0 && letters[letterToNum('H')] > 0 && letters[letterToNum('T')] > 0){
				letters[letterToNum('E')]--;
				letters[letterToNum('I')]--;
				letters[letterToNum('G')]--;
				letters[letterToNum('H')]--;
				letters[letterToNum('T')]--;
				letterCount -= 5;
				answ.push_back(8);
				continue;
			}
			else if(letters[letterToNum('S')] > 0 && letters[letterToNum('V')] > 0 && letters[letterToNum('N')] > 0 && letters[letterToNum('E')] > 1){
				letters[letterToNum('S')]--;
				letters[letterToNum('V')]--;
				letters[letterToNum('N')]--;
				letters[letterToNum('E')]-= 2;
				letterCount -= 5;
				answ.push_back(7);
				continue;
			}

			else if(letters[letterToNum('F')] > 0 && letters[letterToNum('E')] > 0 && letters[letterToNum('I')] > 0 && letters[letterToNum('V')] > 0){
				letters[letterToNum('F')]--;
				letters[letterToNum('E')]--;
				letters[letterToNum('I')]--;
				letters[letterToNum('V')]--;
				letterCount -= 4;
				answ.push_back(5);
				continue;
			}

					else if(letters[letterToNum('I')] > 0 && letters[letterToNum('E')] > 0 && letters[letterToNum('N')] > 1){
				letters[letterToNum('N')]-= 2;
				letters[letterToNum('I')]--;
				letters[letterToNum('E')]-= 1;
				letterCount -= 4;
				answ.push_back(9);
				continue;
			}
					else if(letters[letterToNum('T')] > 0 && letters[letterToNum('W')] > 0 && letters[letterToNum('O')] > 0 ){
				letters[letterToNum('T')]--;
				letters[letterToNum('W')]--;
				letters[letterToNum('O')]--;
				letterCount -= 3;
				answ.push_back(2);
				continue;
			}

			else if(letters[letterToNum('T')] > 0 && letters[letterToNum('H')] > 0 && letters[letterToNum('R')] > 0 && letters[letterToNum('E')] > 1){
				letters[letterToNum('T')]--;
				letters[letterToNum('H')]--;
				letters[letterToNum('R')]--;
				letters[letterToNum('E')]-= 2;
				letterCount -= 5;
				answ.push_back(3);
				continue;
			}
			
			
			
			else if(letters[letterToNum('O')] > 0 && letters[letterToNum('E')] > 0 && letters[letterToNum('N')] > 0 ){
				letters[letterToNum('N')]--;
				letters[letterToNum('E')]--;
				letters[letterToNum('O')]--;
				letterCount -= 3;
				answ.push_back(1);
				continue;
			}
				
			
			
			
			
			
			

		}

		sort(answ.begin(), answ.end());
		for(int i = 0; i < answ.size(); ++ i){
			out << answ[i];
		}
		
		out << "\n";
		out.flush();
	}
	out.flush();
	return 0;
}