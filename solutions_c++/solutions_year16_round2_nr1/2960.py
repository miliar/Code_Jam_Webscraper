#include <string>
#include <iostream>

using namespace std;
int T;

int main(){
	cin >> T;
	for(int i=0; i < T; i ++){
		string str;
		int count[15]; //E F G H I N O R S T U V W X Z
		int num[10];//0 1 2 3 4 5 6 7 8 9
		for(int j = 0; j < 15; j ++)
			count[j] = 0;
		for(int j = 0; j < 10; j++)
			num[j] = 0;
		cin >> str;
		for(int j = 0; j < str.length(); j++){
			if(str[j] == 'E')
				count[0]++;
			else if(str[j] == 'F')
				count[1]++;
			else if(str[j] == 'G')
				count[2]++;
			else if(str[j] == 'H')
				count[3]++;
			else if(str[j] == 'I')
				count[4]++;
			else if(str[j] == 'N')
				count[5]++;
			else if(str[j] == 'O')
				count[6]++;
			else if(str[j] == 'R')
				count[7]++;
			else if(str[j] == 'S')
				count[8]++;
			else if(str[j] == 'T')
				count[9]++;
			else if(str[j] == 'U')
				count[10]++;
			else if(str[j] == 'V')
				count[11]++;
			else if(str[j] == 'X')
				count[12]++;
			else if(str[j] == 'W')
				count[13]++;
			else // 'Z'
				count[14]++;
		}
		num[0] = count[14];
		num[2] = count[13];
		num[8] = count[2];
		num[6] = count[12];
		num[4] = count[10];
		num[1] = count[6] - num[0] - num[2] - num[4];
		num[7] = count[8] - num[6];
		num[5] = count[11] - num[7];
		num[3] = count[3] - num[8];
		num[9] = count[4] - num[6] - num[8] - num[5];

		cout << "Case #" << i+1 << ": " ;
		for(int j = 0; j < 10; j++){
			for(int k = 0; k < num[j]; k++)
				cout << j;
		}
		cout << endl;

	}
}