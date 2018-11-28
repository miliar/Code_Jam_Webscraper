#include <iostream>
#include <fstream>
#include <string>
using namespace std;

struct Digit{
	int i;
	bool flag;
};
static int caseNum = 1;
void updateDigits(struct Digit sheepDigits[], unsigned long long processing){
	while(processing!=0){
		sheepDigits[processing%10].flag = true;
		processing = processing / 10;	
	}
}
bool checkDigits(struct Digit sheepDigits[]){
	bool check = true;
	for(int i=0; i<10; i++){
		check = check & sheepDigits[i].flag;
	}
	return check;
}
void sheep(unsigned long long N, ofstream& out){
	unsigned long long processing = N;
	Digit sheepDigits[10];
	bool sleep = false;
	int mul = 2;
	for(int i=0; i<10; i++){
		sheepDigits[i].i=i;
		sheepDigits[i].flag = false;
	}
	if(N != 0){
		while(processing < 100000000000){
			updateDigits(sheepDigits, processing);
			if(checkDigits(sheepDigits)){
				sleep = true;
				break;
			} 
			processing = mul * N;
			mul++;
		}
	}
	if(sleep){
		cout << "Case #" << caseNum <<": " << processing << endl;
		out << "Case #" << caseNum <<": " << processing << endl;
	}
	else{
		cout << "Case #" << caseNum <<": " << "INSOMNIA" << endl;
		out << "Case #" << caseNum <<": " << "INSOMNIA" << endl;
	}
}

int main(){
	string temp;
	ifstream file("A-large.in");
	ofstream out("output.out");
	int T;
	file >> temp;
	T=stoi(temp);
	if(T>=1 && T<=100){
		while(T!=0){
			unsigned long long N;
			file >> temp;
			N=stol(temp);
			if(N >=0 && N<= 1000000)
				sheep(N, out);
			T--;
			caseNum++;
		}
	}
	return 0;
}