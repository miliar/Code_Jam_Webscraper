#include <iostream>
#include <fstream>
#include <math.h> 
#include <conio.h>

using namespace std;

std::ifstream fin;
std::ofstream fout;
	

int numString[100];
int N, J;
int counter;

void doSth();


long long power (int base, int exp)
{
	long long res = 1;
	for (int i=0;i<exp;i++)
		res = res * base;
		
	return res;
}


void generate (int i)
{
	if (counter == J)
		return;
	
	if (i == N){
		doSth();
		return;
	}
	
	numString[i] = 0;
		generate(i+1);
	
	numString[i] = 1;
		generate(i+1);
	
}


long long interpret(int base)
{
	long long num = 0;
	for (int i=0; i<N; i++){
		if (numString[i] == 1)
			num += power(base,N-1-i);
	}
	return num;
}

int isPprime(long long num)
{
	int isprime = 1;
	for(int i = 2; i <= sqrt(num); i++)
	{
		if((num % i) == 0)
		{
			isprime = i;
			break;
		}
	}

	return isprime;
}



void doSth()
{
	/*for (int i=0; i<N; i++){
		cout<<numString[i];
	}
	cout<<endl;*/
	
	if (numString[0] == 0 || numString[N-1] == 0)
		return;
		
	int isJam = 1;	
	int div[15];
	long long test[15];
	for (int b=2; b<=10; b++){
		long long num = interpret(b);
		test[b] = interpret(b);
		//cout<<test[b]<<endl;
		//getch();
		int temp = isPprime(num);
		if (temp != 1){
			div[b] = temp; 
		} else {
			isJam = 0;
			break;
		}	
	}
	
	if(isJam){
		for (int i=0; i<N; i++){
			fout<<numString[i];
		}
		for (int i=2;i<=10;i++){	
			cout<<test[i]<<"%"<<div[i]<<" = "<<test[i]%div[i]<<endl;
		}
		cout<<endl;
		//getch();
			
		
		for (int i=2;i<=10;i++){	
			fout<<" "<<div[i];
		}
		fout<<endl;
		counter++;
	}
	
}
	




int main ()
{
	
	fin.open("C_small.txt", std::ifstream::in);
	fout.open("C_small_out.txt", std::ifstream::out);
	
	int no_tc;
	fin >> no_tc;
	
	
	for (int tc=1; tc<=no_tc; tc++){
		fin>>N>>J;
		counter = 0;
		
		fout<<"Case #"<<tc<<":"<<endl;
		generate(0);
		
		
	}
	
	return 0;
	
}
