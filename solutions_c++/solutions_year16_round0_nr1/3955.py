#include <iostream>
#include <fstream>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define fi "A-large.in"
#define fo "a.out"
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace std;

void input();
void output();
bool check();

void input()
{
	int d[10];
	int ntest;
	long n, temp, result;
	
	scanf("%d", &ntest);
	
	for(int i = 0 ; i < ntest ; i++){
		scanf("%ld", &n);
		if(n == 0){
			printf("Case #%d: INSOMNIA\n", i + 1);
			continue;
		}
		
		for(int j = 0 ; j < 10 ; j++)
			d[j] = 0;
			
		temp = 0;
		result = 0;
			
		while(true){
			result += n;
			temp = result;
			while(temp > 0){
				d[temp % 10] = 1;
				temp /= 10;
			}
			
			int flag = 0;
			
			for(int j = 0; j < 10; j++){
				if(d[j] == 0)
					flag = 1;
			}
			
			if(flag == 0){
				printf("Case #%d: %ld\n", i + 1, result);
				break;
			}
		}
	}
}

void output()
{
}

int main() {
	
	//freopen(fi,"r",stdin);
	//freopen(fo,"w",stdout);
	
	input();
	
	return 0;
}
