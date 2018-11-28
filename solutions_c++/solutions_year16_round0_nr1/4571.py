#include <iostream>
#include <stdio.h>
#include <cstdlib>
#include <string>
#include <vector>
#include <bitset>
#include <cmath>

using namespace std;

typedef long long BigInt;

/*BigInt pancakes_flip(const string &s)
{
	BigInt n_flips = 0;
	char c = s[0];
	BigInt n = s.size();
	
	for (int i=1;i<n;i++){
		if (s[i]!=s[i-1]){ n_flips++; c=s[i]; }
	}
	if (c=='-') n_flips++;
	
	return n_flips;
}

int main()
{
	BigInt T;
	string s;
	
	cin >> T;
	for (BigInt c=1;c<=T;c++){
		cin >> s;
		
		BigInt n_flips = pancakes_flip(s);
		
		cout << "Case #" << c << ": " << n_flips << endl;
	}
	
	return 0;
}*/

BigInt count_sheep(BigInt N)
{
	BigInt final_N = 0;
	
	if (N == 0) return -1;
	
	std::bitset<10> num_seen(0);
	
	//cout << "****** New case N = " << N << "*****************\n\n";
	
	while (num_seen.count() != 10){
		final_N += N;
		BigInt temp_N = final_N;
		do{
			num_seen.set(temp_N%10,true);
			temp_N /= 10;
			//cout << "temp_N: " << temp_N << endl; 
		}while (temp_N);
		//cout << "final_N: " << final_N << endl;
		//fflush(stdin); scanf("%*c");
	}
	
	return final_N;
}

int main()
{
	BigInt T, N;
	
	cin >> T;
	for (BigInt c=1;c<=T;c++){
		cin >> N;
		BigInt final_N = count_sheep(N);
		if (final_N<0) cout << "Case #" << c << ": " << "INSOMNIA" << endl;
		else cout << "Case #" << c << ": " << final_N << endl;
	}
	
	return 0;
}
