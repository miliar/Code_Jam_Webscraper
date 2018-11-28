/*
 * countingSheep.cc
 *
 *  Created on: Apr 8, 2016
 *      Author: Terrence
 */
#include <iostream>
#include <vector>
#include <cmath>
#include <math.h>
#include <fstream>

using namespace std;

vector<long long> getdigit(long long n){
	vector<long long> digit;
	long long num,count = 0;
	long long i = 10;
	while(1){
		count++;
		if(n/i <= 0)
			break;
		i*=10;
	}
	for(long long j = count; j> 0; j--){
		num = pow(10,j-1);
		digit.push_back((n/num)%10);
	}
	return digit;
}

bool Allcontain(bool arr[10]){
	for(int i = 0; i<10;i++){
		if(arr[i] == false)
			return false;
	}
	return true;
}

long long counting(long long n){
	if(n==0){
		return 0;
	}
	bool flag[10];
	for(long long i = 0; i< 10; i++){
		flag[i] = false;
	}
	long long i = 1;
	long long number;
	while(1){
		number = n*i;
		vector<long long> num = getdigit(number);
		for(vector<long long>::iterator it = num.begin();it != num.end();it++){
			flag[*it] = true;
		}
		i++;
		if(Allcontain(flag)){
			break;
		}
	}
	//cout<<number;
	return number;
}

int main(){
	ifstream in("A-large.in.txt");
	ofstream out("output.txt");
	int title;
	in>>title;
	long long numberset;
	long long i = 1;
	long long results;
	while(in>>numberset){
		results = counting(numberset);
		if(results == 0){
			out<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
		}
		else{
			out<<"Case #"<<i<<": "<<results<<endl;
		}
		i++;
	}
}



