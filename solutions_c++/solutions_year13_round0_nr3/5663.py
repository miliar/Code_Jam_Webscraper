#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <math.h>
#include <regex.h>
using namespace std;

int reverse(int num) {
	int rnum = 0, temp = num;
	while(temp != 0){
		rnum = rnum * 10 + temp % 10;
		temp /= 10;
	}
	return rnum;
}

bool isPalindrome(int num) {
	int temp = reverse(num);
	if ((num-temp) == 0) return true;
	else return false;
}

int main (int argc, char * const argv[]) {
	
    // HANDLE COMMAND-LINE ARGUMENTS
	freopen(argv[1], "rt", stdin);
	
//	freopen("example.in", "rt", stdin);

	if(argc == 3){
		freopen(argv[2], "wt", stdout);
	}else if(argc==2){
		string out = argv[1];
		out = out.substr(0, out.size() - 2);
		out += "out";
		cout << "Result file: " << out << endl;
		freopen(out.c_str(), "wt", stdout);
	}
	else {
		cout << "Input file required!\nUsage: ./" << argv[0] << " example.in [example.out]" << endl;
		return 0;	
	}
	
	int N = 0;	
	cin >> N;
	// for each test case
	for(int testCaseNum=0; testCaseNum<N; ++testCaseNum){		
		cout << "Case #" << testCaseNum+1 << ": ";
		
		int answer = 0;
		
		// get bounds
		int first, last;
		cin >> first >> last;
		
		for (int i=first; i<=last; ++i) {
			if (isPalindrome(i)) {
				int test_num_sqrt = sqrt(i);
				if (test_num_sqrt * test_num_sqrt == i && isPalindrome(test_num_sqrt)) ++answer;
			}
		}
		cout << answer << endl;
	}
	return 0;
}










