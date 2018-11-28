#include <iostream>
#include <vector>
#include <string>
#include <bitset>
using namespace std;
void exe();

int main(void)
{	
	int T;
	cin >> T;
	for(int caseNum=1; caseNum<=T ; ++caseNum){
		cout << "Case #" << caseNum << ": ";
		exe();
		cout << endl;	
	}
	return 0;
}

void exe()
{
	int num; cin >> num;
	if(num==0) cout << "INSOMNIA";
	else{	
		vector<int> digits;
		while(num>0){
			digits.push_back(num%10);
			num/=10;
		}
		auto digitsOfCount = digits;
		
		bitset<10> digitsFlag;
		for(auto digit : digits) digitsFlag.set(digit);
		if(digitsFlag.all()) cout << num;
		else{
			while(digitsOfCount.size() <= digits.size() + 1){
				int carry = 0;
				auto countIter = digitsOfCount.begin();
				for(auto digit : digits){
					*countIter += digit + carry;
					if(*countIter >= 10) carry=1, *countIter-=10;
					else carry = 0;
					digitsFlag.set(*countIter);
					++countIter;
				}
				while(carry==1 && countIter!=digitsOfCount.end()){
					*countIter += 1;
					if(*countIter >= 10) *countIter-=10;
					else carry = 0;
					digitsFlag.set(*countIter);
					++countIter;
				}
				if(carry==1) digitsOfCount.push_back(1), digitsFlag.set(1);
				if(digitsFlag.all()) break;
			}
			if(digitsFlag.all()){
				for(auto iter=digitsOfCount.crbegin() ; iter!=digitsOfCount.crend() ; ++iter)
					cout << *iter;
			}
			else cout << "INSOMNIA";
		}
	}
}
