#include <iostream>
#include <fstream>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <map>

#define fi "cc.inp"
#define fo "cc.out"
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace std;

int depth, nResult;
int countResult;
int array[20];
long long result[1000][20];
bool prime[100000001];

void input();
void output();
bool check();

long long getNumber(int base, int depth){
	long long b = 1;
	long long result = 0;	
	for(int i = depth - 1; i >= 0; i--){
		result += b * array[i];
		b *= base;
	}
	
	//printf("**%lld\n",result);
	
	return result;
}

long long getDivisor(long long number){
	if(number <= 100000000 && !prime[number])
		return -1;
		
	for(long long i = 2 ; i < (long long)sqrt(number); i++)
		if(number % i == 0)
			return i;
			
	return -1;
}

void toBinary(long long number){
	int count;
	int temp[20];
	
	count = 0;
	
	while(number > 0){
		temp[count++] = number % 2;
		number /= 2;
	}
	
	for(int i = count; i < depth; i++)
		printf("0");
	
	for(int i = count - 1; i >= 0 ; i--)
		printf("%d", temp[i]);
}

void generateBinary(int d){
	if(d == depth - 2){
		int temp[20];
		//getNumber(2, depth);
		for(int i = 2 ; i <= 10; i++){
			long long number = getNumber(i, depth);
			if(number == 0 || number == 1)
				return;
				
			long long divisor = getDivisor(number);
			if(divisor == -1)
				return;
				
			temp[i] = divisor;
		}
		
		result[countResult][0] = getNumber(2, depth);
		for(int i = 2; i <= 10; i++)
			result[countResult][i] = temp[i];
			
		countResult++;
		return;
	}
	
	if(countResult == nResult)
		return;	
	
	for(int i = 0 ; i <= 1 ; i++){
		array[d] = i;
		generateBinary(d + 1);
	}
}

void sieve(){
	
	for(long i = 2; i < 100000000; i++)
		if(prime[i] == false)
			for(int j = 2 ;; j++){
				if(i * j <= 100000000)
					prime[i * j] = true;
				else
					break;
			}
}

void input()
{
	int ntest;
	scanf("%d", &ntest);
	sieve();
	for(int i = 0 ; i < ntest; i++){
		scanf("%d %d", &depth, &nResult);
		printf("Case #%d:\n", i + 1);
		array[0] = 1;
		array[depth - 1] = 1;
		generateBinary(1);
		
		for(int j = 0 ; j < nResult; j++){
			//printf("%lld ", result[j][0]);
			toBinary(result[j][0]);
			for(int k = 2; k <= 10; k++)
				printf(" %lld", result[j][k]);
			
			printf("\n");
		}
		//output();
	}
	
	
}

void output()
{
	printf("123123123");
	for(int i = 0 ; i < nResult; i++){
		printf("*%lld\n", result[i][0]);
		int count;
		int temp[20];
		count = 0;
		long long number = result[i][0];
		while(number > 0){
			temp[count++] = number % 2;
			number /= 2;
		}
		
		long long r, t;
		
		for(int j = 2; j <= 10; j++){
			r = 0;
			t = 1;
			for(int k = 0 ; k < count; k++){
				r += t * temp[k];
				t *= j;
			}
			
			printf("base : %d - Number : %lld\n", j, r);
		}
	}
}

int main() {
	
	//freopen(fi,"r",stdin);
	//freopen(fo,"w",stdout);
	
	input();
	
	return 0;
}
