#include <iostream>
#include <fstream>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <map>

#define fi "d.inp"
#define fo "d.out"
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace std;

void input();
void output();
bool check();

void input()
{
	int ntest;
	int k, c ,s;
	scanf("%d",&ntest);
	for(int i = 1 ; i <= ntest; i++){
		printf("Case #%d:", i);
		scanf("%d %d %d",&k, &c, &s);
		if(s < k)
			printf(" IMPOSSIBLE");
		else {
			long long re = 1;
			long long gap = 1;
			
			for(int j = 1 ; j < c ; j++)
				gap *= k;
			
			for(int j = 1 ; j <= k; j++){
				printf(" %lld", re);
				re += gap;
			}
		}
		
		printf("\n");
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
