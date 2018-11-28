#include<iostream>
#include<set>
#include<string>

using namespace std;

int main(){

	int numberOfCase;
	cin >> numberOfCase;
	

	for(int i = 0; i < numberOfCase; i++){
		
		int times = 1;		
		set<int> digits;
		
		int N;
		cin >> N;
	
		/* test
		digits.insert(1);
		digits.insert(1);
		digits.insert(1);
		cout << digits.size() << endl;
		*/

		if(N == 0){
			cout << "case #" << (i+1) << ": INSOMNIA" << endl;
			continue;
		}
		
		string s = to_string(N);
		for(int j = 0; j < s.size(); j++){
			int a = s[j] - '0'; // convert char to int
			digits.insert(a);
		}

		while(digits.size() < 10){
			//cout << "yes" << endl;
			times++;
			//cout << times << endl;
			int M;
			M = times*N;
			//cout << M << endl;
			s = to_string(M);
			for(int j = 0; j < s.size(); j++){
				int a = s[j] - '0'; // convert char to int
				digits.insert(a);
			}
			//cout << digits.size() << endl;
			//break;
		}

		cout << "case #" << (i+1) << ": " << s << endl;
	}

	return 0;
}
