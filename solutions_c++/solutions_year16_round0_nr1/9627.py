#include <iostream>
#include <sstream>
#include <cstdio>
#include <vector>
#include <string>
#include <set>

using namespace std;

long splitbits(long num){
	
	if(num == 0) return -1;
	
	int bit;
	set<int> myset;
	
	for(int i=1; i < 1000; i++){
		long t_2 = num * i;
		long temp = t_2;
		do{
			bit = temp % 10;
			temp = temp / 10;
			myset.insert(bit);
			//cout << temp << " " << bit << endl;
		} while(temp > 0);
		
		
		if(myset.size() >= 10)
			return t_2;
	}
}

int main()
{
	int T;
	cin >> T;
	getchar();
	
	vector<long> N;
	for(int k = 0;k < T; k++){
		long num;
		cin >> num;
		getchar();
		N.push_back(num);
	}
	
	for(int k = 0;k < T; k++){
		long result = splitbits(N[k]);
		if (result == -1)
			cout << "Case #" << k+1 << ": INSOMNIA\n";
		else
			cout << "Case #" << k+1 << ": " << result << endl;
	}
		
	return 0;
}