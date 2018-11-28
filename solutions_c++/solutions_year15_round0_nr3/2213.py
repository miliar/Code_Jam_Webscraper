#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	int L, X;
	int array[10001];
	char c;
	
	int s[5][5] = {0,0,0,0,0,0,1,1,1,1,0,1,-1,1,-1,0,1,-1,-1,1,0,1,1,-1,-1};
	int mult[5][5] = {0,0,0,0,0,0,1,2,3,4,0,2,1,4,3,0,3,4,1,2,0,4,3,2,1};
	
	for (int i = 1; i <= T ; i ++){
	
		scanf("%d", &L);
		scanf("%d", &X);
		scanf("%c", &c);

		for (int j = 0; j < L; j++){
			scanf("%c", &c);
			if (c == 'i') array[j] = 2;
			if (c == 'j') array[j] = 3;
			if (c == 'k') array[j] = 4;	
		}
		
		for (int k = 1; k < X; k++) {
			for (int j = 0; j < L ; j++) 
				array[k*L+j] = array[j];		
		}	
		
		int sign = 1; 
		int index = 0;
		int current = 1;
		int flag = 1; 
		while ((index<X*L)&(!((current == 2)&&(sign == 1)))){
			sign = sign * s[current][array[index]];
			current = mult[current][array[index]];
			index++;
		}
		if (!((current==2)&&(sign==1))) flag = 0;
		
		current = 1;
		while ((index<X*L)&(!((current == 3)&&(sign == 1)))){
			sign = sign * s[current][array[index]];
			current = mult[current][array[index]];
			index++;
		}
		if (!((current==3)&&(sign==1))) flag = 0;
	
		current = 1;
		while ((index<X*L)&(!((current == 4)&&(sign == 1)))){
			sign = sign * s[current][array[index]];
			current = mult[current][array[index]];
			index++;
		}
		if (!((current==4)&&(sign==1))) flag = 0;

		current = 1;
		while (index<X*L){
			sign = sign * s[current][array[index]];
			current = mult[current][array[index]];
			index++;
		}
		if (!((current==1)&&(sign==1))) flag = 0;


		if (flag == 1) 
			printf("Case #%d: YES\n", i);
		else 
			printf("Case #%d: NO\n", i);
		}
	

}
