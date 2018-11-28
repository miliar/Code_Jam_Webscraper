#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

bool is_pal(unsigned long long int in){
	char buf[21];
	int len = sprintf(buf, "%llu", in);
	bool res = true;
	int begin = 0, end = len - 1;
	while (res && (begin < end)){
		if (buf[begin] != buf[end])
			res = false;
		begin++;
		end--;
	}
	return res;
}

int main(){
	int T, case_num;
	cin >> T;
	for (case_num = 1; case_num <= T; ++case_num){
		unsigned long long int A, B, a, b, i;
		int counter = 0;
		cin >> A >> B;
		a = (unsigned long long int)sqrt(A);
		if (a * a < A)
			a += 1;
		b = (unsigned long long int)sqrt(B);
		for (i = a; i <= b; i++){
			if (is_pal(i) && is_pal(i*i))
				counter ++;
		}
		cout << "Case #" << case_num << ": " << counter << endl;
	}//Main Loop
	return 0;
}

