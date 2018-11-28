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

int tab[100][100];
int N,M;
int wtab[100][100];
bool checkLegal(int local_tab[100][100]);
void printTab()
{
	for(int n = 0;n<N;n++){
		for(int m=0;m<M;m++){
			cout <<wtab[n][m]<<" ";
		}
		cout<<endl;
	}
	cout<<endl;

}

bool findMinDiffAndMow()
{
	int min_diff = 100000;
	int temp_n=-1;
	int temp_m=-1;
	for(int n=0;n<N;n++){
		for(int m=0;m<M;m++){
			int temp_diff = wtab[n][m] - tab[n][m];

			if(temp_diff >0 && min_diff > temp_diff){
				min_diff = temp_diff;
				temp_n = n;
				temp_m = m;
			}
		}
	}

	cout<<"min_diff:"<<min_diff<<",n:"<<temp_n<<",m:"<<temp_m<<endl;

	int temp_tab[100][100];
	memcpy(temp_tab, wtab,sizeof(wtab));
	
	int val = wtab[temp_n][temp_m] - min_diff;
	for(int n=0;n<N;n++){
		temp_tab[n][temp_m] = val;
	}
	bool isOK = checkLegal(temp_tab);

	if(isOK){
		memcpy(wtab,temp_tab,sizeof(wtab));
	}

	memcpy(temp_tab, wtab,sizeof(wtab));
	for(int m=0;m<M;m++){
		temp_tab[temp_n][m] = val;	
	}
	bool isOK2 = checkLegal(temp_tab);
	if(isOK2){
		memcpy(wtab,temp_tab,sizeof(wtab));
	}

	if(isOK2 || isOK)
		return true;
	else
		return false;
}
bool checkLegal(int local_tab[100][100])
{
	for(int n=0;n<N;n++){
		for(int m=0;m<M;m++){
			if(local_tab[n][m] < tab[n][m]){
				return false;
			}
		}
	}

	return true;

}
bool checkFinish()
{
	for(int n=0;n<N;n++){
		for(int m=0;m<M;m++){
			if(wtab[n][m] != tab[n][m]){
				return false;
			}
		}
	}

	return true;

}
int main()
{
	long long T;

	cin>>T;
	
	for(long long i=0;i<T;i++){
		cin>> N >>M;
	
		for(int n=0;n<N;n++){
			for(int m=0;m<M;m++){
				cin>>tab[n][m];
				wtab[n][m] = 100;
			}
		}
	
		long long result=0 ;
		
		bool isFin;
		printTab();
		bool isSuccess;
		while(1){
			isFin = checkFinish();
			if(isFin){
				result = 0;
				break;
			}
		    
			isSuccess = findMinDiffAndMow();
			printTab();

			if(!isSuccess){
				result = -1;
				break;
			}
		}

		//printTab();
		if(result == 0)
			cout<<"Case "<<"#"<<i+1<<": YES";
		else
			cout<<"Case "<<"#"<<i+1<<": NO";
			
		cout<<endl;

	}
	return 0;
}


