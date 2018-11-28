#include <iostream>
#include <vector>

using namespace std;


std::vector<int>  split(int num) {
	std::vector<int> result;
	int index = 0,
		part = 0;

	while(num) {
		part = num % 10;
		result.push_back(part);
		index++;
		num = num / 10;

	}
	return result;
}

void allFalse(bool * ref) {
	*(ref + 0) = false;
	*(ref + 1) = false;
	*(ref + 2) = false;
	*(ref + 3) = false;
	*(ref + 4) = false;
	*(ref + 5) = false;
	*(ref + 6) = false;
	*(ref + 7) = false;
	*(ref + 8) = false;
	*(ref + 9) = false;
}

bool check(std::vector<int> * v, bool * ref, int * touched) {
	//cout << v << "\n";
	for(std::vector<int>::iterator it = (*v).begin(); it != (*v).end(); ++it) {
    	/* std::cout << *it; ... */

    	if(*(ref+ *it) == false) {
    		*(ref+ *it) = true;
    		*touched = *touched + 1;
    	}
	}
	return (*touched == 10 ? true : false);
}

int main(int argc, char* argv[]) 
{
	int cases, input, result, touched, increment;
	bool referene[10];
	std::vector<int> numbers;
	cin >> cases;

	for(int i=1; i<=cases; i++) {
		allFalse(referene);
		result = 0;
		touched = 0;
		increment = 1;
		cin >> input;

		if(input!=0) {
			while(true) {
				numbers = split(input * increment);

				if(check(&numbers, referene, &touched)) {
					break;
				}
				increment++;	
			}
			cout << "Case #" << i << ": " << input * increment << "\n";

		} else {
			
			cout << "Case #" << i << ": INSOMNIA\n";
		}
		
		
	}
}