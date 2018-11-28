
#include <cstdio>
#include <algorithm>
#include <math.h>
#include <string>
#include <cstring>
using namespace std;

int main()
{	
	//inputFile = fopen("A-small-attempt0.in", "r");
	//inputFile = fopen("input.txt", "r");
	//outputFile = fopen("output.txt", "w");
	freopen("D-small-attempt0.in", "r", stdin);
	//freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tCase;
	int k;
	int c;
	int s;
	
	scanf("%d", &tCase);
	
	for (int i = 1 ; i <= tCase ; i++){
		scanf("%d", &k);
		scanf("%d", &c);
		scanf("%d", &s);
		printf("Case #%d: ",i);
		for (int j = 0; j < k ; j++){
			printf("%d ", j+1);
		}
		printf("\n");
	} 
	
	return 0;
}


