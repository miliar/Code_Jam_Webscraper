#include<iostream>
#include<sstream>
#include<cstdio>
#include<stack>
#include<queue>
#include<algorithm>
#include<cstring>
#include<string>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<vector>
#include<fstream>
#define constante 3.14159
using namespace std;

int main(){

	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int numCases = 0;
	int numeroCasos;
	int i = 0;
	int J = 1;
	double area = 0;
	int r;
	int t;
	int circles = 0;
	scanf("%d", &numCases);
	numeroCasos = numCases;
	while (i < numCases){
	i++;
	printf("Case #%d: ", i);
	scanf("%d%d", &r, &t);
	
	area += ((r + ((J * 2) -1))*(r + ((J * 2) -1))); 
	area -= ((r + (J * 2)-2)*(r + (J * 2)-2));
		
	while (area <= t){
	circles++;
		J++;
	area += ((r + ((J * 2) -1))*(r + ((J * 2) -1))); 
	area -= ((r + (J * 2)-2)*(r + (J * 2)-2));
			
	}
	printf("%d\n", circles);
	area = 0;
	J=1;
	circles = 0;
	}
	return 0;
}