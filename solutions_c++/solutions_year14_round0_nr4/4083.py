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
int N ;
double data[2][1000];

void printInput()
{
	for(int a = 0;a<2;a++){
		for(int b= 0; b< N ;b++){
			cout<< data[a][b] <<" ";
		}
		cout<<endl;
	}
	cout<<endl;
}

int solveA()
{
	int result = 0;
	
	int round = 0;
	int woman_small = 0;
	int woman_large = N-1;
	int man_small = 0;
	int man_large = N-1;

	for(round = 0; round < N; round++){
		if(data[0][woman_small] < data[1][man_small]){
			woman_small++;
			man_large--;
		}else {
			woman_small++;
			man_small++;
			result++;
		}
	}

	return result;
}
int solveB()
{
	int man_win=0;
	for(int i=0;i<N;i++){
		
		double woman_val = data[0][i];

		int man_idx=0;
		while(data[1][man_idx]<data[0][i]){
			man_idx++;
			if(man_idx >= N){
				break;
			}
		}

		if(man_idx >= N){
			break;
		}
		data[1][man_idx] = -1;
		man_win++;
	}
	return N-man_win;
}

int main()
{
	long long T;

	cin>>T;
	
	for(long long i=0;i<T;i++){

		long long result=0 ;
		cin>> N;
		for(int a = 0; a<2;a++){
			for(int b = 0; b<N;b++){
				cin>>data[a][b];
			}
		}
		//printInput();
		sort(&data[0][0],&data[0][N]);
		sort(&data[1][0],&data[1][N]);
		//printInput();
		int ansA = solveA();
		int ansB = solveB();
		cout<<"Case "<<"#"<<i+1<<": "<<ansA <<" "<<ansB;
		cout<<endl;

	}
	return 0;
}


