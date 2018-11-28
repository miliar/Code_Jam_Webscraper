#include <stdlib.h>
#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <utility>
#include <algorithm>

#define f(x, y) for(int x = 0; x < y; ++x)

using namespace std;

int check_number(char unique, string exclude, map<char, int> &chars);

int main(){

	int T;
	string S;
	map<char, int> chars;
	pair<char, string> numbers[10];
	int order[10] = {0, 2, 6, 7, 5, 4, 3, 8, 1, 9};
	vector<int> number;

	numbers[0] = make_pair('Z', "ERO");
	numbers[1] = make_pair('W', "TO");
	numbers[2] = make_pair('X', "SI");
	numbers[3] = make_pair('S', "EVEN");
	numbers[4] = make_pair('V', "FIE");
	numbers[5] = make_pair('F', "OUR");
	numbers[6] = make_pair('R', "THEE");
	numbers[7] = make_pair('H', "EIGT");
	numbers[8] = make_pair('O', "NE");
	numbers[9] = make_pair('I', "NNE");


	cin >> T;

	f(x, T){
		number.clear();
		chars.clear();
		cout << "Case #" << (x + 1) << ": ";
		cin >> S;
		f(y, S.size()){
			chars[S[y]]++;
		}
		f(y, 10){
			int qt = check_number(numbers[y].first, numbers[y].second, chars);
			number.insert(number.begin(), qt, order[y]);
		}
		sort(number.begin(), number.end());
		f(y, number.size()){
			cout << number[y];
		}
		cout << endl;
	}

	return 0;
}


int check_number(char unique, string exclude, map<char, int> &chars){

	if(chars[unique] > 0){
		int qt = chars[unique];
		chars[unique] = 0;
		f(x, exclude.size()){
			chars[exclude[x]] -= qt;
		}
		return qt;
	}
	return 0;

}
