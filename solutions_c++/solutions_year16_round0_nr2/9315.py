// first.cpp: определяет точку входа для консольного приложения.
//
#include <string>
#include <iostream>
#include <fstream>
using namespace std;

int pancakes(string& str){
	size_t size = str.size();
	string res = "";
	bool top = false;
	int N = 0;
	while (true){
		int plus = 0;
		int min = 0;
		for (int i = 0; i < size; ++i){
			if (str[i] == '-'){
				if (!plus) ++min;
				else{
					if (str[size - 1] == '+'){
						top = true;
						break;
					}
					else{
						break;
					}

				}
			}
			else {
				if (!min) ++plus;
				else{
					if (str[size - 1] == '-'){
						break;
					}
					else { break; }
				}
			}
		}
		if (min == size && N == 0)
			return 1;
		else if (plus == size && N == 0)
			return 0;
		else if (plus == size)
			return N;
		else if (min == size)
			return ++N;
		else if (plus > 0 && top){
			++N;
			res = string(plus, '-');
			str = res + str.substr(plus);
			top = false;
		}
		else if (min > 0){
			++N;
			str = str.substr(min);
			str += string(min, '+');
		}
		else if (plus > 0){
			++N;
			str = str.substr(plus);
			str += string(plus, '-');
		}
	}
}

int main()
{
	int T = 0;
	string S;
	ifstream in("D:\\B-large.in", ios_base::in);
	ofstream out("D:\\output.txt", ios_base::out);
	in >> T;
	for (int i = 0; i < T; ++i){
		in >> S;
		int N = pancakes(S);
		out << "Case #" << i + 1 << ": " << N << endl;
	}
	in.close();
	out.close();
	return 0;
}

