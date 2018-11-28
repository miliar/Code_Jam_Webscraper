#include <iostream>
using namespace std;
int main(){
	int t;
	cin >> t;
	for(int x = 1;x <=t; x++){
		cout <<"Case #" << x <<": ";
		string S;
		cin >> S;
		int C[26] = {0};
		int l = S.length();
		for(int i = 0; i < l; i++)
			C[S[i]-'A']++;
		int d[10]={0};
		d[0] = C['Z'-'A'];
		C['Z'-'A'] -= d[0];
		C['E'-'A'] -= d[0];
		C['R'-'A'] -= d[0];
		C['O'-'A'] -= d[0];
		d[6] = C['X'-'A'];
		C['X'-'A'] -= d[6];
		C['S'-'A'] -= d[6];
		C['I'-'A'] -= d[6];
		d[8] = C['G'-'A'];
		C['G'-'A'] -= d[8];
		C['E'-'A'] -= d[8];
		C['I'-'A'] -= d[8];
		C['H'-'A'] -= d[8];
		C['T'-'A'] -= d[8];
		d[4] = C['U'-'A'];
		C['U'-'A'] -= d[4];
		C['R'-'A'] -= d[4];
		C['F'-'A'] -= d[4];
		C['O'-'A'] -= d[4];
		d[2] = C['W'-'A'];
		C['W'-'A'] -= d[2];
		C['T'-'A'] -= d[2];
		C['O'-'A'] -= d[2];
		d[1] = C['O'-'A'];
		C['O'-'A'] -= d[1];
		C['N'-'A'] -= d[1];
		C['E'-'A'] -= d[1];
		d[3] = C['T'-'A'];
		C['T'-'A'] -= d[3];
		C['H'-'A'] -= d[3];
		C['R'-'A'] -= d[3];
		C['E'-'A'] -= d[3] * 2;
		d[5] = C['F'-'A'];
		C['F'-'A'] -= d[5];
		C['I'-'A'] -= d[5];
		C['V'-'A'] -= d[5];
		C['E'-'A'] -= d[5];
		d[7] = C['S'-'A'];
		d[9] = C['I'-'A'];
		for(int i = 0; i < 10; i++){
			for(int j = 0; j <d[i]; j++)
				cout<<i;
		}
		cout<< endl;
	}
	return 0;
}