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

int p_tab[1000];
int p_tab2[1000];
int num_p_tab = 0;
int num_p_tab2 = 0;

bool isPalindromes(string & str)
{
	
	int str_len = str.length();
	int head = 0;
	int tail = str_len -1;

	while(tail >= head){
		
		if(str.at(head)!= str.at(tail))
			return false;

		tail--;
		head++;
	}

	return true;
	
}

void p_tab_init()
{
	for(int i=1; i<=1000;i++){
		char num_str[100];
		memset(num_str,0,100);
		sprintf(num_str,"%d",i);
		
		string t_str(num_str);
		if( isPalindromes(t_str) == true){
			p_tab[num_p_tab++] = i;
			//cout<<i<<endl;
		}
		
	}

	for(int i=0; i< num_p_tab;i++){
		int tv = p_tab[i];
		int tv2 = tv*tv;
		
		char num_str[100];
		memset(num_str,0,100);
		sprintf(num_str,"%d",tv2);
		string t_str(num_str);
		
		if( isPalindromes(t_str) == true && tv2 <=1000){
			p_tab2[num_p_tab2++] = tv2;
			//cout<<tv2<<endl;
		}
	}

}

int main()
{

	p_tab_init();	

	long long T;

	cin>>T;
	
	for(long long i=0;i<T;i++){

		long long result=0 ;
		int A,B;
		cin>> A>>B;
		
		for(int f=0;f<num_p_tab2;f++){
			if( p_tab2[f] >= A && p_tab2[f] <= B )
				result++;
		}

		cout<<"Case "<<"#"<<i+1<<": "<<result;
		cout<<endl;

	}
	return 0;
}


