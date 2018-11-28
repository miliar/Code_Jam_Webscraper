#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

ofstream mycout;
typedef long long Long;

int isSquare(Long n, Long &sq){
	sq = sqrt(n);
	Long t = sq*sq;
	if(t == n)
		return 1;
	else
		return 0;
}

int isPelindrome(Long n){
	Long num = n;
	Long r = 0;
	
	while(num != 0){
		int t = num % 10;
		r = r*10 + t;
		num /= 10;
	}
	
	if(r == n)
		return 1;
	else
		return 0;
}

void process(int testcase){
	Long A, B;
	cin >> A;
	cin >> B;
	
	Long count = 0;
	for(Long i = A; i <= B; i++){
		Long sq;
		int c1 = isSquare(i, sq);
		if(c1){
			int c2 = isPelindrome(i);
			if(c2){
				int c3 = isPelindrome(sq);
				if(c3)
					count++;
			}
		}
	}
	mycout << "Case #" << testcase << ": ";
	mycout << count << endl;
}

int main(){
	int T;
	cin >> T;
	
	mycout.open("output2.txt");
	for(int i = 0; i < T; i++){
		process(i+1);
	}
	mycout.close();
}
