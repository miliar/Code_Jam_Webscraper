#include <iostream>
#include <list>
#include <math.h>
#include <iterator>
#include <fstream>
#include <algorithm>

class BigInt {
private:
	std::list<short> num;

public:
	BigInt(){};
	BigInt(int newnum);
	BigInt(BigInt &rhs) {num = rhs.num;};
	~BigInt(){};

	int getNum();
	void setNum(int);
	BigInt operator*(int);
	BigInt &operator=(const BigInt &);
	bool operator==(BigInt &);
	BigInt maxNum();
};
bool allElements(bool *, int);

int main(){
	int N(0), number(0);
	BigInt first;

	std::ifstream input;
	std::ofstream output;
	input.open ("A-large.in");
	output.open ("Problem1Solution.txt");
	input >> N;

	for(int i(0); i < N; ++i){
		input >> number;
		if(number == int(0)){
//			std::cout << "Case #" << i + 1 << ": INSOMNIA\n";
			output << "Case #" << i + 1 << ": INSOMNIA\n";
		}
		else{
			first.setNum(number);
		
//			std::cout << "Case #" << i + 1 << ": ";
			output << "Case #" << i + 1 << ": ";
			first = first.maxNum();
//			std::cout << first.getNum() << std::endl;
			output << first.getNum() << std::endl;
		}
	}

	return 0;
}

BigInt::BigInt(int newnum){
	short remainder(0);
	while(newnum > 0){
		remainder = newnum % 10;
		newnum /= 10;
		num.push_back(remainder);
	}
}
void BigInt::setNum(int newnum){
	num.resize(0);
	if(newnum == 0){
		num.push_back(0);
		return;
	}

	short remainder(0);
	while(newnum > 0){
		remainder = newnum % 10;
		newnum /= 10;
		num.push_back(remainder);
	}
}
int BigInt::getNum(){
	int value(0), count(0);
	for(std::list<short>::iterator it = num.begin(); it != num.end(); ++it){
		value += (*it) * pow(10,count);
		count++;
	}
	return value;
}
BigInt BigInt::operator*(int mult){
	BigInt newNum;
	newNum = *this;
	if(mult == 0){
		newNum.setNum(0);
		return newNum;
	} 
	short temp(0), carry(0);
	for(std::list<short>::iterator it = newNum.num.begin(); it != newNum.num.end(); ++it){
		temp = (*it) * mult + carry;
		carry = 0;
		if(temp < 10)
			*it = temp;
		else {
			carry = temp / 10;
			*it = temp % 10;
		}
	}
	while (carry > 0){
		if(carry < 10){
			newNum.num.push_back(carry);
			carry = 0;
		}
		else{
			newNum.num.push_back(carry % 10);
			carry /= 10;
		}
	}
	return newNum;
}
BigInt &BigInt::operator=(const BigInt &rhs){
	num = rhs.num;
	return *this;
}
bool BigInt::operator==(BigInt &rhs){
	if(num.size() != rhs.num.size())
		return false;
	std::list<short>::iterator it2 = rhs.num.begin();
	for(std::list<short>::iterator it1 = num.begin(); it1 != num.end(); ++it1){
		if(*it1 != *it2)
			return false;
		++it2;
	}
	return true;
}
BigInt BigInt::maxNum(){
	BigInt second, third;
	second = *this;
	int count(1);
	bool *ptr = new bool[10];
	bool all = false;
	for(int i(0); i < 10; ++i)
		ptr[i] = false;

	while(!all){
		for(std::list<short>::iterator it = second.num.begin(); it != second.num.end(); ++it)
			ptr[*it] = true;
		all = allElements(ptr, 10);
		count++;
		second = *this * count;
	}
	second = *this * (count - 1);
	return second;
}
bool allElements(bool *list, int size){
	for(int i(0); i < size; ++i)
		if(!list[i])
			return false;

	return true;
}
