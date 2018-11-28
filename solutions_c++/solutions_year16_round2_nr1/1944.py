#include <iostream>

void process(std::string s){
	int letters[10];
	for(int i=0; i<10; i++){
		letters[i]=0;
	}

	for(size_t i; i<s.length(); i++){
		switch(s[i]){
			case 'Z':
				letters[0]++;
				break;
			case 'N':
				letters[1]++;
				break;
			case 'W':
				letters[2]++;
				break;
			case 'H':
				letters[3]++;
				break;
			case 'F':
				letters[4]++;
				break;
			case 'V':
				letters[5]++;
				break;
			case 'X':
				letters[6]++;
				break;
			case 'S':
				letters[7]++;
				break;
			case 'G':
				letters[8]++;
				break;
			case 'I':
				letters[9]++;
				break;
			default:
				break;
		}
	}
	letters[7]-=letters[6];
	letters[5]-=letters[7];
	letters[4]-=letters[5];
	letters[3]-=letters[8];
	letters[9]-=(letters[8]+letters[6]+letters[5]);
	letters[1]-=(letters[7]+letters[9]*2);

	for(int i=0; i<10; i++){
		for(int j=0; j<letters[i]; j++){
			std::cout << i;
		}
	}
	std::cout << std::endl;
}

int main(){
	int cases;
	std::cin >> cases;
	std::string s;
	std::getline(std::cin, s);

	for(int i=0; i<cases; i++){
		std::string input;
		std::getline(std::cin, input);
		std::cout << "Case #" << i+1 << ": ";
		process(input);
	}
}
