//*********************************************
//
//	Elijah Rippeth
//	elijah.rippeth@gmail.com
//	10 April 2015
//	Google Code Jam
//	Standing Ovation
//
//*********************************************


#include <iostream>
#include <string>

using namespace std;

int main()
{
	int test_cases, Smax, count;
	cin >> test_cases;

	for(int i = 0; i < test_cases; i++) {
		int count = 0, 
		    stand_count = 0;
		cin >> Smax;
		cin.get();
		for(size_t j = 0; j < Smax+1; j++) {
			char person_j;
			cin >> person_j;
			
			if(j > stand_count) {
				count+=(j - stand_count);
				stand_count+=(j - stand_count);
			}
			stand_count += (person_j - '0');	
		}
		cout << "Case #" << i+1 << ": " << count << endl;
	}

	return 0;
}