#include <iostream>
#include <string>

using namespace std;

int arr[128];

int numOf[10];
/**
0 : EORZ -> Z
1 : ENO ---> O
2 : OWT -> W
3 : EEHRT ---> T
4 : FORU -> U
5 : EFIV ---> F
6 : ISX -> X
7 : EENSV ------> V
8 : EGHIT -> G
9 : EINN -------->I
**/

void fun(){
	int temp;

	temp = arr['Z'];
	numOf[0] = temp;
	arr['Z'] -= temp;
	arr['E'] -= temp;
	arr['R'] -= temp;
	arr['O'] -= temp;

	temp = arr['W'];
	numOf[2] = temp;
	arr['T'] -= temp;
	arr['W'] -= temp;
	arr['O'] -= temp;
	
	temp = arr['U'];
	numOf[4] = temp;
	arr['F'] -= temp;
	arr['O'] -= temp;
	arr['U'] -= temp;
	arr['R'] -= temp;

	temp = arr['X'];
	numOf[6] = temp;
	arr['S'] -= temp;
	arr['I'] -= temp;
	arr['X'] -= temp;

	temp = arr['G'];
	numOf[8] = temp;
	arr['E'] -= temp;
	arr['I'] -= temp;
	arr['G'] -= temp;
	arr['H'] -= temp;
	arr['T'] -= temp;

	temp = arr['O'];
	numOf[1] = temp;
	arr['O'] -= temp;
	arr['N'] -= temp;
	arr['E'] -= temp;

	temp = arr['T'];
	numOf[3] = temp;
	arr['T'] -= temp;
	arr['H'] -= temp;
	arr['R'] -= temp;
	arr['E'] -= temp;
	arr['E'] -= temp;

	temp = arr['F'];
	numOf[5] = temp;
	arr['F'] -= temp;
	arr['I'] -= temp;
	arr['V'] -= temp;
	arr['E'] -= temp;

	temp = arr['V'];
	numOf[7] = temp;
	arr['S'] -= temp;
	arr['E'] -= temp;
	arr['V'] -= temp;
	arr['E'] -= temp;
	arr['N'] -= temp;

	temp = arr['I'];
	numOf[9] = temp;
	arr['N'] -= temp;
	arr['I'] -= temp;
	arr['N'] -= temp;
	arr['E'] -= temp;
}

int main(){
	int n; 
	cin >> n;

	for(int i = 1; i <= n; i++){
		string str;
		cin >> str;

		int len = str.length();
		for(int i = 0; i < len; i++){
			arr[(int)(str[i])]++;
		}

		fun();

		cout << "Case #" << i << ": ";
		for(int i = 0; i < 10; i++)
			for(int j = 0; j < numOf[i]; j++)
				cout << i;

		cout << endl;

		for(int i = 0; i < 128; i++)
			arr[i] = 0;
		for(int i = 0; i < 10; i++)
			numOf[i] = 0;
	}

	return 0;
}