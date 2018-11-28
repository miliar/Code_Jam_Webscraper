#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
#include <map>
#include <cstdio>
#include <cmath>
#include <fstream>

using namespace std;

long long generateNumber(){
	long long number = 1;
	for(int i = 0; i < 14; i++){
		number*=10;
		number+=rand()%2;
	}
	number*=10;
	number+=1;
	return number;
}

long long changeToBase(long long base, long long number){
	long long tmpBaseCound = 1;
	long long result = 0;
	while(number > 0){
		if(number%10){
			result+=tmpBaseCound;
		}
		tmpBaseCound*=base;
		number/=10;
	}
	return result;
}

int main() {
	long long test;
	int t = 0;
	cin >> t;
	set<long long> already_seen;
	for(int tIndex = 1; tIndex <= t; tIndex++){
		cout<<"Case #"<<tIndex<<": "<<endl;
		while(already_seen.size() < 50){
			long long number = generateNumber();
			vector<long long> divisors;
			for (int i = 2; i <= 10; ++i){
				long long converted = changeToBase(i, number);
				long long sq = sqrt(converted) + 2;
				for(long long tmp = 2; tmp < sq; tmp++){
					if(converted % tmp == 0){
						divisors.push_back(tmp);
						break;
					}
				}
				if(divisors.size() != i - 1){
					break;
				}
			}
			if(divisors.size() == 9){
				cout<<number;
				for(long long divr : divisors){
					cout<<" "<<divr;
				}
				cout<<endl;
				already_seen.insert(number);
			}
		}
	}
}
