#include<bits/stdc++.h>

using namespace std;

int main() {
	ifstream in("A-large.in");
	int tests;
	in >> tests;
	for(int t = 0; t < tests; ++t){
		string s;
		in >> s;
		int arr[26];
		int nums[10];
		for(int i =0 ;i < 26; i++){
			arr[i] = 0;
		}
		for(int i = 0; i < s.length(); i++){
			arr[(int)(s[i]-'A')]++;
		}
		nums[0] = arr['Z'-'A'];
		arr['E'-'A'] -= nums[0];
		arr['R'-'A'] -= nums[0];
		arr['O'-'A'] -= nums[0];
		nums[2] = arr['W'-'A'];
		arr['T'-'A'] -= nums[2];
		arr['O'-'A'] -= nums[2];
		nums[4] = arr['U'-'A'];
		arr['F'-'A'] -= nums[4];
		arr['R'-'A'] -= nums[4];
		arr['O'-'A'] -= nums[4];
		nums[5] = arr['F'-'A'];
		arr['I'-'A'] -= nums[5];
		arr['V'-'A'] -= nums[5];
		arr['E'-'A'] -= nums[5];
		nums[7] = arr['V'-'A'];
		arr['S'-'A'] -= nums[7];
		arr['N'-'A'] -= nums[7];
		arr['E'-'A'] -= (nums[7]*2);
		nums[6] = arr['X'-'A'];
		arr['S'-'A'] -= nums[6];
		arr['I'-'A'] -= nums[6];
		nums[3] = arr['R'-'A'];
		arr['T'-'A'] -= nums[3];
		arr['H'-'A'] -= nums[3];
		arr['E'-'A'] -= (nums[3]*2);
		nums[8] = arr['T'-'A'];
		arr['E'-'A'] -= nums[8];
		arr['I'-'A'] -= nums[8];
		arr['G'-'A'] -= nums[8];
		arr['H'-'A'] -= nums[8];
		nums[9] = arr['I'-'A'];
		arr['N'-'A'] -= (nums[9]*2);
		arr['E'-'A'] -= nums[9];
		nums[1] = arr['O'-'A'];
		cout << "Case #" << t+1 << ": ";
		for(int i = 0; i < 10; i++)
		{
			for(int j = 0; j < nums[i]; j++){
				cout << i;
			}
		}
		cout << endl;
	}

	return 0;
}
