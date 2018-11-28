#include <iostream>
#include <string>

using namespace std;

inline int min(int a, int b){
	if(a < b)return a;
	else return b;
}

int init(int *arr){
int	i;
	for(i = 0 ; i < 26 ; i++)arr[i] = 0;
	return 0;
}

int main() {
string	in;
int	T, i, hash[26], j, dig[10];
	cin >> T;
	for(i = 0 ; i < T ; i++){
		init(hash);
		init(dig);
		cin >> in;
		cout << "Case #" << i + 1 << ": ";
	int	count, k;
		for(j = 0 ; j < in.length() ; j++)hash[in[j] - 65]++;
		count = min(hash[25], min(hash[17], min(hash[14], hash[4])));
		hash[25] -= count;
		hash[17] -= count;
		hash[14] -= count;
		hash[4] -= count;
		dig[0] = count;
		count = min(hash[19], min(hash[8], min(hash[7], min(hash[6], hash[4]))));
		hash[19] -= count;
		hash[8] -= count;
		hash[7] -= count;
		hash[6] -= count;
		hash[4] -= count;
		dig[8] = count;
		count = min(hash[23], min(hash[18], hash[8]));
		hash[23] -= count;
		hash[18] -= count;
		hash[8] -= count;
		dig[6] = count;
		count = min(hash[22], min(hash[19], hash[14]));
		hash[22] -= count;
		hash[19] -= count;
		hash[14] -= count;
		dig[2] = count;
		count = min(hash[20], min(hash[17], min(hash[14], hash[5])));
		hash[20] -= count;
		hash[17] -= count;
		hash[14] -= count;
		hash[5] -= count;
		dig[4] = count;
		count = min(hash[21], min(hash[8], min(hash[5], hash[4])));
		hash[21] -= count;
		hash[8] -= count;
		hash[5] -= count;
		hash[4] -= count;
		dig[5] = count;
		count = min(hash[21], min(hash[18], min(hash[13], hash[4] / 2)));
		hash[21] -= count;
		hash[18] -= count;
		hash[13] -= count;
		hash[4] -= 2 * count;
		dig[7] = count;
		count = min(hash[14], min(hash[13], hash[4]));
		hash[14] -= count;
		hash[13] -= count;
		hash[4] -= count;
		dig[1] = count;
		count = min(hash[19], min(hash[17], min(hash[7], hash[4] / 2)));
		hash[19] -= count;
		hash[17] -= count;
		hash[7] -= count;
		hash[4] -= 2 * count;
		dig[3] = count;
		count = min(hash[13] / 2, min(hash[8], hash[4]));
		hash[13] -= 2 * count;
		hash[8] -= count;
		hash[4] -= count;
		dig[9] = count;
		for(j = 0 ; j < 10 ; j++){
			for(k = 0 ; k < dig[j] ; k++)cout << j;
		}
		cout << endl;
	}
	return 0;
}
