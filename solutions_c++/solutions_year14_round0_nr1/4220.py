#include <iostream>
#include <list>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>

#define ASCII_SPACE 32
#define ASCII_NEWLINE 10


using namespace std;




#define PRINT_TOKEN(token)\
	do{\
		cout<<#token<<" is "<<token<<endl; \
	}while(0)


#define READ(arg)\
	do{\
		long long arg;\
		cin>>arg;\
	}while(0)

//#define PRINT_ARR()
typedef long long ll;

int ans[2];
int table[2][4][4];

int number;

void printInput()
{
	for(int i=0; i< 2;i++){
		cout<< ans[i] << endl;
		for(int row = 0; row< 4;row++){

			for(int col = 0; col < 4;col++){
				cout<< table[i][row][col]<< " ";
			}
			cout<<endl;
		}
	}
}

int solve()
{
	int result = 0;

	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(table[0][ans[0]-1][i] == table[1][ans[1]-1][j]){
				result++;
				number = table[0][ans[0]-1][i];
			}
		}
	}

	return result;
}

int main()
{
	long long T;

	cin>>T;

	for(long long i=0;i<T;i++){

		long long result=0 ;
		for(int idx = 0; idx< 2; idx++){
			cin >> ans[idx];
			for(int row = 0; row< 4; row++){
				for(int col = 0; col <4; col++){
					cin >> table[idx][row][col];
				}
			}
		}
		//printInput();
		result = solve();
		cout<<"Case "<<"#"<<i+1<<": ";
		if(result == 0)
			cout<<"Volunteer cheated!";
		else if (result == 1)
			cout<<number;
		else
			cout<<"Bad magician!";
		cout<<endl;

	}
	return 0;
}


