#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

class Quaternion {
 private:
	int value;
	short sign;
 public:
	Quaternion(char q, short sgn = 1){
		if (q == 'i'){
			value = 2;
		} else if (q == 'j'){
			value = 3;
		} else if (q == 'k'){
			value = 4;
		} else {
			value = 1;
		}
		
		if (sgn == -1){
			sign = -1;
		} else {
			sign = 1;
		}
	}
	
	char getValue(){
		switch (value){
			case 2:
				return 'i';
			case 3:
				return 'j';
			case 4:
				return 'k';
			default:
				return '1';
		}
	}
	
	short getSign(){
		return sign;
	}
	
	bool isOne(){
		return value == 1;
	}
	
	bool isI(){
		return value == 2;
	}
	
	bool isJ(){
		return value == 3;
	}
	
	bool isK(){
		return value == 4;
	}	
	
	Quaternion pow(uint64_t exp){
	 	Quaternion Q1(1), Qm1(1, -1);

		bool isEven = exp % 2 == 0;
		if (isOne()){
			if (sign == 1){
				return Q1;
			}
			return isEven ? Q1 : Qm1;
		}
	
		Quaternion sign = Qm1.pow(exp/2);
		if (isEven){
			return sign;
		}
		return *this * sign;
	}

	Quaternion operator*(char q){
		return *this * Quaternion(q);
	}
	
	Quaternion operator*(Quaternion q){
		short s = sign * q.getSign();
		if (isOne()){
			return Quaternion(q.getValue(), s);
		}
		if (q.isOne()){
			return Quaternion(getValue(), s);
		}
		if (getValue() == q.getValue()){
			return Quaternion('1', -s);
		}
		// i
		if (isI()){
			if (q.isJ()){
				return Quaternion('k', s);
			}			
			return Quaternion('j', -s);
		}
		// j
		if (isJ()){
			if (q.isI()){
				return Quaternion('k', -s);
			}
			return Quaternion('i', s);
		}
		// k
		if (q.isI()){
			return Quaternion('j', s);
		}
		return Quaternion('i', -s);
	}
};

string substring(string str, int begin, int end = -1){
	if (end < 0){
		end = str.length();
	}
	stringstream stream;
	for (int i = begin; i < end; i++){
		stream << str.at(i);
	}
	return stream.str();
}

ostream& operator<<(ostream &stream, Quaternion &q){
	return stream << (q.getSign() == -1 ? "-" : "") << q.getValue();
}

char simpleParse(string expression){
	int L = expression.length();
	Quaternion q(1);
	for (uint64_t i = 0; i < L; i++){
		char value = expression.at(i);
		q = q * Quaternion(value);
	}
	return q.getValue();
}

string parse(uint64_t L, uint64_t X, string expression){
	if (L == 1){
		return "NO";
	}
	
	bool allEqual = true;
	char first = expression.at(0);
	Quaternion q(1);
	uint64_t i;
	for (i = 0; i < L; i++){
		char value = expression.at(i);
		if (value != first){
			allEqual = false;
		}
		q = q * Quaternion(value);
	}	
	q = q.pow(X);
	
	if (allEqual || q.getValue() != '1' || q.getSign() != -1){
		return "NO";
	}
	

	stringstream stream;
	for (i = 0; i < X; i++){
		stream << expression;
	}
	expression = stream.str();
	
	uint64_t length = L * X;
	string s1, s2, s3;
	for (i = 0; i < length; i++){
		s1 = substring(expression, 0, i);
		if (simpleParse(s1) != 'i'){
			continue;
		}
		
		for (uint64_t j = i + 1; j < length; j++){
			s2 = substring(expression, i, j);
			if (simpleParse(s2) != 'j'){
				continue;
			}
			
			s3 = substring(expression, j);
			if (simpleParse(s3) == 'k'){
				return "YES";
			}
		}
	}
		
	return "NO";
}

int main(){
	ifstream input("C_small2.in");
	ofstream output("output.txt");
	int numberOfCases, i = 0;
	uint64_t L, X;
	string expression;
	
	input >> numberOfCases;
	while (input >> L >> X){
		input >> expression;
		string solution = parse(L, X, expression);
		output << "Case #" << ++i << ": " << solution << endl;
	}	
}